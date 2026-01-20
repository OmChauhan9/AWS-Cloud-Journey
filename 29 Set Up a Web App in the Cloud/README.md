# 7-Day DevOps Challenge: Day 1 - Web App Setup

## 🎯 Project Goal
To kickstart a CI/CD pipeline project by building the foundational application. In this first phase ("Day 1"), I provisioned a Cloud Server (EC2), configured a remote development environment (VS Code + SSH), and generated a **Java Web Application** from scratch using **Apache Maven**.

## ⚙️ Architecture Components
* **Amazon EC2:** A virtual server in the cloud used to host the development environment.
* **VS Code (Remote SSH):** The Integrated Development Environment (IDE) used to edit code directly on the remote server.
* **Apache Maven:** The build automation tool used to generate the project structure (Archetype) and manage dependencies.
* **Java (Corretto 8):** The programming language runtime required to execute the application.<br>

  <img width="1326" height="406" alt="Dev 1" src="https://github.com/user-attachments/assets/3bcdd017-8044-4811-b537-8395522877a1" /><br>

## 🛠️ Implementation Steps

### 1. Infrastructure Provisioning
* **Compute:** Launched an `Amazon Linux 2023` instance (t2.micro) on AWS.
* **Security:** Configured a **Security Group** to allow SSH traffic (Port 22) strictly from my IP address to prevent unauthorized access.
* **Access:** Created a `.pem` Key Pair (`nextwork-key-pair`) to authenticate the SSH connection.

### 2. Environment Setup
* **Connection:** Utilized the **VS Code Remote-SSH** extension to establish a secure tunnel to the EC2 instance, allowing for a seamless coding experience.
* **Tooling:** Installed `java-1.8.0` and `apache-maven` via the Linux command line (`dnf install`).
* **Verification:** Confirmed installation by checking version outputs (`mvn -version`).

### 3. Application Generation
* **Scaffolding:** Executed the `mvn archetype:generate` command to create a standard Java Web App structure (`maven-archetype-webapp`).
* **Result:** Successfully generated the `nextwork-web-project` directory containing the source code (`src`) and web resources (`webapp`).

### 4. "Secret Mission" (CLI Editing)
* **Challenge:** Edited the `index.jsp` file without using the VS Code GUI.
* **Execution:** Navigated to the file path using `cd` and used the **Nano** text editor to manually modify the HTML content to say "Hello [My Name]".
* **Learning:** Verified that changes made in the CLI were instantly reflected in the VS Code IDE, demonstrating the real-time nature of the SSH connection.


## 🧠 Key Learnings
* **Remote Development:** Learned how to treat a Cloud Server as my personal development machine using Remote SSH.
* **Scaffolding:** Understood the power of **Maven Archetypes** to standardize project structures, saving time on initial setup.
* **CLI vs GUI:** Gained comfort switching between the efficiency of the Terminal (for commands) and the ease of the IDE (for code editing).
