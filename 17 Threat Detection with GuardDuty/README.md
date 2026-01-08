# Threat Detection with GuardDuty

## 🎯 Project Goal
To simulate a full cybersecurity kill chain (Attack & Defense) in a cloud environment. I deployed a vulnerable web application (**OWASP Juice Shop**), executed **SQL and Command Injection** attacks to steal cloud credentials, and utilized **Amazon GuardDuty** to detect the breach using Machine Learning-powered threat intelligence.

## ⚙️ Architecture Components
* **OWASP Juice Shop:** A purposely insecure web application used for security training.
* **Amazon EC2:** The compute instance hosting the web application.
* **Amazon GuardDuty:** The threat detection service that monitors for malicious activity and unauthorized behavior.
* **AWS CloudShell:** Used as the "Attacker's Terminal" to execute CLI commands with stolen credentials.
* **Amazon S3:** The storage bucket containing the "Secret Information" target.<br>

  <img width="924" height="240" alt="Security 2" src="https://github.com/user-attachments/assets/123fbe75-577c-414b-acb7-fdc920b800b5" /><br>


## 🛠️ Implementation Steps

### 1. The Deployment (Infrastructure)
* **Tool:** AWS CloudFormation.
* **Process:** Deployed a pre-configured stack that launched the Juice Shop on an EC2 instance and configured a VPC with an associated S3 bucket containing sensitive data.

### 2. The Attack (Red Team)
* **SQL Injection:** Exploited the login form by injecting `' or 1=1;--` to bypass authentication and gain Admin access.
* **Command Injection:** Injected a malicious script into the "Username" profile field. The unsanitized input forced the server to query the **EC2 Instance Metadata Service**.
* **Credential Theft:** The script exposed the temporary IAM credentials (Access Key & Secret Key) of the EC2 instance to a public endpoint (`credentials.json`).

### 3. The Exfiltration
* **Tool:** AWS CloudShell.
* **Action:**
    1.  Downloaded the exposed credentials.
    2.  Configured a rogue AWS CLI profile (`stolen`).
    3.  Used the stolen profile to access the private S3 bucket and download `secret_information.txt`.
* **Result:** Validated that I had full read-access to the private data using the compromised keys.

### 4. The Defense (Blue Team)
* **Service:** Amazon GuardDuty.
* **Finding:** Detected **"UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS"**.
* **Analysis:** GuardDuty correctly identified that the EC2 instance's credentials were being used from an external IP address (CloudShell), which deviates from normal behavior patterns.

### 5. Malware Protection (Bonus)
* **Configuration:** Enabled GuardDuty Malware Protection for S3.
* **Test:** Uploaded an **EICAR** test file to the bucket.
* **Result:** GuardDuty successfully scanned and flagged the file as "Malicious" without requiring agent installation.

## 📸 Verification

1.  **The Exploit:** Successfully logging in as Admin via SQL Injection.
    <img width="1200" height="1440" alt="image" src="https://github.com/user-attachments/assets/8b9b00f1-d374-43c1-8065-73d0662145a1" /><br>

    <img width="3362" height="2538" alt="image" src="https://github.com/user-attachments/assets/ec507651-40f8-4730-8974-ad0cd82a66e3" /><br>

2.  **The Breach:** CloudShell terminal showing the contents of the stolen secret file.
    <img width="3488" height="1436" alt="image" src="https://github.com/user-attachments/assets/de98c29c-5b09-4e16-8b7a-4f6df2cc95a1" /><br>

3.  **The Detection:** GuardDuty Console displaying the High Severity finding details.
    <img width="2568" height="1524" alt="image" src="https://github.com/user-attachments/assets/e846482b-0da9-446e-b3d2-1681f221774d" /><br>

## 🧠 Key Learnings
* **Input Sanitization:** The critical importance of validating user input to prevent SQL and Command Injection.
* **Instance Metadata Security:** How attackers target the metadata service to steal IAM roles, and why restricting access to it is a best practice.
* **Anomaly Detection:** How GuardDuty uses ML to distinguish between legitimate API calls and suspicious behavior (like keys being used from the wrong location).
