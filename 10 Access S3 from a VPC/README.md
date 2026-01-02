# Accessing S3 from VPC

## 🎯 Project Goal
To bridge the gap between compute (EC2) and storage (S3). I configured an EC2 instance with **Access Keys** to programmatically interact with Amazon S3 using the **AWS CLI**, bypassing the need for the AWS Management Console.

## ⚙️ Architecture Components
* **AWS CLI (Command Line Interface):** A tool to manage AWS services using scripts/commands.
* **Access Keys:** Long-term credentials (ID & Secret) used to authenticate the CLI.
* **Amazon S3:** The storage service we are controlling remotely.<br>

  <img width="991" height="473" alt="Screenshot 2026-01-02 at 11 41 41 AM" src="https://github.com/user-attachments/assets/6c27e643-8a4a-4b17-b147-b6b8238a9be8" /><br>


## 🛠️ Implementation Steps

### 1. Credentials Setup (Access Keys)
* **Challenge:** EC2 instances do not have permissions by default.
* **Action:** Generated an **Access Key Pair** (ID + Secret) for my IAM User.
* *Security Note:* While I used Access Keys for this lab, I learned that **IAM Roles** are the production best practice as they use temporary, rotating credentials.

### 2. Configuring the Environment
* logged into the EC2 instance via SSH.
* Ran `aws configure` to inject the credentials.
* **Validation:** Ran `aws s3 ls` to confirm the instance could "see" my S3 buckets.

### 3. Remote Management (The Upload Test)
Instead of using the drag-and-drop console:
1.  Created a local file (`touch secret_message.txt`).
2.  Used the copy command (`aws s3 cp`) to push the file to the cloud.
3.  Verified the file appeared in the S3 Bucket immediately.

## 📸 Verification

1.  **CLI Authentication:** Terminal showing the successful listing of S3 buckets.
    <img width="1512" height="859" alt="Screenshot 2025-12-31 at 12 47 25 AM" src="https://github.com/user-attachments/assets/1534839e-001f-4127-a49a-33c523016f69" /><br>

    <img width="1512" height="859" alt="Screenshot 2025-12-31 at 12 48 30 AM" src="https://github.com/user-attachments/assets/a7479e5b-4518-4e9a-94f1-66ae65555312" /><br>


2.  **Remote Upload:** Screenshot of the S3 Console showing the file uploaded via CLI.
    <img width="1512" height="859" alt="Screenshot 2025-12-31 at 12 47 40 AM" src="https://github.com/user-attachments/assets/1a8cf701-37cc-4276-af77-517d1a0993bd" />


## 🧠 Key Learnings
* **CLI Power:** The AWS CLI allows for automation. I can write a script to upload 1,000 files in seconds, which is impossible via the Console.
* **Public Internet Routing:** Currently, this traffic travels from my VPC, out to the Public Internet, and then to S3. In the next project, I will learn how to secure this using **VPC Endpoints**.
* **Credentials:** Learned that `aws configure` stores keys locally on the instance, which is why deleting them after the lab is critical for security.
