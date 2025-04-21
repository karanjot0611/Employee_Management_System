# Employee Management System

This is a Python-based Employee Management System that allows for managing employee records, including their IDs, names, phone numbers, roles, genders, and salaries. It utilizes **CTkinter** for the graphical user interface (GUI) and **MySQL** for database management. The system allows you to add, update, delete, and search employee records.

## Features

- **Login System**: A secure login page for authentication.
- **Employee Management**: Add, update, delete, and view employee details.
- **Search Functionality**: Search employees by ID, name, phone number, role, gender, or salary.
- **Data Storage**: All data is stored in a MySQL database.
- **User Interface**: The system is built using Tkinter for a modern and easy-to-use interface.

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python`
- `customtkinter` library
- `Pillow` library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Employee-Management-System.git
   ```

2. **Install the required libraries**:
   You can install the required Python libraries using `pip`:
   ```bash
   pip install mysql-connector-python customtkinter Pillow
   ```

3. **Setup MySQL Database**:
   - Create a database named `employee_data` in MySQL.
   - Run the SQL schema provided in `database.py` to create the necessary table.

4. **Run the Application**:
   - Launch the `Login.py` file to start the system:
   ```bash
   python Login.py
   ```

## Files

- **Login.py**: Handles the login page.
- **Employee_Management_System.py**: The main program for managing employee records.
- **database.py**: Contains functions for interacting with the MySQL database.
- **bg.jpg / BG EMS.png**: Images used in the interface.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- **Tkinter** for creating the GUI.
- **MySQL** for database management.
- **Pillow** for handling image assets in the UI.
