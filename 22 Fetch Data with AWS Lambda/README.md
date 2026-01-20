# Serverless Data Tier: Connecting Lambda to DynamoDB

## 🎯 Project Goal
To complete the "Three-Tier Architecture" by implementing the **Data Tier**. In this final phase, I integrated the Logic Tier (Lambda) with a NoSQL database (DynamoDB). The objective was to enable the serverless backend to dynamically fetch user profiles while strictly managing **IAM Permissions** to ensure security.

## ⚙️ Architecture Components
* **Amazon DynamoDB:** A serverless, Key-Value NoSQL database used to store user profiles.
* **AWS SDK (Node.js):** The library used within the Lambda function to communicate with DynamoDB.
* **IAM Roles & Policies:** The security layer that explicitly grants the Lambda function permission to `GetItem` from the database.
* **Full Stack Integration:** Validating the complete flow: `API Gateway -> Lambda -> DynamoDB`.<br>

  <img width="1340" height="268" alt="CC 3" src="https://github.com/user-attachments/assets/645ad2c6-89e7-4143-aa78-77aa2337953b" /><br>

## 🛠️ Implementation Steps

### 1. Data Modeling (DynamoDB)
* **Table Design:** Created a table named `UserData` with a Partition Key of `UserId` (String).
* **Data Seeding:** Inserted a sample item (`UserId: 1`, `Name: Test User`) using the AWS CLI to verify the table structure.

### 2. Logic Tier Update
* **Dependency:** Updated the Node.js Lambda function to require the `aws-sdk`.
* **Logic:** Wrote a function to instantiate a `DocumentClient` and fetch specific items based on the `UserId`.

### 3. Identity & Access Management (The Challenge)
* **Issue:** The initial test failed with `AccessDeniedException`.
* **Root Cause:** The Lambda Execution Role lacked permissions to access the Data Tier.
* **Resolution:** Attached the `AmazonDynamoDBReadOnlyAccess` policy to the IAM Role, adhering to the Principle of Least Privilege (Read-Only vs. Full Access).

### 4. End-to-End Testing
* **Execution:** Triggered the API Gateway endpoint.
* **Verification:** Confirmed that the API returned the exact JSON object stored in DynamoDB, proving the successful integration of all three tiers.

## 📸 Verification

1.  **Data Persistence:** DynamoDB table populated with sample user data.
    <img width="1511" height="856" alt="Screenshot 2026-01-10 at 1 14 18 AM" src="https://github.com/user-attachments/assets/8134dbe4-7b40-44fd-82f6-4840bcbbd06f" /><br>

2.  **Logic Implementation:** Lambda function code interacting with the AWS SDK.
    <img width="1511" height="856" alt="Screenshot 2026-01-10 at 1 13 44 AM" src="https://github.com/user-attachments/assets/54cbafd4-453b-42e6-a05d-422d7f60fbb8" /><br>

3.  **Security Configuration:** IAM Role displaying the attached Read-Only policy.
    <img width="1511" height="856" alt="Screenshot 2026-01-10 at 1 13 56 AM" src="https://github.com/user-attachments/assets/0e6f3902-b648-4df6-a1da-397b745cdb61" /><br>

4.  **Full Stack Success:** API response confirming data retrieval from the database.
    <img width="1511" height="856" alt="Screenshot 2026-01-10 at 1 15 00 AM" src="https://github.com/user-attachments/assets/ebe81b53-5830-4d3d-809f-e837c4b0cab0" /><br>

## 🧠 Key Learnings
* **IAM is Key:** Learned that in AWS, services don't talk to each other by default. You must explicitly grant permissions via IAM Roles.
* **SDK Efficiency:** Discovered how the AWS SDK abstracts the complexity of signing HTTP requests, making database calls as simple as a function call.
* **Three-Tier Completion:** Successfully linked Presentation (S3/CloudFront), Logic (API Gateway/Lambda), and Data (DynamoDB) into a cohesive serverless application.
