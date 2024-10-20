from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:shHZB4bL@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind=engine)


# Models
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity_in_stock = Column(Integer)


class CartItem(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    product = relationship("Product")


Base.metadata.create_all(engine)


# Helper functions
def add_products():
    session = Session()
    products = [
        Product(name="ლეპტოპი", price=1999.99, quantity_in_stock=10),
        Product(name="სმარტფონი", price=799.99, quantity_in_stock=20),
        Product(name="ყურსასმენები", price=199.99, quantity_in_stock=50),
        Product(name="პლანშეტი", price=499.99, quantity_in_stock=15),
        Product(name="სმარტ საათი", price=299.99, quantity_in_stock=30)
    ]
    session.add_all(products)
    session.commit()
    session.close()


def view_products():
    session = Session()
    products = session.query(Product).all()
    print("\nხელმისაწვდომი პროდუქტები:")
    for product in products:
        print(f"{product.id}. {product.name} - ფასი: {product.price:.2f}₾, მარაგშია: {product.quantity_in_stock}")
    session.close()


def view_cart():
    session = Session()
    cart_items = session.query(CartItem).all()
    if not cart_items:
        print("თქვენი კალათა ცარიელია.")
    else:
        total = 0
        print("კალათის შიგთავსი:")
        for item in cart_items:
            subtotal = item.quantity * item.product.price
            total += subtotal
            print(
                f"{item.product.name} - რაოდენობა: {item.quantity}, ფასი: {item.product.price:.2f}₾, ჯამი: {subtotal:.2f}₾")
        print(f"ჯამური ღირებულება: {total:.2f}₾")
    session.close()


def add_to_cart():
    view_products()
    session = Session()
    product_id = int(input("შეიყვანეთ პროდუქტის ID კალათაში დასამატებლად: "))
    quantity = int(input("შეიყვანეთ რაოდენობა: "))

    product = session.query(Product).get(product_id)
    if product and product.quantity_in_stock >= quantity:
        cart_item = CartItem(product_id=product_id, quantity=quantity)
        session.add(cart_item)
        product.quantity_in_stock -= quantity
        session.commit()
        print("პროდუქტი წარმატებით დაემატა კალათაში.")
    else:
        print("პროდუქტი ვერ მოიძებნა ან არასაკმარისი რაოდენობაა მარაგში.")
    session.close()


def clear_cart():
    session = Session()
    session.query(CartItem).delete()
    session.commit()
    print("კალათა გასუფთავდა.")
    session.close()


def main():
    add_products()

    while True:
        print("\nაირჩიეთ მოქმედება:")
        print("1. პროდუქტების ნახვა")
        print("2. კალათის ნახვა")
        print("3. პროდუქტის დამატება კალათაში")
        print("4. კალათის გასუფთავება")
        print("0. გამოსვლა")

        choice = input("შეიყვანეთ თქვენი არჩევანი: ")

        if choice == '1':
            view_products()
        elif choice == '2':
            view_cart()
        elif choice == '3':
            add_to_cart()
        elif choice == '4':
            clear_cart()
        elif choice == '0':
            break
        else:
            print("არასწორი არჩევანი. გთხოვთ სცადოთ ხელახლა.")


if __name__ == "__main__":
    main()