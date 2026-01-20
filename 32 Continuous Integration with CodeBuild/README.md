# 7-Day DevOps Challenge: Day 4 - Continuous Integration with CodeBuild

## 🎯 Project Goal
To automate the software build process. Transitioning from manual compilation, I implemented **Continuous Integration (CI)** using **AWS CodeBuild**. The pipeline now automatically fetches source code from GitHub, retrieves secure dependencies from CodeArtifact, compiles the Java application, and packages the result into an S3 bucket.

## ⚙️ Architecture Components
* **AWS CodeBuild:** A fully managed build service that compiles source code and produces artifacts.
* **Buildspec (`buildspec.yml`):** The YAML configuration file defining the build logic (phases and commands).
* **Amazon S3:** Used as the "Artifact Store" to hold the final zipped application package.
* **IAM Roles:** Custom permissions allowing the CodeBuild environment to securely authenticate with AWS CodeArtifact.<br>

  <img width="1020" height="332" alt="Dev 4" src="https://github.com/user-attachments/assets/385c4af2-ea00-4b7c-8db4-3d23261db2be" /><br>

## 🛠️ Implementation Steps

### 1. Build Definition (The Recipe)
* **Configuration:** Authored a `buildspec.yml` file in the root of the repository.
* **Phases:** Defined the `pre_build` phase to authenticate with CodeArtifact (using the AWS CLI) and the `build` phase to execute `mvn compile` using the custom settings created in Day 3.

### 2. Infrastructure Setup
* **Storage:** Provisioned an **Amazon S3 Bucket** to serve as the destination for the compiled build artifacts.
* **Project:** Configured a CodeBuild project connected to the GitHub repository via OAuth.

### 3. Security & Permissions
* **Challenge:** The build environment failed to download dependencies because it lacked access to the private repository.
* **Solution:** Modified the **CodeBuild Service Role** by attaching an inline IAM policy granting `codeartifact:GetAuthorizationToken` and `codeartifact:ReadFromRepository`.

### 4. Execution & verification
* **Automation:** Triggered the build process manually (simulating a CI trigger).
* **Artifact Generation:** Verified that CodeBuild successfully compiled the application and uploaded a `.zip` file containing the web app and all dependencies to the S3 bucket.


## 🧠 Key Learnings
* **Continuous Integration:** Learned how to decouple the build process from a developer's local machine, ensuring consistency.
* **Buildspecs:** Mastered the syntax for defining build phases (`install`, `pre_build`, `build`, `post_build`).
* **Artifact Management:** Understood the flow of data: Source (GitHub) -> Build (CodeBuild) -> Storage (S3).
