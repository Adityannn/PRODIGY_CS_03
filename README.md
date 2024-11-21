
**`ComplexityChecker`** is a Python-based tool that evaluates the strength of a password using various security criteria. It provides feedback to help users create stronger passwords by following recommended best practices. The program uses color-coded output to indicate password strength, making it easy for users to understand the strength of their passwords at a glance.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Password Strength Criteria](#password-strength-criteria)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features
- Checks password complexity based on multiple criteria:
  - Length (minimum 8 characters)
  - Presence of uppercase and lowercase letters
  - Presence of digits
  - Inclusion of special characters
- Provides visual feedback using color-coded strength levels:
  - Weak (Red)
  - Moderate (Yellow)
  - Strong (Light Green)
  - Very Strong (Green)
- User-friendly interface with clear instructions.
- Easy to understand and modify.

## Installation
To get started with `ComplexityChecker`, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Adityannn/PRODIGY_CS_03.git
   ```
   
2. **Navigate to the Directory**:
   ```bash
   cd complexitychecker
   ```

3. **Install Dependencies**:
   Make sure you have [Python](https://www.python.org/downloads/) installed (version 3.6+ recommended). Install the required package with:
   ```bash
   pip install colorama
   ```

## Usage
To run the password complexity checker, use the following command:
```bash
python complexitychecker.py
```

You will be prompted to enter a password. The tool will evaluate the password and display its strength along with recommendations for improvement if needed.

## Password Strength Criteria
The program checks the password based on the following rules:
- **Length**: Minimum of 8 characters
- **Uppercase Letter**: At least one uppercase letter (A-Z)
- **Lowercase Letter**: At least one lowercase letter (a-z)
- **Digit**: At least one numeric digit (0-9)
- **Special Character**: At least one special character (e.g., `!@#$%^&*`)
