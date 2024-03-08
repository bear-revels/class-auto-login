# Auto Attendance Program

Automate the task of checking in and out of class on a Moodle webpage.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

This Python program automates the process of checking in and out of class on a Moodle webpage at specific times each weekday. It uses Selenium WebDriver to interact with the webpage and performs the following actions:
- Logs in with provided username and password.
- Clicks the 'Check in' button at 09:00 and 13:30 CET on Mondays, Tuesdays, Wednesdays, Thursdays, and Fridays.
- Selects the location ('oncampus' or 'athome') based on the current day.
- Clicks the 'Check out' button at 12:30 and 17:00 CET on Mondays, Tuesdays, Wednesdays, Thursdays, and Fridays.

## Features

- Headless execution using Selenium WebDriver.
- Automates checking in and out of class at specific times on weekdays.
- Supports logging with error handling.
- Runs non-locally so user doesn' need to devote local machine to task.

## Prerequisites

- Python 3.x
- Chrome WebDriver
- GitHub repository with secrets configured for Moodle username and password

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/auto-attendance.git

2. Clone the repository:
   ```
   pip install -r requirements.txt

## Usage

1. Configure GitHub Secrets:
    - MOODLE_USERNAME: Your Moodle username.
    - MOODLE_PASSWORD: Your Moodle password.

2. Ensure the Chrome WebDriver is installed and in your system's PATH.

3. Run the program:
    ```
    python auto_attendance.py

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or additional features.