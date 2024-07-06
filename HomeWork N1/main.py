# 1

a = int(input("შეიყვანეთ პირველი რიცხვი: "))
b = int(input("შეიყვანეთ მეორე რიცხვი: "))
c = int(input("შეიყვანეთ მესამე რიცხვი: "))

sum = a + b + c
print("სამი რიცხვის ჯამი არის:", sum)

# 2

a = int(input("შეიყვანეთ კუბის გვერდის სიგრძე: "))

v = a ** 3
s = 6 * (a ** 2)

print("კუბის მოცულობაა:", v)
print("კუბის ზედაპირის ფართობია:", s)


# 3

monitor_price = float(input("შეიყვანეთ მონიტორის ფასი: "))
system_price = float(input("შეიყვანეთ სისტემური ბლოკის ფასი: "))
keyboard_price = float(input("შეიყვანეთ კლავიატურის ფასი: "))
mouse_price = float(input("შეიყვანეთ მაუსის ფასი: "))

total_price = monitor_price + system_price + keyboard_price + mouse_price

print("კომპიუტერის საერთო ფასია:", total_price)