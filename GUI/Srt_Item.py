# Составляет таблицу из слов в субтитрах (Слово - количество)
import pysrt, re, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func
from Stemmer import Stemmer
from DictTable import DictTableItem


class SRTItem:
    def __init__(self, path):
        self.word_index = dict()
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
        self.get_srt_table()
        self.load_dict_table()

    def get_srt_table(self):
        stemmer = Stemmer("english")
        raw_word_list = list(filter(lambda x: x, re.split("[^'a-zA-Z]+", self.generate_text(False).lower())))
        temp_dictionary = dict()
        for i in raw_word_list:
            temp_dictionary[stemmer.stemWord(i)]['Amount'] = \
                temp_dictionary.setdefault(stemmer.stemWord(i), {'Word': i, 'Amount': 0})['Amount'] + 1
            if temp_dictionary[stemmer.stemWord(i)] == i:
                temp_dictionary[i]['Word'] = i
            self.word_index.setdefault(stemmer.stemWord(i), set()).add(i)
        req = self.srt_table.insert()
        for i in sorted(temp_dictionary):
            req.execute({'Stem': i, 'Amount': temp_dictionary[i]['Amount'], 'Word': temp_dictionary[i]['Word']})
        return self.srt_table

    def srt_query(self):
        stmt = select([self.srt_table]).select_from(self.srt_table).order_by(self.srt_table.c.Word)
        result = self.session.execute(stmt).fetchall()
        return result

    def dictionary_query(self):
        stmt = select([self.dictionary_table]).select_from(self.dictionary_table).order_by(self.dictionary_table.c.Word)
        result = self.session.execute(stmt).fetchall()
        return result

    def get_actual_table(self):
        stmt = select(self.dictionary_table.c.Word,
                      self.dictionary_table.c.Stem,
                      self.dictionary_table.c.Translate,
                      self.dictionary_table.c.Meeting,
                      self.dictionary_table.c.Known,
                      self.srt_table.c.Amount).select_from(
            self.srt_table.join(self.dictionary_table, self.dictionary_table.c.Stem == self.srt_table.c.Stem)).order_by(
            func.lower(self.dictionary_table.c.Word))
        result = self.session.execute(stmt).fetchall()
        return result

    def load_dict_table(self):
        dict_table_item = DictTableItem()
        self.dictionary_table = Table('Stems', self.metadata, autoload=True, autoload_with=dict_table_item.engine)
        self.dictionary_table.create(self.engine)
        for rec in dict_table_item.get_data():
            self.session.execute(self.dictionary_table.insert(rec))
        return self.dictionary_table

    def generate_text(self, showTimePeriod=None):
        if showTimePeriod is None:
            showTimePeriod = True
        else:
            showTimePeriod = False
        text = ''
        for k in self.subs:
            if showTimePeriod:
                text += f'{k.start} --> {k.end}\n'
            text += f'{k.text}\n'
        return text

    def count_total_words(self):
        return self.session.scalar(func.sum(self.srt_table.c.Amount))

    def count_unique_words(self):
        return self.session.scalar(func.count(self.srt_table.c.Amount))


if __name__ == '__main__':
    srt_table_item = SRTItem('Carter.srt')
    srt_table = srt_table_item.srt_table
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

    for i in srt_table_item.word_index.values():
        print(i)