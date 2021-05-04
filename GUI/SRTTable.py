# Составляет таблицу из слов в субтитрах (Слово - количество)
import pysrt, re, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func
from Stemmer import Stemmer
from DictTable import DictTableItem


class SRTTableItem:
    def __init__(self, path):
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
        self.get_srt_table(path)
        self.load_dict_table()

    def get_srt_table(self, path):
        stemmer = Stemmer("english")
        subs = pysrt.open(path)
        raw_word_list = list(filter(lambda x: x, re.split('[^\'a-zA-Z]+', subs.text.lower())))
        # print(results)
        temp_dictionary = dict()
        for i in raw_word_list:
            temp_dictionary[stemmer.stemWord(i)]['Amount'] = \
                temp_dictionary.setdefault(stemmer.stemWord(i), {'Word': i, 'Amount': 0})['Amount'] + 1
            if temp_dictionary[stemmer.stemWord(i)] == i:
                temp_dictionary[i]['Word'] = i
        req = self.srt_table.insert()
        for i in sorted(temp_dictionary):
            req.execute({'Stem': i, 'Amount': temp_dictionary[i]['Amount'], 'Word': temp_dictionary[i]['Word']})
        return self.srt_table

    def srt_query(self):
        stmt = select([self.srt_table]).select_from(self.srt_table).order_by(self.srt_table.c.Word)
        result = self.session.execute(stmt).fetchall()
        return result

    def dictionary_query(self):
        stmt = select([self.dictionary_table]).select_from(self.dictionary_table).order_by(self.dictionary_table.c.Stem)
        result = self.session.execute(stmt).fetchall()
        return result

    def load_dict_table(self):
        dict_table_item = DictTableItem()
        self.dictionary_table = Table('Stems', self.metadata, autoload=True, autoload_with=dict_table_item.engine)
        self.dictionary_table.create(self.engine)
        return self.dictionary_table


if __name__ == '__main__':
    srt_table_item = SRTTableItem('Carter.srt')
    srt_table = srt_table_item.srt_table
    # srt_table = GetSrtTable(engine, 'Carter.srt')
    # print(f'{i}: {r[i]}')

    total_words = srt_table_item.session.scalar(func.sum(srt_table.c.Amount))
    unique_words = srt_table_item.session.scalar(func.count(srt_table))
    # print(stmt)
    # for r in result:
    # print(dict(r))
    #    print(f"{r.word}")
    print("")
    print(f"Total words:{total_words}")
    print(f"Unique words:{unique_words}")
    print(srt_table_item.metadata.tables.keys())
    print(srt_table_item.srt_table.c)
    print(srt_table_item.dictionary_table.c)
