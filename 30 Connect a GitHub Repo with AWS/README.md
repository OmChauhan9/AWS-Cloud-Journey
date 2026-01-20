# 7-Day DevOps Challenge: Day 2 - Source Control Integration

## 🎯 Project Goal
To secure the application code and enable collaboration. Building on Day 1 (where the code lived solely on the EC2 server), Day 2 focused on implementing **Git** for version control and integrating with **GitHub**. This establishes the "Source" stage of the CI/CD pipeline.

## ⚙️ Architecture Components
* **Git:** Distributed Version Control System installed on the Linux EC2 instance.
* **GitHub:** Cloud-based hosting service used as the Remote Repository.
* **Personal Access Token (PAT):** The security mechanism used to authenticate the CLI with GitHub.
* **EC2 Instance:** The "Local" development environment pushing code to the cloud.<br>

  <img width="1347" height="447" alt="Dev 2" src="https://github.com/user-attachments/assets/cff8ce97-b7d1-4921-b889-dc21f75f11a4" /><br>

## 🛠️ Implementation Steps

### 1. Version Control Setup
* **Installation:** Installed Git via the CLI (`dnf install git`).
* **Initialization:** Transformed the Maven project folder into a tracked repository using `git init`.
* **Configuration:** Set global user identity parameters to ensure accurate change attribution in the commit history.

### 2. Security & Authentication
* **Challenge:** GitHub deprecated password authentication for CLI operations.
* **Solution:** Generated a **Personal Access Token (Classic)** with `repo` scope permissions.
* **Implementation:** Used this token as the authentication credential when establishing the secure handshake between the AWS Server and GitHub.

### 3. Cloud Integration
* **Remote Linking:** Connected the local EC2 directory to the GitHub repository using `git remote add origin`.
* **Push Operation:** Executed the standard Git workflow:
    1.  `git add .` (Staging)
    2.  `git commit` (Local Save)
    3.  `git push -u origin master` (Cloud Upload)
* **Result:** Successfully replicated the local Java Web App code to the centralized GitHub repository.

### 4. Secret Mission (The README)
* **Action:** Created a `README.md` file directly on the server using `touch` and `nano`.
* **Markdown:** formatted the file to include project setup instructions and contact details.
* **Verification:** Pushed the new file to GitHub and verified that the repository homepage instantly updated to display the documentation.


## 🧠 Key Learnings
* **Token Authentication:** Mastered the use of PATs for secure CLI authentication, a standard requirement in modern DevOps environments.
* **Distributed Version Control:** Understood the decoupling of "Local" (EC2) vs. "Remote" (GitHub) repositories.
* **The Pipeline Foundation:** Recognized that getting code into GitHub is the trigger event that will eventually start the CI/CD automation in future steps.
