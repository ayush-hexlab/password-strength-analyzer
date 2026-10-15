# 🔐 Password Strength Analyzer

A beginner-friendly cybersecurity project built with Python to evaluate basic password characteristics and provide suggestions for improving password quality.

## Features

- Checks password length.
- Detects uppercase and lowercase letters.
- Checks for numbers and symbols.
- Calculates a simple strength score.
- Displays a rating and improvement suggestions.
- Hides password input in a supported terminal.
- Includes automated unit tests.

## Technologies Used

- Python 3
- `string`
- `getpass`
- `unittest`

No external packages are required.

## Project Structure

```text
password-strength-analyzer/
├── password_checker.py
├── test_password_checker.py
├── README.md
├── .gitignore
└── LICENSE
```

## Getting Started

### Run the application

From the project directory, execute:

```bash
python password_checker.py
```

If the `python` command is unavailable on Windows, try:

```powershell
py password_checker.py
```

Alternatively, run the program using your installed Python interpreter.

### Run automated tests

```bash
python -m unittest -v
```

## How It Works

The program evaluates password length and character variety, then assigns a rating based on a simple scoring system.

The score is an educational heuristic. It does not measure actual password entropy or guarantee that a password is secure.

## Limitations

- Uses a basic scoring model.
- Does not check breached-password databases.
- Does not estimate password-cracking time.
- A strong rating does not guarantee security.

Use unique passwords for each account and consider a reputable password manager.

## Privacy

The program does not intentionally store or transmit the entered password. Password input is hidden in supported terminals. Use made-up test passwords while developing and testing the project.

## Future Improvements

- Detect common passwords and predictable patterns.
- Improve password-strength assessment.
- Build a graphical interface using Streamlit.
- Expand automated test coverage.

## Learning Outcomes

This project demonstrates Python functions, conditions, loops, strings, lists, and automated testing, along with basic cybersecurity concepts.

## Ethical Use

This project is intended for educational use and personal password-security awareness.