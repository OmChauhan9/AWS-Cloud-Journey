# Launching VPC Resources

## 🎯 Project Goal
To deploy compute resources (EC2) into a custom VPC architecture, establishing a secure "Bastion Host" pattern. The goal was to ensure the Private Instance is completely inaccessible from the internet and can only be managed via the Public Instance.

## ⚙️ Architecture Components
* **Public Instance (Bastion):** Acts as the secure gateway (Jump Box).
* **Private Instance (Internal):** Simulates a sensitive database or backend server.
* **Security Group Chaining:** A firewall rule where the "Source" is another Security Group, not an IP address.<br>

  <img width="1013" height="647" alt="Screenshot 2025-12-30 at 3 32 15 PM" src="https://github.com/user-attachments/assets/d09676c6-9a69-498a-8ea6-0bf3b03825a8" /><br>


## 🛠️ Implementation Steps

### 1. Launching the Public Server
I deployed an Amazon Linux 2023 instance into the Public Subnet.
* **Network:** Auto-assign Public IP = **Enable**.
* **Security:** Allowed SSH (Port 22) from `0.0.0.0/0` (Anywhere) so I can log in.

### 2. Launching the Private Server
I deployed a second instance into the Private Subnet.
* **Network:** Auto-assign Public IP = **Disable**.
* **Security:** This was the critical step. I did NOT allow any IP addresses.

### 3. Implementing Security Group Chaining
Instead of using IP ranges (CIDRs), I used **Logical Referencing**.
* **Rule:** In the Private Security Group, I set the Inbound SSH Source to be the **Public Security Group ID** (`sg-xxxxxx`).
* **Result:** The Private Server explicitly trusts *only* traffic coming from the Public Server. Even if someone knew the Private IP, they couldn't connect unless they were standing on the Public Server.

## 📸 Verification


1.  **Instance Status:** Both Public and Private instances in "Running" state.
    <img width="1512" height="299" alt="Screenshot 2025-12-29 at 11 36 46 PM" src="https://github.com/user-attachments/assets/22772b50-792b-496f-a3c7-e4a19d559f41" /><br>

2.  **SG Chaining:** Private Security Group rules proving the Source is set to the Public SG ID.
    <img width="1512" height="607" alt="Screenshot 2025-12-29 at 11 37 48 PM" src="https://github.com/user-attachments/assets/15803bca-0f8f-467e-a930-e58b1105bcd9" /><br>

3.  **Topology Map:** VPC Resource Map showing instances residing in their respective isolated subnets.
    <img width="1512" height="540" alt="Screenshot 2025-12-29 at 11 38 11 PM" src="https://github.com/user-attachments/assets/b7c54d60-2ec0-4a6f-bcc3-4a5b0c6db831" /><br>


## 🧠 Key Learnings
* **Bastion Host Pattern:** Learned that private servers need a "Jump Box" to be managed, as they have no direct internet connectivity.
* **SG Chaining vs. CIDR:** Referencing a Security Group ID is safer than referencing IP addresses because it works dynamically even if the Public Server's IP changes.
* **Tenancy:** Understood that "Default" tenancy means sharing hardware with other AWS customers, while "Dedicated" is for compliance needs.
