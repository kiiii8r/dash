# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime
import os

# 各種DBについて記載 data.dbという名前で格納 (絶対パスで表現されるよう指定)
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')
# どのDBを用いるか。 echo=pythonでのDB操作でsql文を出力するか
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True , echo=True)
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
