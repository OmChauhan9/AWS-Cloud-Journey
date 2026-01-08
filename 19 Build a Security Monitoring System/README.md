# Security Monitoring System: CloudTrail, CloudWatch & SNS Pipeline

## 🎯 Project Goal
To build a real-time security surveillance system for an AWS environment. The objective was to detect unauthorized access to sensitive data (Secrets Manager) and trigger an immediate email alert to the security team (me). This project simulates a **Security Operations Center (SOC)** workflow using native AWS observability tools.

## ⚙️ Architecture Components
* **AWS Secrets Manager:** Stored a dummy "Top Secret" credential to act as the honeypot/protected asset.
* **AWS CloudTrail:** The "CCTV" system that logs every API call made in the account, specifically tracking `GetSecretValue`.
* **Amazon CloudWatch Logs:** Ingested the CloudTrail logs to allow for filtering and analysis.
* **CloudWatch Metric Filter:** A custom filter designed to parse raw logs and count occurrences of the specific "Secret Accessed" pattern.
* **Amazon SNS (Simple Notification Service):** The messaging bus used to broadcast the alarm to email subscribers.<br>

  <img width="1478" height="554" alt="Security 4" src="https://github.com/user-attachments/assets/c6545e17-6d47-48ac-860d-a188f1c1eff9" /><br>


## 🛠️ Implementation Steps

### 1. Asset Creation (The Target)
* **Action:** Provisioned a secret in AWS Secrets Manager containing a mock API key.
* **Security Context:** In a real scenario, this would be a database password or production API key that requires strict monitoring.

### 2. Logging & Surveillance
* **Service:** AWS CloudTrail.
* **Configuration:** Created a new Trail to track **Management Events**.
* **Key Learning:** Learned that accessing a secret is classified as a "Management Event" (free to track) rather than a "Data Event," prioritizing security visibility.

### 3. Metric Filtering (The Logic)
* **Challenge:** CloudTrail collects thousands of logs. I needed to isolate *only* the specific event where the secret was read.
* **Solution:** Created a **CloudWatch Metric Filter** looking for the specific JSON pattern `GetSecretValue`.
* **Result:** Every time the pattern matched, a custom metric (`SecretAccessed`) was incremented by 1.

### 4. Automated Alerting (The Response)
* **Tool:** CloudWatch Alarms + SNS.
* **Logic:** Configured an alarm to trigger if `SUM(SecretAccessed) >= 1` within a 1-minute period.
* **Action:** The alarm publishes a message to an SNS Topic (`SecurityAlarms`), which forwards the alert to my verified email address.

### 5. Troubleshooting & Optimization
* **Issue:** The initial test failed to trigger the email.
* **Root Cause:** The alarm statistic was set to `Average` over 5 minutes. Since the event happened only once, the average was `0.003`, which was below the threshold of `1`.
* **Fix:** Changed the alarm statistic to `Sum` to count the *total* number of access attempts, resulting in immediate successful detection.

## 📸 Verification

1.  **Event Detection:** CloudTrail history verifying the API call was logged.
    <img width="1509" height="856" alt="Screenshot 2026-01-07 at 12 26 53 AM" src="https://github.com/user-attachments/assets/35475d4b-2672-49c5-bf00-58cb882d2ce6" /><br>

2.  **Metric Spike:** CloudWatch graph showing the detected security event.
    <img width="1512" height="807" alt="Screenshot 2026-01-07 at 1 17 03 AM" src="https://github.com/user-attachments/assets/a9cc6d90-158c-4cff-841f-e8e6329a1ec5" /><br>

3.  **Final Alert:** The email notification received in my inbox.
    <img width="1918" height="991" alt="Screenshot 2026-01-07 at 1 16 27 AM" src="https://github.com/user-attachments/assets/2be5cb6a-15da-4145-bae3-8d3e80c1fdd5" /><br>

## 🧠 Key Learnings
* **SIEM Fundamentals:** Built a basic Security Information and Event Management pipeline using cloud-native tools.
* **Statistical Accuracy:** Learned that choosing the right metric statistic (`Sum` vs `Average`) is critical for "rare" events like security breaches.
* **CloudTrail vs. CloudWatch:** Clarified that CloudTrail *records* the past, while CloudWatch *monitors* the present and triggers actions.
