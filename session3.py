# Define the function f(x)
def f(x):
    return x ** 3 + 8


def main():
    # Call the function f(x) with x = 9
    x = 9
    result = f(x)

    print(f"f({x}) = {result}")

    if result > 27:
        print("YAY!")


if __name__ == "__main__":
    main()
