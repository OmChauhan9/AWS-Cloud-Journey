# Secure S3 Access with VPC Gateway Endpoints

## 🎯 Project Goal
To secure data transfer between the VPC and Amazon S3. I replaced the public internet route with a **VPC Gateway Endpoint**, ensuring traffic stays within the AWS network. I verified this by implementing a **Bucket Policy** that denies all access attempts not originating from this specific private endpoint.

## ⚙️ Architecture Components
* **VPC Gateway Endpoint:** A virtual device that routes traffic to S3/DynamoDB privately without using an Internet Gateway or NAT Device.
* **Prefix List (`pl-xxx`):** A dynamic list of IP address ranges for AWS services, managed automatically by AWS.
* **S3 Bucket Policy:** A resource-based policy used to enforce the "VPC Endpoint Only" restriction.<br>

  <img width="1075" height="629" alt="architecture-today" src="https://github.com/user-attachments/assets/2969554a-8358-406f-a145-3c6855f7425c" /><br>


## 🛠️ Implementation Steps

### 1. Creating the Private Tunnel (Endpoint)
* Deployed a **Gateway Endpoint** for the S3 service in the `us-east-1` region.
* Associated it with the VPC's Route Table.
* **Result:** AWS automatically added a route sending all S3-bound traffic (`pl-xxxx`) to the endpoint (`vpce-xxxx`).

### 2. The Security Hardening (Bucket Policy)
I implemented a "Zero Trust" policy on the S3 bucket.
* **Action:** `Deny All`.
* **Condition:** `StringNotEquals` -> `aws:SourceVpce`: `vpce-my-id`.
* **Effect:** If a request comes from the Public Internet (even from me), it is blocked. If it comes from the VPC Endpoint, it is allowed.

### 3. Verification & Testing
* **Console Test:** Attempted to view files via the AWS Console (Browser). -> **BLOCKED** (As expected).
* **CLI Test:** Attempted to list files via the EC2 Instance. -> **ALLOWED**.
* **Conclusion:** The architecture successfully discerns the source of traffic and enforces the security boundary.

## 📸 Verification

1.  **Route Table:** Screenshot showing the `pl-` prefix list route targeting the Endpoint.
    <img width="1512" height="859" alt="Screenshot 2025-12-31 at 2 22 21 AM" src="https://github.com/user-attachments/assets/2b086597-fa55-4284-93db-6a4ed2f15e13" /><br>

2.  **Bucket Policy:** JSON policy showing the conditional access restriction.
    <img width="1512" height="642" alt="Screenshot 2025-12-31 at 2 22 59 AM" src="https://github.com/user-attachments/assets/044f2869-21c3-43c0-952c-ae705b29825d" /><br>
    
3.  **Terminal Success:** CLI output proving the instance retains access despite the strict policy.
    <img width="1512" height="859" alt="Screenshot 2025-12-31 at 2 23 20 AM" src="https://github.com/user-attachments/assets/682e9232-3d6b-4632-8fe7-8ecd270c1118" /><br>


## 🧠 Key Learnings
* **Gateway vs. Interface:** Learned that S3 and DynamoDB use **Gateway** endpoints (Free, Route Table-based), while other services use **Interface** endpoints (ENI-based, Cost money).
* **The "Console Lockout":** Realized that applying a "VPC Endpoint Only" policy locks *me* out of the S3 Console because my laptop is not inside the VPC.
* **Cost Optimization:** Gateway Endpoints are free! This is a cheaper way to access S3 from a private subnet compared to using a NAT Gateway.
