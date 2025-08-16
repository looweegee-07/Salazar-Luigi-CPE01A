def main() -> None:
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "). strip())
    height = float(input("Enter your height in meters:"). strip())
    weight = float(input("Enter your weight in kilograms:"). strip())
    next_age =  age + 1
    greetings = "Hello, " + name + "!"

    print(greetings)
    print("-" * len(greetings))
    print(f"Your name has {(n := len(name))} characters ") # tempting ibahin yung n sa ibang words since wala naman value ( ° ͜ʖ °)
    print("Next year you will", next_age, "years old.")
    print("Height:", height, "m", "Weight:", weight, "kg")


if __name__ == '__main__': main()