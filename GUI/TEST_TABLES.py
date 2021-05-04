# Составляет таблицу из слов в субтитрах (Слово - количество)
import re, sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func
from Stemmer import Stemmer

from DictTable import DictTableItem
from SRTTable import SRTTableItem

if __name__ == '__main__':
    srt_table_item = SRTTableItem('Carter.srt')
    dict_table_item = DictTableItem()
    srt_table_item.dictionary_table = Table('Stems', srt_table_item.metadata, autoload=True,
                                            autoload_with=dict_table_item.engine)
    srt_table_item.dictionary_table.create(srt_table_item.engine)
    print(srt_table_item.metadata.tables.keys())
    print(srt_table_item.dictionary_query())

    for r in dict_table_item.get_data():
        srt_table_item.session.execute(srt_table_item.dictionary_table.insert(r))

    # print(srt_table_item.dictionary_query())
    print(srt_table_item.metadata.tables.keys())
    print(srt_table_item.dictionary_table.c)
