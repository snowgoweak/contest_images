import sqlalchemy as sa

metadata = sa.MetaData()

engine = sa.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

