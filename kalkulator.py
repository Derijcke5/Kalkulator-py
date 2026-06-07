print(" KALKULATOR")

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("Wybierz działanie:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

choice = input("Twój wybór: ")

if choice == "1":
    print("Wynik:", a + b)
elif choice == "2":
    print("Wynik:", a - b)
elif choice == "3":
    print("Wynik:", a * b)
elif choice == "4":
    if b != 0:
        print("Wynik:", a / b)
    else:
        print("Nie można dzielić przez zero!")
else:
    print("Błędny wybór")
