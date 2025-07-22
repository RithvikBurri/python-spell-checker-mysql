# Smart Spell Checker

Interactive Python spell checker using MySQL database for word validation. Detects misspelled words, provides correction suggestions using string similarity algorithms, and logs user selections with timestamps for analysis.

## Purpose

Demonstrates database integration, string matching algorithms, and interactive Python applications. Logged corrections help identify common errors and improve suggestion accuracy.

## Skills Learned

Throughout the development of this project, I gained hands-on experience and strengthened my skills in:

* **Database Management:** MySQL connections, CRUD operations, and schema design
* **Python Programming:** Command-line applications, user input handling, and program flow control
* **String Manipulation:** Text cleaning, punctuation handling, and case sensitivity management
* **Algorithm Implementation:** String similarity algorithms for intelligent word suggestions
* **Error Handling & Logging:** Misspelling detection, correction suggestions, and change tracking
* **Data Analysis Fundamentals:** Using logged data to identify patterns and improve system performance
* **Development Environment Proficiency**: Gained familiarity and efficiency with VS Code for project development and debugging.
<br>

# Instructions: Setup and Run

Follow these steps to set up and run the Smart Spell Checker locally:

## 1. Clone the Repository

```bash
git clone https://github.com/RithvikBurri/python-spell-checker-mysql.git
cd python-spell-checker-mysql
```

## 2. Set Up MySQL Database

Make sure MySQL is installed and running on your system.

Open your MySQL client (such as MySQL Workbench or terminal), and run the SQL script to set up the database:

```bash
source dictionary_dump.sql;
```

This will create the required database and populate it with initial data.

## 3. Configure Database Connection

In `dictionary.py`, update the database connection details with your own MySQL credentials:

```python
connection = mysql.connector.connect(
    host='localhost',
    user='your_mysql_username',
    password='your_mysql_password',
    database='your_database_name'
)
```

## 4. Install Required Python Packages

Make sure you're using Python **3**.

Install the MySQL connector:

```bash
pip install mysql-connector-python
```

## 5. Run the Application

```bash
python dictionary.py
```

## How It Works

1. Enter a sentence when prompted.
2. The program will identify misspelled words.
3. You'll be shown a list of correction suggestions for each word.
4. Your selections will be logged for future analysis.

