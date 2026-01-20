# 7-Day DevOps Challenge: Day 5 - Automated Deployment with CodeDeploy

## 🎯 Project Goal
To bridge the gap between "Built" and "Live." After automating the build process in Day 4, Day 5 focused on **Continuous Deployment (CD)**. I provisioned a production environment using **CloudFormation** and configured **AWS CodeDeploy** to automatically install the application on a live server, completing the CI/CD pipeline.

## ⚙️ Architecture Components
* **AWS CloudFormation:** Used "Infrastructure as Code" to provision a production-ready VPC and EC2 instance tagged for deployment.
* **AWS CodeDeploy:** The service responsible for pulling the artifact from S3 and deploying it to the fleet of EC2 instances.
* **AppSpec (`appspec.yml`):** The configuration file defining the deployment hooks and mapping them to shell scripts.
* **Bash Scripts:** Custom scripts (`install_dependencies.sh`, `start_server.sh`, `stop_server.sh`) to manage the application lifecycle.<br>

  <img width="1173" height="386" alt="Dev 5" src="https://github.com/user-attachments/assets/62fc13a5-ebc6-4744-a906-d16b4bf14ada" /><br>

## 🛠️ Implementation Steps

### 1. Infrastructure Provisioning (IaC)
* **Action:** Deployed a CloudFormation stack (`devops-webapp.yaml`) to launch a clean "Production" EC2 instance.
* **Tagging Strategy:** The instance was automatically tagged with `Role: web-server`, allowing CodeDeploy to dynamically identify target servers without hardcoded IP addresses.

### 2. Deployment Scripting
* **Logic:** Created shell scripts to automate manual tasks:
    * **Dependencies:** Installing Tomcat and Apache via `yum`.
    * **Lifecycle:** Starting and stopping services using `systemctl`.
* **Configuration:** Authored `appspec.yml` to instruct CodeDeploy to run `ApplicationStop` first (to clear old versions), followed by `BeforeInstall` and `ApplicationStart`.

### 3. Pipeline Integration
* **The Bridge:** Updated `buildspec.yml` to include the new scripts and `appspec.yml` in the final zip artifact.
* **Re-Build:** Triggered AWS CodeBuild to generate a new artifact containing the deployment logic.

### 4. Deployment Execution
* **Setup:** Configured a CodeDeploy Application and Deployment Group targeting instances with the `web-server` tag.
* **IAM Security:** Created a service role granting CodeDeploy permission to access EC2 and S3.
* **Result:** Successfully deployed the Java Web App to the production server. Verified by accessing the public DNS of the new instance.

## 🧠 Key Learnings
* **Infrastructure as Code (IaC):** Experienced the power of CloudFormation to spin up complex networking and compute resources from a single template.
* **Deployment Lifecycle:** Understood the sequence of a deployment (`Stop` -> `Install` -> `Start`) and how to hook into these events using AppSpec.
* **Tag-Based Deployment:** Learned how CodeDeploy uses tags to manage fleets of instances, allowing for scalable deployments without manual IP management.
