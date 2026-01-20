# AWS-Cloud-Journey

Welcome to my Cloud Engineering & Architecture portfolio! 🚀

This repository documents my journey through the **[NextWork](https://www.nextwork.org/roadmaps/solutions-architect) AWS Solutions Architect Roadmap**. It contains infrastructure code, architectural diagrams, and documentation for real-world projects ranging from foundational networking to advanced serverless and DevOps automations.

## 🏆 Portfolio Highlights

| Domain | Key Projects | Tech Stack |
| :--- | :--- | :--- |
| **DevOps & CI/CD** | Automated "Supply Chain" Deployment | CodePipeline, CodeBuild, CodeDeploy, Docker |
| **Networking** | Custom VPC Design & Traffic Control | VPC, Subnets, NACLs, Security Groups |
| **Compute** | Scalable Web Applications | EC2, Auto Scaling, Load Balancers (ALB) |
| **Serverless** | Event-Driven Architectures | Lambda, API Gateway, DynamoDB |
| **Security** | Identity Federation & Compliance | IAM, KMS, WAF, Shield |
| **Storage** | Multi-Cloud Disaster Recovery | S3, Google Cloud Storage, Transfer Service |

---

## 🛠️ Project Showcase

### 1️⃣ The DevOps Capstone: End-to-End CI/CD 🔄
*> **Role:** DevOps Engineer*
A fully automated deployment pipeline for a Java Web App. This project moves away from manual "ClickOps" to a robust "Commit-to-Deploy" workflow.
* **Architecture:** GitHub ➔ CodeArtifact ➔ CodeBuild ➔ CodeDeploy ➔ Production EC2.
* **Key Features:** Infrastructure as Code (CloudFormation), Automated Rollbacks, Dependency Caching.

### 2️⃣ Enterprise Networking: Custom VPC 🌐
*> **Role:** Network Architect*
Designed a highly available network from scratch, bypassing the "Default VPC" limitations.
* **Architecture:** Multi-AZ deployment with public/private subnets.
* **Security:** Configured NACLs and Security Groups to implement a strict "Least Privilege" traffic model.
* **Connectivity:** Implemented NAT Gateways for secure outbound internet access from private subnets.

### 3️⃣ Serverless API & Microservices ⚡
*> **Role:** Backend Developer*
Built a serverless CRUD API that scales to zero when not in use.
* **Stack:** AWS Lambda (Python/Node.js) + API Gateway + DynamoDB.
* **Outcome:** Reduced idle compute costs by 100% compared to EC2.

### 4️⃣ High Availability & Auto Scaling 📈
*> **Role:** Systems Administrator*
Deployed a fault-tolerant web application capable of handling sudden traffic spikes.
* **Components:** Application Load Balancer (ALB) distributing traffic across an Auto Scaling Group (ASG).
* **Resilience:** Stress-tested with 100% CPU load to verify dynamic scaling policies.

### 5️⃣ Multi-Cloud Disaster Recovery (AWS ↔ GCP) 🌩️
*> **Role:** Cloud Security Engineer*
Implemented an automated backup strategy linking AWS S3 to Google Cloud Storage.
* **Security:** Used **Identity Federation** (OIDC) to grant GCP access to AWS without sharing long-term access keys.

---

## 📜 Certifications & Skills

**AWS Services Mastered:**
* **Compute:** EC2, Lambda, ECS
* **Storage:** S3, EBS, EFS, Glacier
* **Database:** RDS (MySQL/Postgres), DynamoDB
* **Networking:** VPC, Route53, CloudFront, ELB
* **Management:** CloudWatch, CloudTrail, Systems Manager

**Tools & Languages:**
* Python (Boto3), Bash Scripting, Java
* Git, GitHub Actions, Docker
* Linux Administration (RHEL/Amazon Linux)

---

## 📬 Connect with Me

I am a **Master of Science in Software Engineering** student at **Arizona State University**.

* **GitHub:** [OmChauhan9](https://github.com/OmChauhan9)
* **LinkedIn:** [Om Chauhan](https://www.linkedin.com/in/om-chauhan-42531918b/)
