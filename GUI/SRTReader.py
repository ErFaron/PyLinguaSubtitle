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
        self.metadata = MetaData(self.engine)
        self.srt_table = Table('words', self.metadata,
                               Column('stem', String, primary_key=True),
                               Column('word', String),
                               Column('amount', Integer),
                               )
        self.metadata.create_all(self.engine)
        self.get_srt_table(path)

    def get_srt_table(self, path):
        stemmer = Stemmer("english")
        subs = pysrt.open(path)
        results = list(filter(lambda x: x, re.split('[^\'a-zA-Z]+', subs.text.lower())))
        # print(results)
        r = dict()
        for i in results:
            r[stemmer.stemWord(i)] = r.setdefault(stemmer.stemWord(i), {'word': i, 'amount': 0})
            r[stemmer.stemWord(i)]['amount'] = r[stemmer.stemWord(i)]['amount'] + 1
        print(r)

        req = self.srt_table.insert()
        for i in sorted(r):
            req.execute({'stem': i, 'amount': r[i]['amount'], 'word': r[i]['word']})
        return self.srt_table


if __name__ == '__main__':
    srt_table_item = SRTTableItem('Carter.srt')
    srt_table = srt_table_item.srt_table
    # srt_table = GetSrtTable(engine, 'Carter.srt')
    # print(f'{i}: {r[i]}')

    total_words = srt_table_item.engine.scalar(func.sum(srt_table.c.amount))
    unique_words = srt_table_item.engine.scalar(func.count(srt_table))
    # print(stmt)
    stmt = select([srt_table]).select_from(srt_table).order_by(srt_table.c.word)
    result = srt_table_item.engine.execute(stmt).fetchall()

    # for r in result:
    # print(dict(r))
    #    print(f"{r.word}")
    print("")
    print(f"Total words:{total_words}")
    print(f"Unique words:{unique_words}")
