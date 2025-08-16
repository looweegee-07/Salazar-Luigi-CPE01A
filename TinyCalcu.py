def main() -> None:
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))

    result = a + b, a - b, a * b, a / b, a // b, a % b, a ** b
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    print("Division =", a / b)
    print("Integer division =", a // b)
    print("Remainder =", a % b)
    print("Exponent =", a ** b)

    result = 0
    result += a
    result *= b
    result -= 1
    print("Final =",result)

    word = input("Enter word: ")
    print(f"The word has {(n := len(word))} characters ")




if __name__ == '__main__': main()