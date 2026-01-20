# 7-Day DevOps Challenge: Day 3 - Dependency Management with CodeArtifact

## 🎯 Project Goal
To secure the software supply chain. In Day 2, we secured the *Source Code* (GitHub). In Day 3, we focused on securing the *Dependencies* (External Libraries). I implemented **AWS CodeArtifact** as a private artifact repository to proxy and cache public Maven packages, ensuring build reliability and security.

## ⚙️ Architecture Components
* **AWS CodeArtifact:** A fully managed artifact repository service used to store private packages and proxy public ones.
* **Maven Central:** The public upstream repository for Java libraries.
* **IAM Roles:** Used to securely grant the EC2 instance permission to authenticate with CodeArtifact without hardcoding credentials.
* **Apache Maven:** Configured via `settings.xml` to retrieve libraries solely from the private AWS repository.<br>

  <img width="1380" height="429" alt="Dev 3" src="https://github.com/user-attachments/assets/59676ad9-cc00-4bfb-af7b-0b36f1dbf5ed" /><br>

## 🛠️ Implementation Steps

### 1. Repository Infrastructure
* **Domain Setup:** Created a logical domain (`omchauhan`) in AWS to manage permissions and storage across multiple repositories.
* **Upstream Connection:** Configured the repository to connect to **Maven Central Store**. This enables the "Fetch and Cache" behavior—if a package is missing locally, AWS fetches it from the public web and saves a copy forever.

### 2. Security Configuration (IAM)
* **The Challenge:** The build server (EC2) required secure access to the artifact repository.
* **The Solution:** Created a custom **IAM Policy** granting `GetAuthorizationToken` and `ReadFromRepository` permissions. Attached this policy to an **IAM Role** and associated it with the EC2 instance, eliminating the need for long-term API keys.

### 3. Build Configuration
* **Authentication:** Executed AWS CLI commands to retrieve a temporary (12-hour) authorization token for Maven.
* **Routing:** Created a `settings.xml` file to override Maven's default behavior, forcing all dependency traffic through the secure CodeArtifact endpoint.
* **Execution:** Ran `mvn -s settings.xml compile` to trigger the dependency download.

### 4. Secret Mission (Publishing)
* **Objective:** To simulate a developer publishing a private, internal tool.
* **Action:** Created a custom generic package (`secret-mission.tar.gz`), generated a SHA-256 hash for integrity, and used the AWS CLI to **publish** it to the repository.
* **Result:** Verified the custom package appeared alongside the public Maven libraries in the AWS Console.


## 🧠 Key Learnings
* **Supply Chain Security:** Understood that relying on public repositories (Maven/NPM) directly creates a risk of downtime or "left-pad" style deletion incidents.
* **Proxy Pattern:** Learned how CodeArtifact acts as a middleware, caching dependencies so the build server never talks to the open internet directly.
* **IAM Identity:** Practiced the "AWS Way" of authentication—using Roles and temporary tokens instead of hardcoded passwords in configuration files.
