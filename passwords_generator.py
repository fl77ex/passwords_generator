import random
import string


def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%*()_"

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    while True:
        password = "".join(random.choice(characters) for _ in range(length))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in "!@#$%*()_-+=" for c in password)
        ):
            return password


def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords < 1:
            raise ValueError("The number of passwords must be greater than zero.")

        with open("passwords.txt", "w") as file:
            for _ in range(num_passwords):
                length = random.randint(8, 14)
                password = generate_password(
                    length,
                    use_uppercase=True,
                    use_digits=True,
                    use_special=True,
                )
                file.write(password + "\n")

        print(f"{num_passwords} passwords were successfully written to passwords.txt.")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
