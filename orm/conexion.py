from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:49P54ty8.@localhost/slangs_orm')
Sesion = sessionmaker(bind=engine)

Base = declarative_base()



