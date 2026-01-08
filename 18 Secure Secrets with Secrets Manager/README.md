# Secure Secrets with Secrets Manager

## 🎯 Project Goal
To refactor a legacy application that insecurely stored AWS credentials in plain text. I migrated the sensitive data to **AWS Secrets Manager**, implemented **GitHub Push Protection** to prevent future leaks, and performed a **Git Rebase** to scrub compromised credentials from the version control history.

## ⚙️ Architecture Components
* **AWS Secrets Manager:** A service to encrypt, store, and retrieve database credentials and API keys.
* **GitHub Secret Scanning:** A proactive security feature that blocks commits containing recognizable secret patterns.
* **Python (Boto3):** The AWS SDK used to programmatically fetch secrets at runtime.
* **Git Rebase:** An advanced version control command used to rewrite commit history and remove traces of sensitive data.<br>

  <img width="1512" height="1272" alt="image" src="https://github.com/user-attachments/assets/4eb868e6-5f10-41c8-9689-fd0097e12ecc" /><br>

## 🛠️ Implementation Steps

### 1. The Vulnerability Simulation
* **Action:** Deliberately hardcoded valid AWS Access Keys into a `config.py` file to simulate a common developer error.
* **The Guardrail:** Attempted to push this code to GitHub.
* **Result:** **Blocked.** GitHub's Secret Scanning feature detected the `AKIA...` pattern and rejected the push, demonstrating an effective "Shift Left" security control.

### 2. Centralized Secret Storage (AWS CLI)
* **Solution:** Moved the credentials out of the codebase and into a secure vault.
* **Execution:** Used the AWS CLI to create a new secret entry.
    ```bash
    aws secretsmanager create-secret --name "aws-access-key-task18" --secret-string file://creds.json
    ```
* **Benefit:** Credentials are now encrypted at rest and can be rotated without touching the application code.

### 3. Application Refactoring
* **Action:** Rewrote the application logic (`app.py`) to remove the hardcoded strings.
* **Implementation:** Integrated the `boto3` library to authenticate with AWS and call the `get_secret_value` API.
* **Outcome:** The application now requests permission to access the keys at runtime, rather than owning the keys itself.

### 4. History Sanitization
* **Challenge:** Even after deleting the keys from the file, they remained in the Git Commit History.
* **Remediation:** Performed an interactive rebase (`git rebase -i --root`).
* **Action:** "Dropped" the specific commit containing the leak, effectively rewriting the timeline to ensure the keys never existed in the repo.

## 📸 Verification

1.  **Push Protection:** Terminal output showing GitHub blocking the insecure commit.
    <img width="1512" height="944" alt="Screenshot 2026-01-08 at 12 14 54 AM" src="https://github.com/user-attachments/assets/f9a61b87-7339-4957-bdb4-9b714dc5429b" /><br>

2.  **Secret Vault:** AWS Secrets Manager console showing the active secret.
    <img width="1512" height="856" alt="Screenshot 2026-01-08 at 12 19 11 AM" src="https://github.com/user-attachments/assets/e4140b7b-4cc8-49d9-b4dc-65b8a5ca8812" /><br>

3.  **Secure Code:** Python code snippet demonstrating programmatic secret retrieval.
    <img width="1509" height="794" alt="Screenshot 2026-01-08 at 12 20 38 AM" src="https://github.com/user-attachments/assets/12f34aa8-5b8d-45ca-a50d-1a3edfa469b9" /><br>

## 🧠 Key Learnings
* **Secret Sprawl:** Hardcoded credentials are the #1 cause of cloud breaches. Centralized management is mandatory for production.
* **Shift Left Security:** Tools like GitHub Secret Scanning protect developers from themselves by catching errors *before* they reach the repository.
* **Git Internals:** Understanding that "deleting a file" does not "delete the history," and learning how to use Rebase to perform deep cleaning of a repository.
