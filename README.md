# 🔐 Real-time Password Strength Checker

## Table of Contents

* [About the Project](#about-the-project)
* [Features](#features)
* [How It Works](#how-it-works)
* [Usage](#usage)
* [Requirements](#requirements)
* [Installation](#installation)
* [Contributing](#contributing)
* [Contact](#contact)

---

## About The Project

This project provides a user-friendly desktop application for checking the strength of passwords in real-time. Built with Python's Tkinter library, it offers immediate feedback as you type, guiding you to create strong and secure passwords that meet common security standards.

The application aims to help users avoid weak passwords that are vulnerable to common attacks by enforcing rules such as length requirements, character variety, and preventing the use of easily guessable personal information.

## Features

* **Real-time Strength Feedback**: Instantly assesses password strength as you type.
* **Comprehensive Validation Rules**:
    * **Length Constraints**: Requires passwords to be between 6 and 15 characters.
    * **Personal Information Exclusion**: Prevents the use of your name, full date of birth (DOB), or birth year within the password.
    * **Character Diversity**: Ensures the inclusion of uppercase letters, lowercase letters, digits, and special characters.
* **Clear Visual Cues**: Uses color-coded messages (e.g., red for weak, orange for missing criteria, green for strong) to provide intuitive feedback.
* **Final Validation Check**: A dedicated button for a conclusive password assessment.

## How It Works

The application takes your name, date of birth, and desired password as input. As you type in the password field, a `StringVar` in Tkinter triggers the `update_realtime_strength` function. This function performs the following checks:

1.  **DOB Validation**: Ensures the DOB is in the correct 8-digit format (DDMMYYYY after cleaning).
2.  **Length Check**: Verifies if the password is within the 6-15 character limit.
3.  **Personal Info Check**: Scans for the presence of your name, full DOB, or birth year.
4.  **Character Type Check**: Confirms the presence of at least one lowercase, uppercase, digit, and special character.

Based on these checks, the `realtime_strength_label` is updated with appropriate messages and colors. A separate `submit_full_validation` function provides a final, more explicit validation message using `tkinter.messagebox` upon button click.

## Usage

1.  **Run the script**: Execute `password_checker.py`.
2.  **Enter Name and DOB**: Fill in your name and Date of Birth in `DD-MM-YYYY` format.
3.  **Type Password**: Enter your desired password in the password field.
4.  **Observe Feedback**: Watch the real-time strength indicator below the password field.
5.  **Final Check**: Click the "Final Password Check" button for a conclusive assessment.

## Requirements

To run this application, you need:

* Python 3.x
* Tkinter (usually bundled with Python installations; if not, install it via your OS package manager or `pip install tk`)

## Installation

1.  **Clone the repository** (or download the `password_checker.py` file directly if you used the direct upload method):
    ```bash
    git clone [https://github.com/YOUR_USERNAME/PasswordStrengthChecker.git](https://github.com/YOUR_USERNAME/PasswordStrengthChecker.git)
    cd PasswordStrengthChecker
    ```
2.  **Run the application**:
    ```bash
    python password_checker.py
    ```

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

## Contact

Your Name - your.email@example.com

Project Link: https://github.com/manavjhorad/Password-Strength-Checker/
