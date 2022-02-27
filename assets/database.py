# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime
import os
import pandas as pd

# 各種DBについて記載 data.dbという名前で格納 (絶対パスで表現されるよう指定)
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')
# どのDBを用いるか。 echo=pythonでのDB操作でsql文を出力するか
engine = create_engine(os.environ.get('DATABASE_URL') or 'sqlite:///' + databese_file, convert_unicode=True , echo=True)
db_session = scoped_session(
                sessionmaker(
                    autocommit = False, # 自動コミット
                    autoflush = False, #自動反映
                    bind = engine
                )
             )
Base = declarative_base()
Base.query = db_session.query_property()

# DBの初期化
def init_db():
    import assets.models
    Base.metadata.create_all(bind=engine)

def read_data():
    from assets import models
    df = pd.read_csv('assets/data.csv')
    for index, _df in df.iterrows():
        # date型への変更
        date = datetime.datetime.strptime(_df['date'], '%Y/%m/%d').date()
        row = models.Data(date=date, subscribers=_df['subscribers'], reviews=_df['reviews'])
        db_session.add(row)
    db_session.commit()
