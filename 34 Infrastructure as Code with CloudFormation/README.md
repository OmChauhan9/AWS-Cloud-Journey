# 7-Day DevOps Challenge: Day 6 - Infrastructure as Code with CloudFormation

## 🎯 Project Goal
To transition from manual configuration to **Infrastructure as Code (IaC)**. In Day 6, I used **AWS CloudFormation** to reverse-engineer my existing DevOps infrastructure. I scanned the account, generated a template, fixed logical dependencies, and successfully automated the provisioning of the entire CI/CD stack.

## ⚙️ Architecture Components
* **AWS CloudFormation:** The IaC service used to define and provision AWS infrastructure.
* **IaC Generator:** A tool to scan existing resources and bootstrap a CloudFormation template.
* **YAML:** The data serialization language used to write the infrastructure definition.
* **The DevOps Stack:** CodeArtifact, CodeBuild, CodeDeploy, S3, and IAM Roles—all defined as code.<br>

  <img width="1021" height="469" alt="Dev 6" src="https://github.com/user-attachments/assets/b4428a0d-e929-414d-a9b9-4bb846d6ef05" /><br>


## 🛠️ Implementation Steps

### 1. Resource Discovery
* **Scanning:** Utilized the **CloudFormation IaC Generator** to index all resources created in Days 1-5.
* **Filtering:** Selected the specific CI/CD resources (IAM Roles, S3 Buckets, Code connections) to import into the template foundation.

### 2. Template Refactoring (The Hard Part)
* **Dependency Management:** Encountered race conditions where Policies tried to attach to Roles that didn't exist.
* **Fix:** Implemented the `DependsOn` attribute in the YAML to enforce sequential provisioning.
* **Circular Dependencies:** Resolved a "deadlock" where Roles and Policies referenced each other. I refactored the code to decouple the Role creation from the Policy attachment.

### 3. Secret Mission (Manual Definitions)
* **Limitations:** The generator could not scan the CodeBuild Project or Deployment Group.
* **Authoring:** Manually wrote the CloudFormation YAML definitions for these complex resources, linking them dynamically to the S3 buckets and IAM roles using `!Ref` and `!GetAtt`.
* **Parameterization:** Added `Parameters` for GitHub credentials to make the template reusable for other developers.

### 4. Verification (The Phoenix Test)
* **Destruction:** Manually deleted the entire manual infrastructure to simulate a clean environment.
* **Reconstruction:** Deployed the CloudFormation stack.
* **Result:** Verified that the entire ecosystem (Artifacts, Build Projects, Deployment Groups) was restored in <3 minutes with zero manual configuration.

## 🧠 Key Learnings
* **Reverse Engineering:** Learned how to bootstrap IaC by scanning existing resources rather than writing from scratch.
* **Logical Dependencies:** Mastered the nuance of `DependsOn` and how CloudFormation handles parallel resource creation.
* **Disaster Recovery:** Realized that having this template turns a potential disaster (accidental deletion) into a minor inconvenience, as the entire stack can be respawned instantly.
