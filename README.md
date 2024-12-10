# Password Combination Generator

A Python script to generate a comprehensive list of password combinations based on user inputs. This tool is designed for users who want to create secure, personalized password datasets.

## 📜 Features

- **User Input Handling**:
  - Accepts inputs in the format: `name,age,DOB` (e.g., `John,25,11-12-1998`).
  - Processes the name to generate various case variations (uppercase, lowercase, swap case).
  - Validates and processes the date of birth (DOB) into numerical sequences.

- **Password Combination Generation**:
  - Creates numerical combinations based on the provided DOB.
  - Includes special characters to enhance password variety.
  - Supports external numerical inputs from a file (`numerical.txt`).

- **Progress Tracking**:
  - Displays a dynamic progress bar to monitor the generation process.

- **File Handling**:
  - Reads numerical data from `numerical.txt`.
  - Saves all generated passwords in `pass.txt`.

## 🚀 How It Works

1. **Input**:
   - The script prompts the user to enter their `name, age, and DOB`.
   - Example input: `John,25,11-12-1998`.

2. **Processing**:
   - Generates multiple variations of the name and creates DOB-based numerical combinations.
   - Combines these inputs with special characters and pre-defined numerical data.

3. **Output**:
   - Passwords longer than six characters are saved in a file named `pass.txt`.

4. **Progress Updates**:
   - A progress bar is displayed during password generation.

## 🛠 Prerequisites

- Python 3.x installed on your system.
- A file named `numerical.txt` containing numerical values (one value per line).

## 💻 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/password-combination-generator.git
2. Navigate to the project directory:
   ```bash
   cd password-combination-generator

## 📋 Usage

1. Run the script:
   ```bash
   python main.py
2. Enter the required inputs as prompted (e.g., name,age,DOB).
3. The passwords will be saved to pass.txt in the same directory.

## 📂 Example Input and Output

Input:
John,25,11-12-1998

Output:
John@112519
JOHN#251198
john$251198
JoHn^119825
...

⚠️ Notes

1. Ensure the input format is correct: name,age,DOB (e.g., John,25,11-12-1998).
2. Larger input datasets may take longer to process.

🔒 Disclaimer

This tool is for educational purposes and personal use only. Do not use it for malicious activities.

Made with ❤️ by Hrishabh



