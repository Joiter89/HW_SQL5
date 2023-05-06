import sqlalchemy 
from sqlalchemy.orm import sessionmaker
from create_tables import create_tables, Publisher, Book, Shop, Stock, Sale

def get_book_sales(session):
    publisher_info = input('Введите имя или идентификатор издателя (publisher): ')
    q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale
                      ).select_from(Stock).\
        join(Shop).\
        join(Book).\
        join(Publisher).\
        join(Sale)
    if publisher_info.isdigit():
        q = q.filter(Publisher.id == publisher_info).all()
    else:
        q = q.filter(Publisher.name == publisher_info).all() 
    l = []  
    m = []     
    for a, b, c, d in q:
        l.append(len(a))
        m.append(len(b))
    x = max(l)
    y = max(m)    
    for a, b, c, d in q: 
        print(f'{a.ljust(x)}  |  {b.ljust(y)}  |  {c}  |  {d.strftime("%d-%m-%Y")}')

    session.commit()    
