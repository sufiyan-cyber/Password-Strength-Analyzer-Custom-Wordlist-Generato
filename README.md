# Password-Strength-Analyzer-Custom-Wordlist-Generator
# Password Strength Analyzer & Custom Wordlist Generator

[cite_start]This is a command-line tool built in Python as part of the Elevate Labs Internship Project[cite: 1, 2]. It provides two main cybersecurity utilities:
1.  **Password Strength Analyzer**: Evaluates the strength of a password using the `zxcvbn` library and provides feedback.
2.  **Custom Wordlist Generator**: Creates a targeted wordlist based on personal information for use in ethical password auditing.

## Features
- **Password Analysis**: Get a strength score (0-4), estimated crack time, and actionable suggestions.
- [cite_start]**Custom Wordlists**: Generate wordlists from personal data like names, dates, and nicknames to simulate realistic password attacks[cite: 65].
- [cite_start]**Smart Variations**: Automatically creates variations including capitalization, leetspeak, and appending of common years and symbols[cite: 66].
- **CLI Interface**: An easy-to-use menu-driven command-line interface.

## Setup and Installation
To run this tool, you need Python 3 installed.

1.  **Clone the repository:**

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Use
Run the script from your terminal:
```bash
python password_analyzer.py
