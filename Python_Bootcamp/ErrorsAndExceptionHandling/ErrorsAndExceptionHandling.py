try:
    a = int(input("Enter an integer\n"))
    b = int(input("Enter another integer\n"))
    c = a / b
except:
    print("An exception has occurred ")
else:
    print(f'c is {c}')
finally:
    print("well done you did great")
