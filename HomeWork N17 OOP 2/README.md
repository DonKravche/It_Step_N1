# Real Estate Management System

This project implements a simple real estate management system in Python, featuring `Person` and `House` classes to simulate property ownership and transactions.

## Features

- `Person` class to represent individuals with deposits and loans
- `House` class to represent properties with owners and status
- Property sale functionality, including cash and loan-based transactions

## Classes

### Person

Represents an individual with the following attributes:
- `name`: Person's name
- `deposit`: Current deposit amount (default: 1000)
- `loan`: Current loan amount (default: 0)

Methods:
- `__str__`: Returns a string representation of the person's information

### House

Represents a property with the following attributes:
- `ID`: Cadastral code of the property
- `price`: Price of the property
- `owner`: Owner of the property (Person object)
- `status`: Current status of the property (default: "გასაყიდი" [For Sale])

Methods:
- `sell_house(buyer, loan_amount=0)`: Handles the sale of the property

## Functionality

1. Create `Person` objects for owners and buyers
2. Create `House` objects with initial owners
3. Simulate property sales:
   - Cash transaction: Only buyer is provided as an argument
   - Loan-based transaction: Buyer and loan amount are provided as arguments

## Usage

1. Create `Person` objects for the owner and potential buyers
2. Create a `House` object with an initial owner
3. Use the `sell_house` method to simulate property sales:
   - For cash transactions: `house.sell_house(buyer)`
   - For loan-based transactions: `house.sell_house(buyer, loan_amount)`

## Example

```python
owner = Person("გიორგი", 5000)
buyer1 = Person("ანა", 120000)
buyer2 = Person("ნიკა", 50000)
house = House("12345", 100000, owner)

# Cash transaction
result1 = house.sell_house(buyer1)

# Loan-based transaction
result2 = house.sell_house(buyer2, 60000)

print(result1)
print(result2)
```

This system allows for basic real estate transactions, including cash and loan-based sales, while tracking the financial status of individuals and property ownership.