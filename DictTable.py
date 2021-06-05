from sqlalchemy import create_engine, Table, MetaData, select
from sqlalchemy.orm import sessionmaker


# Stem	Word	Known	Meeting	Translate	Study	Language

class DictTableItem:
    def __init__(self):
        self.engine = create_engine('sqlite:///Vocabulary.db')
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()
        self.metadata = MetaData(self.engine)
        self.stems = Table('Stems', self.metadata, autoload=True, autoload_with=self.engine)

    def get_data(self):
        stmt = select([self.stems]).select_from(self.stems).order_by(self.stems.c.Word)
        result = self.session.execute(stmt).fetchall()
        return result


if __name__ == '__main__' or __name__ == 'Test':
    dict_table_item = DictTableItem()
    for r in dict_table_item.get_data():
        print(dict(r))
        if r.Word == r.Stem:
            print(f"{r.Word} - {r.Translate}")
        else:
            print(f"{r.Word}({r.Stem}) - {r.Translate}")
