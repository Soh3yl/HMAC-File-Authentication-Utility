# File HMAC Generator & Verifier

## Overview
This project provides a graphical interface for generating and verifying HMAC (Hash-based Message Authentication Code) for files. It is built using Python and PyQt5, offering a sleek and modern user interface with features like:
•	HMAC Generation: Generate an HMAC for a file using a secret key.

•	HMAC Verification: Verify the integrity of a file using a previously generated HMAC.

•	User-Friendly Interface: Intuitive design with custom styling.

•	Modular Code: Clean and maintainable code structure.

## Features
•	Error Handling: User-friendly error messages with custom styling.

•	Cross-Platform: Works on Windows, macOS, and Linux.

## Requirements
To run this project, you need the following:
•	Python 3.7 or higher

•	PyQt5

## Installation
1.	Install Dependencies:
   
pip install -r requirements.txt

2.	Run the Application:
   
python main.py 

## Usage
### 1.	Generate HMAC:

  -Click Browse File to select the file you want to generate an HMAC for.

  -Enter a secret key in the Secret Key field.

  -Click Browse HMAC Output to choose where to save the HMAC.

  -Click Generate HMAC to create and save the HMAC.

### 2.	Verify HMAC:

  -Click Browse File to select the file you want to verify.

  -Enter the same secret key used to generate the HMAC.

  -Click Browse HMAC Output to select the saved HMAC file.

  -Click Verify HMAC to check the file's integrity.

### 3.	Results:

  -If the file is verified, a message will display: File Integrity: VERIFIED.

  -If the file is not verified, a message will display: File Integrity: NOT VERIFIED.

### 4.	You can also use the app without GUI. (check out “test” folder)
