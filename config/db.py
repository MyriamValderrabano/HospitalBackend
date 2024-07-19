from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_G5sGwfrbPtZVPUhHUS2@mysql-base-hospital-hospital-base.h.aivencloud.com:19854/defaultdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()