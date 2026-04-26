# Passwords Generator

A small Python script that generates random passwords and saves them to a `passwords.txt` file.

## What the project does

- asks the user how many passwords to generate;
- generates the requested number of random passwords;
- chooses a random length for each password between 8 and 14 characters;
- saves the result to `passwords.txt`.

By default, generated passwords may include:

- lowercase letters;
- uppercase letters;
- digits;
- special characters.

## Project structure

- [passwords_generator.py](./passwords_generator.py) - main script;
- `passwords.txt` - output file created after running the program.

## Requirements

- Python 3.8+.

No external dependencies are required. The script uses only the standard `random` and `string` modules.

## Run

From the project root:

```bash
python passwords_generator.py
```

After launch, the program asks for the number of passwords to generate.

Example:

```text
Enter the number of passwords to generate: 5
5 passwords were successfully written to passwords.txt.
```

## How generation works

The `generate_password(...)` function:

- receives the password length;
- builds the allowed character set;
- generates a random password;
- retries until the password passes the built-in checks.
