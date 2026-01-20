# 7-Day DevOps Challenge: Day 7 - The Grand Finale (AWS CodePipeline) 🏆

## 🎯 Project Goal
To complete the "DevOps Loop." In this final project, I unified all previous tools (GitHub, CodeBuild, CodeDeploy) into a single, automated workflow using **AWS CodePipeline**. This achieved true **Continuous Integration and Continuous Deployment (CI/CD)**, where a simple `git push` triggers the entire release process to production.

## ⚙️ Architecture Components
* **AWS CodePipeline:** The orchestration service that manages the workflow stages.
* **Source Stage (GitHub):** Detects changes in the repository using Webhooks.
* **Build Stage (CodeBuild):** Compiles the Java application and packages artifacts.
* **Deploy Stage (CodeDeploy):** Automates the deployment of the application to EC2 instances.
* **Manual Rollback:** A safety mechanism to revert production to a previous stable state.<br>

  <img width="1496" height="540" alt="Dev 7" src="https://github.com/user-attachments/assets/2eacebde-32a4-4f8a-93c2-2da5226120a6" /><br>

## 🛠️ Implementation Steps

### 1. Pipeline Orchestration
* **Setup:** configured a 3-stage pipeline connecting the existing resources created throughout the week.
* **Execution Mode:** Selected **Superseded** mode to ensure the pipeline always prioritizes the latest code commit, cancelling outdated runs to save costs and time.

### 2. The Automation Test
* **Action:** Modified the source code (`index.jsp`) in VS Code and pushed the changes to GitHub.
* **Observation:** Verified that CodePipeline automatically detected the commit, triggered the build, and initiated the deployment without any manual interaction in the AWS Console.

### 3. Verification & Safety
* **Live Check:** Confirmed the changes appeared on the live production server minutes after the push.
* **Secret Mission (Rollback):** Tested the disaster recovery capability by manually triggering a **Rollback**. Verified that AWS CodeDeploy immediately reverted the live application to the previous successful version, mitigating the "bad deployment."

## 📸 Evidence

1.  **The Complete Pipeline:** All stages (Source, Build, Deploy) executing successfully.
    <img width="1512" height="859" alt="Screenshot 2026-01-16 at 11 26 53 PM" src="https://github.com/user-attachments/assets/b03c669d-6bf3-4e4f-9e79-3bc39d80fea1" /><br>


## 🧠 Final Reflections
* **The "One-Click" Dream:** I successfully moved from manual, error-prone deployments (Day 1) to a fully automated pipeline (Day 7).
* **Integration:** Learned that DevOps is not just about tools, but about *connecting* tools. CodePipeline is the glue that makes CI/CD possible.
* **Safety First:** Understood that features like Automatic Rollbacks and Staging environments are critical for maintaining production stability in the real world.
