# Encrypt Data with AWS KMS

## 🎯 Project Goal
To implement **Encryption at Rest** using a Customer Managed Key (CMK) in AWS Key Management Service (KMS). This project demonstrates the critical security concept that **Identity (IAM)** is separate from **Data Visibility (Encryption)**. I proved that a user with "Full Database Access" still cannot read sensitive data without explicit decryption permissions.

## ⚙️ Architecture Components
* **AWS KMS (Key Management Service):** Created a Symmetric Customer Managed Key (`aws-task16-key`) to control data security.
* **Amazon DynamoDB:** A NoSQL database configured to use the custom KMS key for server-side encryption.
* **AWS IAM:** Created a test user (`aws-task16-user`) to simulate a "breach" or unauthorized internal access attempt.
* **Key Policies:** The resource-based policy that ultimately controls who can unlock the data.<br>

  <img width="804" height="386" alt="Security 1" src="https://github.com/user-attachments/assets/7e23f427-b3a9-4c36-86fd-b10c3eb04688" /><br>


## 🛠️ Implementation Steps

### 1. Cryptographic Key Management
* **Action:** Provisioned a **Symmetric Key** in AWS KMS.
* **Configuration:** Defined Key Administrators (myself) but intentionally excluded Key Users initially to test the security boundaries.

### 2. Encrypted Database Deployment
* **Service:** Deployed a DynamoDB table (`aws-task16-db`).
* **Security:** Enabled **Server-Side Encryption (SSE)** using the specific KMS key created in Step 1, rather than the default AWS-owned key. This ensures strict control over data access.

### 3. The "Access vs. Decrypt" Experiment
* **Scenario:** Created a user with `AmazonDynamoDBFullAccess` policy.
* **Hypothesis:** Since the user has "Full Access," they should be able to read the table data.
* **Test:** Logged in as the test user and attempted to `Scan` the table.
* **Result:** **FAILED.** The operation returned `AccessDeniedException: User is not authorized to perform: kms:Decrypt`.
* **Conclusion:** Verified that resource permissions (IAM) are insufficient if the user lacks the specific cryptographic key permissions.

### 4. Policy Remediation
* **Action:** Updated the KMS Key Policy to include the test user in the "Key Users" list.
* **Validation:** Retried the table scan. The data was instantly decrypted and visible ("Transparent Data Encryption").

## 📸 Verification

1.  **Key Infrastructure:** The active Customer Managed Key in the KMS Console.
    <img width="1499" height="855" alt="Screenshot 2026-01-06 at 1 59 25 AM" src="https://github.com/user-attachments/assets/4e4e1a46-a539-457f-a6ec-0e6c1b7c2331" /><br>

2.  **Encryption Configuration:** DynamoDB settings confirming the use of the custom key.
    <img width="1499" height="855" alt="Screenshot 2026-01-06 at 2 00 01 AM" src="https://github.com/user-attachments/assets/087edc02-ad6a-4fd8-ac9b-90351479b53c" /><br>

3.  **Security Proof:** The critical error message proving "Full Access" does not bypass Encryption.
    <img width="1499" height="855" alt="Screenshot 2026-01-06 at 2 00 49 AM" src="https://github.com/user-attachments/assets/29baec51-75b4-4ec6-9cde-379367bfcac3" /><br>


## 🧠 Key Learnings
* **Separation of Duties:** Learned how to architect systems where Database Admins manage infrastructure but cannot read sensitive data (PII) without specific key access.
* **Symmetric vs. Asymmetric:** Applied Symmetric encryption (Single Key) for high-performance database protection.
* **Transparent Data Encryption (TDE):** Understood that cloud services handle the heavy lifting of encryption/decryption on the fly, provided the permissions are correct.
