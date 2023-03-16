from sqlalchemy import create_engine, MetaData


engine = create_engine("mysql+pymysql://fastAPI:21308182:localhost:3306/bicistar")

conn = engine.connect()

meta_data = MetaData()