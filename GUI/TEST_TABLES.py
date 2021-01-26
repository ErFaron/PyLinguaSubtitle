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
    engine = create_engine('sqlite:///:memory:', echo=True)
    Session = sessionmaker(engine)
    session = Session()
    srt_table = srt_table_item.srt_table
    dict_table = dict_table_item.stems
    stmt = select([srt_table]).select_from(srt_table).order_by(srt_table.c.Word)
    result = session.execute(stmt).fetchall()
    print(result)
