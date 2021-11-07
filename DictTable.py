from sqlalchemy import create_engine, Table, MetaData, select, func
from sqlalchemy.orm import sessionmaker
from timeit import timeit


# Stem	Word	Known	Meeting	Translate	Study	Language

class DictTableItem:
    def __init__(self):
        self.engine = create_engine('sqlite:///Vocabulary.db')
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()
        self.metadata = MetaData(self.engine)
        self.stems = Table('Stems', self.metadata, autoload=True, autoload_with=self.engine)

    # @timeit
    def __get_raw_data(self):
        stmt = select([self.stems]).select_from(self.stems).order_by(self.stems.c.Word)
        result = self.session.execute(stmt).fetchall()
        return result

    def get_formatted_data(self):
        result = []
        for r in self.__get_raw_data():
            result.append(dict(r))
        self.session.close()
        return result

    def update_db(self, data):
        for r in data:
            stmt = (
                f'REPLACE INTO {self.stems.name}(Stem,Word,Known,Meeting,Translate,Study,Language) VALUES("{r["Stem"]}","{r["Word"]}",{r["Known"]},{r["Meeting"] + 1},"{r["Translate"]}",0,"english")')
            self.session.execute(stmt)
        self.session.commit()
        self.session.close()


if __name__ == '__main__' or __name__ == 'Test':
    dict_table_item = DictTableItem()
    for i in dict_table_item.get_formatted_data():
        if i['Stem'] == 'zoom': print(i)
    dict_table_item.update_db([{'Stem': 'zoom', 'Word': 'zoom', 'Translate': '', 'Language': 'english', 'Known': 1,
                                'Meeting': 2, 'Study': 0}])
    dict_table_item.session.commit()
    print('')
    for i in dict_table_item.get_formatted_data():
        if i['Stem'] == 'zoom': print(i)
    # dict_table_item.update_db()
    # for r in dict_table_item.get_data():
    #    print(dict(r))
    # if r.Word == r.Stem:
    #    print(f"{r.Word} - {r.Translate}")
    # else:
    #    print(f"{r.Word}({r.Stem}) - {r.Translate}")
