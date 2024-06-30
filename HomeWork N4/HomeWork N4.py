# 1
user_input = str(input("Enter name: "))
palindrome = user_input[::-1]

if palindrome == user_input:
    print("This Word is Palindrome")
else:
    print("This Word is not Palindrome")


# 2
def Ascii():
    user_input2 = input("Please Enter txt: ")
    for char in user_input2:
        print(f"Character: {char}, ASCII: {ord(char)}")


Ascii()
