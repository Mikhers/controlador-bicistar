from sqlalchemy import create_engine, MetaData


engine = create_engine("mysql+pymysql://mikhers:Kjkszpj21308182@localhost:3306/bicistar")

meta_data = MetaData()