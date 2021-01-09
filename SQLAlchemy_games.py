from sqlalchemy import create_engine, MetaData, select, asc
from sqlalchemy.schema import Table
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker


# Stem	Word	Known	Meeting	Translate	Study	Language


def getData(path):
    some_engine = create_engine('sqlite:///' + path)
    metadata = MetaData()
    p_s = Table('stems', metadata, autoload_with=some_engine)

    stmt = select([p_s]).select_from(p_s).order_by(p_s.c.Word)
    print(stmt)
    result = some_engine.execute(stmt).fetchall()
    # print(stemsi)
    # print(result)
    return result


if __name__ == '__main__' or __name__ == 'Test':
    # print(getData('Vocabulary.db'))

    # for r in getData('Vocabulary.db'):
    #     # print(dict(r))
    #     if r.Translate:
    #         if r.Word == r.stem:
    #             print(f"{r.Word} - {r.Translate}")
    #         else:
    #             print(f"{r.Word} ({r.stem}) - {r.Translate}")
    #     else:
    #         if r.Known==0:
    #             print(f"{r.Word} ({r.stem}) - ?")
    s = 0
    for r in getData('Vocabulary.db'):
        # print(dict(r))
        if not r.Translate:
            if not r.Known:
                s = s + 1
                if r.Word == r.stem:
                    print(f"{r.Word} - {r.Translate}")
                else:
                    print(f"{r.Word} ({r.stem}) - {r.Translate}")
    print(s)
