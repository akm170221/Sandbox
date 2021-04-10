"""Victor"""

def main():
    name = input("Name? ")
    age = input("Age? ")
    print("Your name is {} and age is {}". format(name, age))
    if is_adult(age):
        print("You are an adult")
    else:
        print("You are a child")

def is_adult(age):
    return age >=21

main()