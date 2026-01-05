# Connect a Web App with Aurora

## 🎯 Project Goal
To build a fully functional, dynamic web application on AWS. This project integrates the **Compute Layer (EC2)** with the **Persistence Layer (Amazon Aurora)**. I configured a LAMP stack (Linux, Apache, MySQL, PHP) to host a web form that captures user data and commits it to a relational database in real-time.

## ⚙️ Architecture Components
* **Amazon Aurora (MySQL):** The high-performance database cluster used to store employee records.
* **Amazon EC2 (Web Server):** An Amazon Linux 2023 instance hosting the application code.
* **Apache Web Server (httpd):** The engine serving the web pages to the internet.
* **PHP:** The server-side scripting language used to process form data and communicate with the database.
* **MySQL CLI:** Used to verify data integrity directly from the terminal.<br>

  <img width="1464" height="1051" alt="Database 2" src="https://github.com/user-attachments/assets/e9e58a9c-d913-4d5a-9d20-577ea40dfeb7" />

## 🛠️ Implementation Steps

### 1. Web Server Configuration (Linux CLI)
* **Environment:** Updated the OS (`sudo dnf update`) and installed the required software stack:
    * `httpd` (Apache Web Server)
    * `php` (Application Logic)
    * `php-mysqli` (Database Driver)
    * `mariadb105` (SQL Client Tools)

### 2. Application Deployment
* **Security:** Created a dedicated configuration file (`dbinfo.inc`) in a separate directory (`/var/www/inc`) to store database credentials securely, rather than hardcoding them in the public HTML folder.
* **Logic:** Developed a PHP application (`SamplePage.php`) that:
    1.  Establishes a connection to the Aurora Writer Endpoint.
    2.  Checks if the `Employees` table exists (and creates it if not).
    3.  Accepts user input (Name, Address) and executes an `INSERT` SQL statement.

### 3. Data Flow Verification
* **Frontend Test:** Accessed the application via the EC2 Public DNS. Successfully submitted entry "King of Zamunda" via the web form.
* **Backend Verification:**
    * Logged into the Aurora Database via the terminal (`mysql -h ...`).
    * Executed `SELECT * FROM employees;`.
    * **Result:** Confirmed the data submitted via the web browser was accurately stored in the database.

## 📸 Verification

1.  **Server Access:** Successful SSH connection to the Amazon Linux instance.
    <img width="1511" height="283" alt="Screenshot 2026-01-03 at 11 16 25 PM" src="https://github.com/user-attachments/assets/70e4c1f9-7b98-4a0c-bf78-a525cf1bf142" /><br>

2.  **The Web Application:** The live PHP application collecting and displaying user data.
    <img width="1509" height="856" alt="Screenshot 2026-01-03 at 11 36 41 PM" src="https://github.com/user-attachments/assets/51a48bc5-4430-463e-8bc9-cb2920b758a5" /><br>

3.  **Database Verification:** Terminal output proving data persistence via SQL queries.
    <img width="1509" height="829" alt="Screenshot 2026-01-03 at 11 44 11 PM" src="https://github.com/user-attachments/assets/c09eb0a4-5f38-4bea-9b33-209b7b7af3bc" /><br>

## 🧠 Key Learnings
* **The LAMP Stack:** Gained practical experience configuring Linux, Apache, MySQL, and PHP to work together in a cloud environment.
* **Security Best Practices:** Learned to separate credential files (`.inc`) from public HTML files to prevent sensitive data exposure.
* **Troubleshooting:** Navigated permission errors (`chmod 400`) and SQL syntax requirements (semicolons and quotes) during the testing phase.
