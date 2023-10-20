import math


def main():
    num_entries = 1000
    start_x = 0
    end_x = 2 * math.pi

    step_size = (end_x - start_x) / (num_entries - 1)

    print("x\t\t sin(x)")

    # Generate and print the table
    x = start_x
    for _ in range(num_entries):
        sin_x = math.sin(x)
        print(f"{x:.4f}\t\t {sin_x:.4f}")
        x += step_size


if __name__ == "__main__":
    main()
