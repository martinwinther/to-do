try:
    totalValue = int(input("Enter total value: "))
    value = int(input("Enter value: "))

    print(f"That is {value / totalValue * 100}%")
except ValueError:
    print("You need to enter a number. Run the program again.")

except ZeroDivisionError:
    print("Your total value cannot be zero")
