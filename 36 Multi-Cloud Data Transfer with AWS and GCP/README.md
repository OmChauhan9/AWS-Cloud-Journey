# Multi-Cloud Data Transfer System (AWS ↔ GCP) ☁️☁️

## 🎯 Project Goal
To implement a robust **Multi-Cloud Disaster Recovery** strategy. I built an automated pipeline that transfers and backs up data from **Amazon S3** to **Google Cloud Storage (GCS)** without using insecure long-term access keys.

## ⚙️ Architecture Components
* **AWS S3:** The primary storage solution hosting the source data.
* **Google Cloud Storage (GCS):** The secondary/backup storage solution.
* **GCP Storage Transfer Service:** The managed service that orchestrates the data movement between clouds.
* **Identity Federation:** A passwordless authentication method allowing GCP to securely assume an IAM Role within AWS.
* **Manifest Files:** A CSV-based control mechanism for selective data transfer.<br>

  <img width="1054" height="590" alt="Dev 9" src="https://github.com/user-attachments/assets/2d208e3e-74a9-4e52-a801-319b05546514" /><br>


## 🛠️ Implementation Steps

### 1. Cross-Cloud Authentication (The Hard Part)
* **Challenge:** Connecting two rival cloud providers securely.
* **Solution:** configured **Workload Identity Federation**. I retrieved the unique **Subject ID** of my GCP Service Agent and used it to craft a **Custom Trust Policy** in AWS IAM.
* **Result:** GCP can now request temporary access credentials from AWS STS (Security Token Service) only for the duration of the transfer.

### 2. Infrastructure Setup
* **Source:** Provisioned an S3 bucket in `us-east-1` populated with critical project documentation.
* **Destination:** Provisioned a GCS bucket in `us-west4` with a Standard storage class for immediate availability.

### 3. Automated Transfer Execution
* **Job Creation:** Configured a GCP Transfer Job to pull objects from the S3 source.
* **Execution:** Verified the transfer speed and integrity (checksum validation).
* **Selective Transfer:** Implemented a **Manifest File (CSV)** to demonstrate granular control, successfully transferring only specific high-priority documents rather than the entire bucket.

## 📸 Evidence

1.  **Trust Configuration:** The AWS IAM Role allowing Google Federation.
    <img width="1512" height="859" alt="Screenshot 2026-01-19 at 4 23 54 PM" src="https://github.com/user-attachments/assets/e7171ffe-a7e6-41e7-ae58-a68685e651c4" /><br>

2.  **Multi-Cloud View:** Side-by-side view of the same files existing in both AWS S3 and GCS.
    <img width="1512" height="859" alt="Screenshot 2026-01-19 at 4 57 59 PM" src="https://github.com/user-attachments/assets/383e5a4a-5319-4898-bc32-4bee815adf41" /><br>

## 🧠 Key Learnings
* **Federation > Keys:** I learned that modern cloud security relies on "Roles" and "Trust," not "Keys" and "Passwords."
* **Interoperability:** Gained hands-on experience with how different cloud providers (AWS vs. GCP) speak the same language (Object Storage) but use different dialects (S3 vs. GCS).
* **Disaster Recovery:** Practical implementation of the "3-2-1 Backup Rule" using a secondary cloud provider as the offsite backup location.
