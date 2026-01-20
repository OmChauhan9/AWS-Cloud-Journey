# Infrastructure Orchestration: Launching Amazon EKS Clusters

## 🎯 Project Goal
To provision a production-grade Kubernetes environment on AWS. Moving beyond single-server management, I used **Amazon EKS (Elastic Kubernetes Service)** to deploy a scalable container orchestration platform. I utilized **eksctl** for Infrastructure as Code (IaC) automation and verified the cluster's high-availability "Self-Healing" capabilities.

## ⚙️ Architecture Components
* **Amazon EKS:** Managed Kubernetes Control Plane.
* **Amazon EC2:**
    * **Jump Host:** A temporary admin instance used to run CLI commands securely.
    * **Worker Nodes:** The compute fleet running the actual Kubernetes workloads.
* **eksctl:** The command-line utility that automates EKS provisioning via CloudFormation.
* **AWS CloudFormation:** The engine used under the hood to deploy the VPC, Subnets, and Auto Scaling Groups.<br>

  <img width="1276" height="693" alt="CC 7" src="https://github.com/user-attachments/assets/f044449a-a905-4281-ba0d-b0fff8400eb1" /><br>

## 🛠️ Implementation Steps

### 1. Administrative Workspace (EC2)
* **Strategy:** Instead of running commands locally, I provisioned an Amazon Linux 2023 instance to act as a clean "DevOps Workspace."
* **Tooling:** Installed `eksctl` and `kubectl` on the instance.
* **Security:** Created and attached an **IAM Role** with `AdministratorAccess` to the instance, allowing it to provision resources on my behalf without storing static access keys.

### 2. Cluster Provisioning (Infrastructure as Code)
* **Execution:** Ran the `eksctl create cluster` command.
* **Automation:** Observed how `eksctl` triggered two distinct **CloudFormation Stacks**:
    1.  **Cluster Stack:** Created the Control Plane and VPC networking.
    2.  **Node Group Stack:** Provisioned the Worker Nodes (EC2s) and Auto Scaling configurations.

### 3. Access Management (RBAC)
* **Challenge:** The EKS Console initially showed "Access Denied" for the nodes.
* **Reason:** Kubernetes RBAC (Role-Based Access Control) is separate from AWS IAM. The cluster creator (EC2 Role) had access, but my Console User did not.
* **Solution:** Created an **Access Entry** in the EKS Console to map my IAM User to the `AmazonEKSClusterAdminPolicy`.

### 4. Resilience Testing (The Secret Mission)
* **Test:** Manually terminated all 3 Worker Node EC2 instances via the AWS Console to simulate a catastrophic failure.
* **Result (Self-Healing):** The EKS Control Plane detected the health check failure. Within moments, the Auto Scaling Group automatically provisioned 3 new EC2 instances to return the cluster to its "Desired State."

## 📸 Verification

1.  **Cluster Automation:** CloudFormation stacks successfully deploying network and compute resources.
    <img width="1511" height="856" alt="Screenshot 2026-01-12 at 1 15 38 AM" src="https://github.com/user-attachments/assets/5a1af27f-ab65-4ecf-a925-9b37a0d13682" /><br>

2.  **Cluster Status:** EKS Console displaying the active cluster and associated Node Group.
    <img width="1511" height="856" alt="Screenshot 2026-01-12 at 1 15 54 AM" src="https://github.com/user-attachments/assets/ca35b094-e34e-486a-ad4c-59baed18718d" /><br>


## 🧠 Key Learnings
* **Declarative Infrastructure:** Kubernetes is "Declarative." You define the *Desired State* (e.g., "3 Nodes"), and the system works continuously to maintain that state, even if nodes crash.
* **Abstraction Layers:** `eksctl` abstracts away the complexity of creating VPCs, Subnets, and Route Tables manually, allowing Engineers to focus on the Cluster itself.
* **Identity Mapping:** Learned that AWS IAM and Kubernetes RBAC are distinct systems that must be bridged using **Access Entries** (formerly `aws-auth` ConfigMap).
