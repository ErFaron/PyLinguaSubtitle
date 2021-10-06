# Составляет таблицу из слов в субтитрах (Слово - количество)
import pysrt, re, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func
from sqlalchemy.sql.functions import coalesce
from Stemmer import Stemmer
from DictTable import DictTableItem
from timeit import timeit


class SRTItem:
    def __init__(self, path):
        self.stem_index = dict()
        self.subs = pysrt.open(path)
        self.engine = create_engine('sqlite:///:memory:', echo=False)
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()
        self.metadata = MetaData(self.engine)
        self.srt_table = Table('words', self.metadata,
                               Column('Stem', String, primary_key=True),
                               Column('Word', String),
                               Column('Amount', Integer),
                               )
        self.dictionary_table = Table()
        self.metadata.create_all(self.engine)
        self.subs_text_full = self.__generate_text()
        self.subs_text_short = self.__generate_text(show_time_period=False)
        self.subs_text_array_full = self.subs_text_full.split('\n')
        self.subs_text_array_short = self.subs_text_short.split('\n')
        self.get_srt_table()
        self.load_dict_table()
        self.word_index = self.get_word_index()

    @timeit
    def get_srt_table(self):
        stemmer = Stemmer("english")
        raw_word_list = list(filter(lambda x: x, re.split("[^'a-zA-Z]+", str.lower(self.subs_text_short))))
        temp_dictionary = dict()
        for i in raw_word_list:
            if re.match("\w+'?\w+'?", i) and len(i) > 2:
                temp_dictionary[stemmer.stemWord(i)]['Amount'] = \
                    temp_dictionary.setdefault(stemmer.stemWord(i), {'Word': i, 'Amount': 0})['Amount'] + 1
                if temp_dictionary[stemmer.stemWord(i)] == i:
                    temp_dictionary[i]['Word'] = i
                self.stem_index.setdefault(stemmer.stemWord(i), set()).add(i)
        req = self.srt_table.insert()
        for i in sorted(temp_dictionary):
            req.execute({'Stem': i, 'Amount': temp_dictionary[i]['Amount'], 'Word': temp_dictionary[i]['Word']})
        return self.srt_table

    def get_word_index(self):
        line_index_text_only = 0
        line_index_including_timecodes = 0
        stemmer = Stemmer("english")
        word_index = dict()
        for srt_item in self.subs:
            line_index_including_timecodes += 1
            line_array = srt_item.text.split('\n')

            # print(len(line_array))
            for line in line_array:
                word_array = list(filter(lambda x: x, re.split("[^'a-zA-Z]+", line)))
                for word in word_array:
                    if re.match("\w+'?\w+'?", word) and len(word) > 2:
                        word_index.setdefault(stemmer.stemWord(word.lower()), []).append(
                            {'Word': word,
                             'Srt_item_index': srt_item.index,
                             'Line_index_text_only': line_index_text_only,
                             'Line_index_including_timecode': line_index_including_timecodes
                             })
                line_index_text_only += 1
                line_index_including_timecodes += 1
        return word_index
        # for item in sorted(stem_dictionary):
        #     print(item)
        #     for i in stem_dictionary[item]:
        #         print(i)

    @timeit
    def get_first_index(self, stem):
        return self.word_index[stem][0]['Line_index_including_timecode']

    def srt_query(self):
        stmt = select([self.srt_table]).select_from(self.srt_table).order_by(self.srt_table.c.Word)
        result = self.session.execute(stmt).fetchall()
        return result

    def dictionary_query(self):
        stmt = select([self.dictionary_table]).select_from(self.dictionary_table).order_by(self.dictionary_table.c.Word)
        result = self.session.execute(stmt).fetchall()
        return result

    @timeit
    def get_actual_table(self):
        stmt = select(self.srt_table.c.Word,
                      self.srt_table.c.Stem,
                      coalesce(self.dictionary_table.c.Translate, '').label('Translate'),
                      coalesce(self.dictionary_table.c.Meeting, 0).label('Meeting'),
                      coalesce(self.dictionary_table.c.Known, 0).label('Known'),
                      self.srt_table.c.Amount).select_from(
            self.srt_table.outerjoin(self.dictionary_table,
                                     self.srt_table.c.Stem == self.dictionary_table.c.Stem)).order_by(
            func.lower(self.srt_table.c.Word))
        result = self.session.execute(stmt).fetchall()
        return result

    @timeit
    def load_dict_table(self):
        dict_table_item = DictTableItem()
        self.dictionary_table = Table('Stems', self.metadata, autoload=True, autoload_with=dict_table_item.engine)
        self.dictionary_table.create(self.engine)
        self.session.execute(self.dictionary_table.insert(), dict_table_item.get_formatted_data())
        return self.dictionary_table

    @timeit
    def __generate_text(self, show_time_period=None):
        if show_time_period is None:
            show_time_period = True
        else:
            show_time_period = False
        text = ''
        for k in self.subs:
            if show_time_period:
                text += f'{k.start} --> {k.end}\n'
            text += f'{k.text}\n'
        return text

    def get_text(self, show_time_period=True):
        if show_time_period == True:
            return self.subs_text_full
        else:
            return self.subs_text_short

    def count_total_words(self):
        return self.session.scalar(func.sum(self.srt_table.c.Amount))

    def count_unique_words(self):
        return self.session.scalar(func.count(self.srt_table.c.Amount))


if __name__ == '__main__':
    # srt_table_item = SRTItem('Wrath.Of.Man.2021.HDRip.XviD.AC3-EVO.srt')
    srt_table_item = SRTItem('Carter.srt')
    # srt_table = srt_table_item.srt_table
    # for item in (srt_table_item.word_index['you']):
    #    print(item)
    # print(srt_table_item.get_first_index('retort'))
    # print(srt_table_item.subs_text_array_full[579])
    for r in (srt_table_item.get_actual_table()):
        if r.Stem == "agre":
            print(r)
    print(Stemmer("english").stemWord('agree'))
    # if r.Word == r.Stem:
    #     print(f"{r.Word} - {r.Translate} - ")
    # else:
    #     print(f"{r.Word}({r.Stem}) - {r.Translate}")

    # srt_table = GetSrtTable(engine, 'Carter.srt')
    # print(f'{i}: {r[i]}')

    # print(stmt)
    # for r in result:
    # print(dict(r))
    #    print(f"{r.word}")
    # print("")
    # print(f"Total words:{srt_table_item.count_total_words()}")
    # print(f"Unique words:{srt_table_item.count_unique_words()}")
    # print(srt_table_item.metadata.tables.keys())
    # print(srt_table_item.srt_table.c)
    # print(srt_table_item.dictionary_table.c)

    # for r in srt_table_item.dictionary_query():
    # for r in srt_table_item.get_actual_table():
    #     # print(dict(r))
    #     if r.Word == r.Stem:
    #         print(f"{r.Word} - {r.Translate} - {r.Amount}")
    #     else:
    #         print(f"{r.Word} ({r.Stem}) - {r.Translate} - {r.Amount}")

    # for i in srt_table_item.word_index.values():
    #    print(i)
