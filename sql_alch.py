from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///employee.db', echo=True)
meta = MetaData()

emp = Table('employees', meta,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('last_name', String))
#
#
# meta.create_all(engine)
#
# ins = emp.insert()
#
# ins2 = emp.insert().values(name='Saurav', last_name='Kumar')
#
# conn = engine.connect()
# result = conn.execute(ins2)
#
# conn.execute(emp.insert(), [
#     {'name': 'Saurav', 'last_name': 'Soni'},
#     {'name': 'S.', 'last_name': 'Soni'},
#     {'name': 'Nan', 'last_name': 'Paul'}
#])

s = emp.select()
conn = engine.connect()
result =  conn.execute(s)

for row in result:
    print(row)

