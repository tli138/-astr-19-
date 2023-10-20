class Dog:
    def __init__(self, arm_length: float, leg_length: float, num_eyes: int, has_tail: bool, is_furry: bool):
        self.arm_length: float = arm_length
        self.leg_length: float = leg_length
        self.num_eyes: int = num_eyes
        self.has_tail: bool = has_tail
        self.is_furry: bool = is_furry

    def describe_and_print(self):
        print("Physical Characteristics of Dog:")
        print(f"Arm Length: {self.arm_length} units")
        print(f"Leg Length: {self.leg_length} units")
        print(f"Number of Eyes: {self.num_eyes}")
        if self.has_tail:
            print("Has a Tail: Yes")
        else:
            print("Has a Tail: No")
        if self.is_furry:
            print("Is Furry: Yes")
        else:
            print("Is Furry: No")


def main():
    my_favorite_animal = Dog(99.5, 50.0, 2, True, True)

    my_favorite_animal.describe_and_print()


if __name__ == "__main__":
    main()
