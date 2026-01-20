# Containerization Pipeline: Docker & Amazon ECR

## 🎯 Project Goal
To prepare a backend application for Kubernetes deployment. Following the provisioning of the EKS cluster (Part 1), this project focuses on the **Build Artifact** phase. I cloned a Flask application, containerized it using **Docker** to ensure environment consistency, and established a secure supply chain by pushing the image to **Amazon ECR**.

## ⚙️ Architecture Components
* **Docker:** The engine used to package the application code and dependencies into a portable image.
* **Amazon ECR (Elastic Container Registry):** A fully managed container registry used to store and scan the Docker images.
* **AWS CLI:** Used to authenticate the local Docker client with the remote ECR registry.
* **Linux Permissions:** Managed user groups to allow secure, non-root execution of Docker commands.<br>

  <img width="1627" height="781" alt="CC 8" src="https://github.com/user-attachments/assets/177fb6ec-d81a-47f8-b398-705bbb789b69" /><br>

## 🛠️ Implementation Steps

### 1. Environment Setup
* **Source Code:** Cloned the `nextwork-flask-backend` repository onto the EC2 Admin Instance.
* **Security Challenge:** Encountered a `permission denied` error when accessing the Docker Daemon.
* **Resolution:** Executed `sudo usermod -a -G docker ec2-user` to grant the user strictly defined privileges to manage containers without full `root` access.

### 2. Image Build
* **Definition:** Reviewed the `Dockerfile` to understand the layering (Python Base Image -> Install Requirements -> Copy Code).
* **Execution:** Ran `docker build -t nextwork-flask-backend .` to compile the application artifact.

### 3. Registry Configuration (ECR)
* **Provisioning:** Created a private ECR repository to host the image.
* **Authentication:** Used the `aws ecr get-login-password` command to generate a temporary authentication token, piping it securely into `docker login`.

### 4. Distribution
* **Tagging:** Applied the ECR repository URI as a tag to the local image, effectively "addressing" the package for delivery.
* **Push:** Executed `docker push` to upload the layer to the AWS Cloud.
* **Verification:** Confirmed the image's presence and `latest` tag in the ECR Console.

## 📸 Verification

1.  **Container Build:** Terminal output verifying the successful creation of the Docker image.
    <img width="1511" height="856" alt="Screenshot 2026-01-13 at 12 26 38 AM" src="https://github.com/user-attachments/assets/9a9dbcbf-e622-49ef-9324-c78eff2166c5" /><br>

2.  **Registry Creation:** AWS ECR Console displaying the active repository.
    <img width="1511" height="856" alt="Screenshot 2026-01-13 at 12 53 12 AM" src="https://github.com/user-attachments/assets/202ec2d3-92f5-4da5-abba-170cfca9c706" /><br>

3.  **Artifact Upload:** Evidence of the image stored securely in the cloud with the `latest` tag.
    <img width="1511" height="856" alt="Screenshot 2026-01-13 at 12 53 19 AM" src="https://github.com/user-attachments/assets/9dd2de57-7a07-4b8f-ac08-3477e43e5cda" /><br>

## 🧠 Key Learnings
* **Container Standardization:** Learned that EKS/Kubernetes requires applications to be containerized (not raw code) to function.
* **Linux Groups:** Deepened understanding of Linux user management and how `usermod` works to grant specific application permissions.
* **ECR Authentication:** Mastered the specific CLI pattern (`get-login-password | docker login`) required to bridge the gap between a local Docker client and a private AWS registry.
