# Cloud Security with AWS IAM

## 🎯 Project Goal
To secure a cloud environment by implementing the **Principle of Least Privilege**. I created a scoped "Developer" identity that can manage specific resources based on tags but is strictly forbidden from touching Production infrastructure.

## ⚙️ Security Architecture
* **Identity:** IAM User (`Intern`) managed via an IAM Group.
* **Policy:** Custom JSON policy enforcing **Tag-Based Access Control**.
* **Resource:** EC2 Instances tagged as `Env: Production` vs. `Env: Development`.<br>

  <img width="653" height="363" alt="Screenshot 2025-12-29 at 2 24 42 AM" src="https://github.com/user-attachments/assets/29cf8840-c5c5-4ab7-8187-d0f7f8ea8c7b" /><br>


## 🛠️ Implementation Steps

### 1. Environment Tagging
I launched two EC2 instances to simulate a real-world setup:
* **Prod Server:** Tagged `Env: Production`
* **Dev Server:** Tagged `Env: Development`

### 2. Custom Policy Creation (JSON)
Instead of using a default AWS policy (which is often too broad), I wrote a custom JSON policy.
* **Effect:** `Allow` EC2 actions.
* **Condition:** Actions are ONLY allowed if the resource tag `Env` equals `Development`.
* **Explicit Deny:** Protected critical tags from being removed or changed.

### 3. User & Group Management
* Created a **User Group** (`Intern`) and attached the custom policy.
* Created the **IAM User** and added them to the group.
* *Why:* Managing permissions via Groups is a scalable best practice compared to attaching policies directly to individual users.

## 📸 Verification

1.  **Policy Details:** the permissions defined in the policy.
    <img width="1512" height="855" alt="Screenshot 2025-12-29 at 1 51 24 AM" src="https://github.com/user-attachments/assets/ecae3172-9ec9-4cdb-850f-39cefdfc4bb2" /><br>
    
2.  **Access Denied:** the "Dev User" attempting to stop a "Production" instance and receiving an authorization error.
    <img width="1512" height="855" alt="Screenshot 2025-12-29 at 1 53 55 AM" src="https://github.com/user-attachments/assets/9386e4a9-a2db-421c-9ff2-bd3ac4c543fb" /><br>
    
3.  **Successful Action:** The same user was successfully able to stop the "Development" instance, verifying the permissions boundary is accurate.
    <img width="1512" height="855" alt="Screenshot 2025-12-29 at 2 04 07 AM" src="https://github.com/user-attachments/assets/98c8f62c-afe5-469f-8d4f-04cd940b5a59" /><br>

## 🧠 Key Learnings
* **Policies are the Firewall:** IAM is the first line of defense. A well-written policy can prevent accidents better than a manual process.
* **The Power of Tags:** Combining `Condition` blocks with Resource Tags allows for dynamic permission management (e.g., any new "Dev" server is automatically accessible to the Dev team).
* **Explicit Deny:** An explicit `Deny` in a policy always overrides an `Allow`, making it a powerful tool for protecting critical assets.
