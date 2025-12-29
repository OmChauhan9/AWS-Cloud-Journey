# Host a Static Website on Amazon S3

## 🎯 Project Goal
To deploy a high-availability static website using **Amazon S3**, configuring it to be publicly accessible to users worldwide while correctly managing access permissions.

## ⚙️ Architecture Components
* **Amazon S3:** Object storage used to host the HTML/CSS assets.
* **Static Website Hosting:** S3 feature that turns a storage bucket into a web server.
* **Bucket Policy:** JSON document controlling access rights (Public Read).<br>

  <img width="682" height="201" alt="Screenshot 2025-12-29 at 2 19 32 PM" src="https://github.com/user-attachments/assets/f82442df-5249-4fd1-8e2a-2dff8c66e4d7" /><br>


## 🛠️ Implementation Steps

### 1. Bucket Creation & Configuration
* Created a unique S3 bucket in the `us-east-1` region.
* Uploaded `index.html` and assets to the root directory.

### 2. Enabling Static Hosting
* Activated the **Static Website Hosting** feature in the bucket properties.
* **Result:** Generated a specific S3 website endpoint URL (`http://...s3-website...`).

### 3. Security & Permissions Configuration
By default, S3 buckets are private and block all public access. To enable the website:
* **Step A:** I disabled "Block All Public Access" settings to open the gateway.
* **Step B:** I applied a **Bucket Policy** to explicitly grant `s3:GetObject` permission to `Principal: *` (Everyone).
* *Note:* This step is critical; without the policy, the "Block Public Access" setting alone is not enough to serve traffic.

## 📸 Verification

1.  **Live Site:** Screenshot of the browser rendering the HTML file via the S3 Endpoint.
    <img width="1510" height="856" alt="Screenshot 2025-12-29 at 2 15 24 PM" src="https://github.com/user-attachments/assets/c9868c97-7dde-4888-905e-4645d8eb3491" /><br>

2.  **Permissions:** Proof that Public Access blocking was correctly toggled to "Off".
    <img width="1510" height="856" alt="Screenshot 2025-12-29 at 2 15 37 PM" src="https://github.com/user-attachments/assets/2cba3c47-0406-47a3-9273-9e2375dbd546" /><br>


## 🧠 Key Learnings
* **Bucket vs. Object Permissions:** Unblocking "Public Access" at the bucket level isn't enough; you must also add a Bucket Policy to actually allow traffic.
* **Endpoints:** S3 Website endpoints (`http`) are different from standard API endpoints (`https`).
* **Global Namespace:** Learned that S3 bucket names must be globally unique across all AWS accounts.
