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

## Current limitations

- passwords are generated with `random` instead of `secrets`;
- the `use_uppercase`, `use_digits`, and `use_special` arguments exist, but the final validation currently still expects all character groups;
- the special-character set used for generation does not fully match the one used for validation;
- password length cannot be configured by the user;
- the output file is always overwritten;
- Russian console messages in the script currently have encoding issues.

## What can be improved

1. Replace `random` with `secrets` for stronger password generation.
2. Fix the validation logic so it respects the `use_uppercase`, `use_digits`, and `use_special` flags.
3. Use the same special-character set in both generation and validation.
4. Fix the encoding of Russian console messages.
5. Add command-line arguments for:
   - password count;
   - password length;
   - enabling or disabling character groups;
   - output file name.
6. Add validation for impossible configurations, such as an empty character set.
7. Add tests for core scenarios:
   - correct password length;
   - required character presence;
   - invalid input handling;
   - multiple password generation.
8. Add a `.gitignore` file so `passwords.txt` is not committed accidentally.
9. Support additional output formats such as `txt`, `csv`, or `json`.
10. Add a non-interactive mode so the script can be used in automation.

## Possible next step

If you continue developing this project, it could become a small CLI utility, for example:

```bash
python passwords_generator.py --count 10 --length 16 --no-special --output my_passwords.txt
```

That would make the script much more convenient both for manual use and for automation.
