class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f'Person name: {self.name} have amount of {self.deposit} deposit, and loan is: {self.loan}'


class House:
    def __init__(self, ID, price, owner):
        self.id = ID
        self.price = price
        self.owner = owner
        self.status = 'available'

    def sell_house(self, buyer, loan_amount=0):
        if buyer.deposit + loan_amount >= self.price:
            self.owner.deposit += self.price

            if loan_amount > 0:
                buyer.deposit -= (self.price - loan_amount)
                buyer.loan += loan_amount
                self.status = 'გაყიდული სესხით'
            else:
                buyer.deposit -= self.price
                self.status = 'გაყიდული'

            old_owner = self.owner
            self.owner = buyer

            if loan_amount > 0:
                return f"ბინა გაიყიდა სესხით! ახალი მფლობელია {buyer.name}. \n" \
                       f"{old_owner.name}-ს დეპოზიტი გაიზარდა {self.price}-ით. \n" \
                       f"{buyer.name}-ს დეპოზიტი შემცირდა {self.price - loan_amount}-ით და სესხი გაიზარდა {loan_amount}-ით."
            else:
                return f"ბინა გაიყიდა! ახალი მფლობელია {buyer.name}. \n" \
                       f"{old_owner.name}-ს დეპოზიტი გაიზარდა {self.price}-ით. \n" \
                       f"{buyer.name}-ს დეპოზიტი შემცირდა {self.price}-ით."
        else:
            return f"{buyer.name}-ს არ აქვს საკმარისი თანხა ბინის შესაძენად."


owner = Person("გიორგი", 5000)
buyer1 = Person("ანა", 120000)
buyer2 = Person("ნიკა", 50000)
house = House("12345", 100000, owner)

print("საწყისი მდგომარეობა:")
print(owner)
print(buyer1)
print(buyer2)
print(f"House: ID={house.id}, Price={house.price}, Owner={house.owner.name}, Status={house.status}")

print("\nგაყიდვა ნაღდი ანგარიშსწორებით:")
result1 = house.sell_house(buyer1)
print(result1)
print(owner)
print(buyer1)
print(f"House: ID={house.id}, Price={house.price}, Owner={house.owner.name}, Status={house.status}")


house.owner = owner
house.status = 'გასაყიდი'
owner.deposit = 5000
buyer2.deposit = 50000

print("\nგაყიდვა სესხით:")
result2 = house.sell_house(buyer2, 60000)
print(result2)
print(owner)
print(buyer2)
print(f"House: ID={house.id}, Price={house.price}, Owner={house.owner.name}, Status={house.status}")
