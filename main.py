import sqlalchemy
from sqlalchemy.orm import sessionmaker

from create_tables import create_tables, Publisher, Book, Shop, Stock, Sale
from insert_data import insert_data
from book_sales import get_book_sales

DSN = 'postgresql://postgres:12345678@localhost:5432/books_db'
engine = sqlalchemy.create_engine(DSN)

# create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# insert_data(session)

if __name__ == '__main__':
    create_tables(engine)
    insert_data(session)
    get_book_sales(session)



    session.close()