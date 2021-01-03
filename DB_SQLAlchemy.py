from sqlalchemy import create_engine


# Stem	Word	Known	Meeting	Translate	Study	Language


def getData(path):
    engine = create_engine('sqlite:///' + path)
    result = engine.execute('SELECT * FROM STEMS ORDER BY WORD')
    a = result.fetchall()
    result.close()
    return a


if __name__ == '__main__' or __name__ == 'Test':
    for r in getData('Vocabulary.db'):
        print(dict(r))
        if r.Word == r.Stem:
            print(f"{r.Word} - {r.Translate}")
        else:
            print(f"{r.Word}({r.Stem}) - {r.Translate}")
