import pysrt, re, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func


def printFormatted(item):
    print(f'{item.start} --> {item.end}')
    print(item.text)

class Word(object):
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __repr__(self):
        return f"{self.word}: {self.count}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:', echo=True)
    metadata = MetaData(engine)
    srt_table = Table('words', metadata,
                      Column('word', String, primary_key=True),
                      Column('count', Integer),
                      )
    metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    subs = pysrt.open('Carter.srt')

    results = list(filter(lambda x: x, re.split('[^\'a-zA-Z-]+', subs.text.lower())))
    #print(results)
    r = dict()
    for i in results:
        if re.search('[a-zA-Z]', i):
            r[i] = r.setdefault(i, 0) + 1

    req = srt_table.insert()
    for i in sorted(r):
        for j in set(sorted(r.values())):
            if r[i] == j:
                req.execute({'word': i, 'count': r[i]})
                #print(f'{i}: {r[i]}')

    total_words = len(results)
    unique_words = len(r)

    print(f"Total words:{len(results)}")
    print(f"Unique words:{len(r)}")
    print("")

    stmt = select([srt_table]).select_from(srt_table).where(func.length(srt_table.c.word)<=2).order_by(srt_table.c.word)
    print(stmt)
    result = engine.execute(stmt).fetchall()

    for r in result:
        # print(dict(r))
        print(f"{r.word}")