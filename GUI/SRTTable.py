# Составляет таблицу из слов в субтитрах (Слово - количество)
import pysrt, re, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func
from Stemmer import Stemmer


class SRTTableItem:
    def __init__(self, path):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()
        self.metadata = MetaData(self.engine)
        self.srt_table = Table('words', self.metadata,
                               Column('stem', String, primary_key=True),
                               Column('Word', String),
                               Column('Amount', Integer),
                               )
        self.metadata.create_all(self.engine)
        self.get_srt_table(path)

    def get_srt_table(self, path):
        stemmer = Stemmer("english")
        subs = pysrt.open(path)
        raw_word_list = list(filter(lambda x: x, re.split('[^\'a-zA-Z]+', subs.text.lower())))
        # print(results)
        dictionary = dict()
        for i in raw_word_list:
            dictionary[stemmer.stemWord(i)]['Amount'] = \
                dictionary.setdefault(stemmer.stemWord(i), {'Word': i, 'Amount': 0})['Amount'] + 1
            if dictionary[stemmer.stemWord(i)] == i:
                dictionary[i]['Word'] = i
        print(dictionary)
        req = self.srt_table.insert()
        for i in sorted(dictionary):
            req.execute({'stem': i, 'Amount': dictionary[i]['Amount'], 'Word': dictionary[i]['Word']})
        return self.srt_table

    def get_data(self):
        stmt = select([self.srt_table]).select_from(self.srt_table).order_by(self.srt_table.c.Word)
        result = self.session.execute(stmt).fetchall()
        return result


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
