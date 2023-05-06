import sqlalchemy
from create_tables import create_tables, Publisher, Book, Shop, Stock, Sale

def insert_data(session):
    publisher1 = Publisher(name='Фицджеральд')
    publisher2 = Publisher(name='Ремарк')
    publisher3 = Publisher(name='Шекспир')

    session.add_all([publisher1, publisher2, publisher3])

    book1 = Book(title='Великий Гэтсби', publisher=publisher1)
    book2 = Book(title='На Западном фронте без перемен', publisher=publisher2)
    book3 = Book(title='Король Лир', publisher=publisher3)

    session.add_all([book1, book2, book3])

    shop1 = Shop(name='Читай-город')
    shop2 = Shop(name='Книжный лабиринт')
    shop3 = Shop(name='Дом книги')

    session.add_all([shop1, shop2, shop3])

    stock1 = Stock(book=book1, shop=shop1, count=72)
    stock2 = Stock(book=book1, shop=shop2, count=87)
    stock3 = Stock(book=book1, shop=shop3, count=69)
    stock4 = Stock(book=book2, shop=shop1, count=94)
    stock5 = Stock(book=book2, shop=shop2, count=110)
    stock6 = Stock(book=book2, shop=shop3, count=102)
    stock7 = Stock(book=book3, shop=shop1, count=48)
    stock8 = Stock(book=book3, shop=shop2, count=30)
    stock9 = Stock(book=book3, shop=shop3, count=55)

    session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9])

    sale1 = Sale(price=750, date_sale='10.01.2023', stock=stock1, count=19)
    sale2 = Sale(price=780, date_sale='11.01.2023', stock=stock2, count=12)
    sale3 = Sale(price=730, date_sale='12.01.2023', stock=stock3, count=22)
    sale4 = Sale(price=820, date_sale='13.01.2023', stock=stock4, count=8)
    sale5 = Sale(price=850, date_sale='14.01.2023', stock=stock5, count=26)
    sale6 = Sale(price=870, date_sale='15.01.2023', stock=stock6, count=34)
    sale7 = Sale(price=650, date_sale='16.01.2023', stock=stock7, count=8)
    sale8 = Sale(price=615, date_sale='17.01.2023', stock=stock8, count=11)
    sale9 = Sale(price=690, date_sale='18.01.2023', stock=stock9, count=6)

    session.add_all([sale1, sale2, sale3, sale4, sale5, sale6,sale7,sale8,sale9])


    session.commit()

