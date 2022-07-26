from sqlalchemy import Table, Column, Integer, String, create_engine, MetaData
engine = create_engine('sqlite:///employee.db', echo=True)
meta = MetaData()


