# Network Monitoring with VPC Flow Logs & CloudWatch

## 🎯 Project Goal
To implement observability into the cloud network. By enabling **VPC Flow Logs**, I captured real-time data on inbound and outbound traffic and used **Amazon CloudWatch Logs Insights** to query and visualize network patterns (e.g., identifying top talkers or blocked traffic).

## ⚙️ Architecture Components
* **VPC Flow Logs:** The "CCTV" system capturing packet metadata (Source IP, Destination IP, Action).
* **Amazon CloudWatch:** The central repository for storing log data.
* **IAM Role:** A custom role granting the VPC service permission to write logs to CloudWatch.
* **Logs Insights:** An interactive query tool used to analyze log data.<br>

  <img width="961" height="628" alt="Screenshot 2025-12-30 at 4 11 00 PM" src="https://github.com/user-attachments/assets/f81d9d3a-4ff6-400b-95be-fc81a795ab61" /><br>


## 🛠️ Implementation Steps

### 1. Infrastructure Setup (Traffic Source)
* Re-deployed the "Multi-VPC" architecture (Peered VPCs) to generate legitimate cross-network traffic for analysis.

### 2. Configuring Permissions (IAM)
* **Challenge:** The VPC service cannot write to CloudWatch by default.
* **Solution:** Created a custom **IAM Role** with a Trust Policy allowing `vpc-flow-logs.amazonaws.com` to assume it.
* **Policy:** Granted permissions for `CreateLogStream` and `PutLogEvents`.

### 3. Enabling Flow Logs
* Activated Flow Logs at the VPC level.
* **Filter:** Set to `All` (capturing both `ACCEPT` and `REJECT` traffic).
* **Destination:** Targeted the `aws-task9-lg` in CloudWatch.

### 4. Traffic Analysis (The Investigation)
* **Action:** Generated traffic by pinging between instances.
* **Analysis:** Used **CloudWatch Logs Insights** to run queries.
* **Query Example:**
    ```sql
    stats count(*) by action, srcAddr
    ```
* **Result:** Successfully visualized the volume of accepted vs. rejected traffic.

## 📸 Verification


1.  **Flow Log Status:** Screenshot confirming the Flow Log is "Active" in the VPC Console.
    <img width="1511" height="855" alt="Screenshot 2025-12-30 at 2 18 34 AM" src="https://github.com/user-attachments/assets/10ed88c8-8c7e-441c-a5c8-dd7e5c3eb365" /><br>

2.  **Raw Logs:** CloudWatch Log Stream showing detailed packet information (IPs, Ports, Protocols).
    <img width="1511" height="855" alt="Screenshot 2025-12-30 at 2 19 06 AM" src="https://github.com/user-attachments/assets/c1b8d607-73fb-4b9c-835e-4e3ca3819a26" /><br>

3.  **Data Visualization:** Logs Insights graph showing traffic volume analysis.
    <img width="1511" height="855" alt="Screenshot 2025-12-30 at 2 19 24 AM" src="https://github.com/user-attachments/assets/dcd059df-30f8-475c-acdf-3b6d605b765b" /><br>


## 🧠 Key Learnings
* **Metadata vs. Content:** Flow Logs capture *metadata* (who talked to whom, on what port), but NOT the actual *content* of the packet (the message itself).
* **Troubleshooting Power:** Flow Logs are the primary tool for debugging Security Groups. If a connection fails, Flow Logs will explicitly show a `REJECT` record.
* **IAM Trust Policies:** Learned that services (like VPC) need explicit "Trust Relationships" to perform actions on your behalf.
