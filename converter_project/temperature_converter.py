import sys
    
def celsius_to_fahrenheit(n):
    answer = (n * 9/5) + 32
    return round(answer, 2)

def fahrenheit_to_celsius(n):
    answer = (n - 32) * 5/9
    return round(answer, 2)

def main():
    while True:
        choice = input("\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Exit\n\nChoice: ")
        if choice == "1":
            value = input("Value to convert: ")
            print(f"{celsius_to_fahrenheit(int(value))} °F")
        elif choice == "2":
            value = input("Value to convert: ")
            print(f"{fahrenheit_to_celsius(int(value))} °C")
        elif choice == "3":
            sys.exit()
        else:
            print("\nPlease input a valid choice")


if __name__ == "__main__":
    main()