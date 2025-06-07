from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://root@cockroach:26257/defaultdb?sslmode=disable"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

predictions = Table(
    'predictions', metadata,
    Column('id', Integer, primary_key=True),
    Column('label', String)
)

metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_prediction(label):
    session = Session()
    session.execute(predictions.insert().values(label=str(label)))
    session.commit()
    session.close()