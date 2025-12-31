# VPC Peering

## 🎯 Project Goal
To simulate a large-scale organizational network by creating two separate Virtual Private Clouds (VPCs) and connecting them securely using **VPC Peering**. The goal is to allow private communication between them without using the public internet.

## ⚙️ Architecture Components
* **VPC 1:** `10.1.0.0/16` (The Requester).
* **VPC 2:** `10.2.0.0/16` (The Accepter).
* **VPC Peering Connection:** A direct network route connecting the two VPCs.
* **Elastic IP:** Used to restore public connectivity to an EC2 instance.<br>

  <img width="1038" height="650" alt="Screenshot 2025-12-30 at 3 58 55 PM" src="https://github.com/user-attachments/assets/4a0c3809-085b-4eb8-a98c-d394cb4b5a97" /><br>


## 🛠️ Implementation Steps

### 1. Multi-VPC Setup
I deployed two distinct VPCs with non-overlapping CIDR blocks.
* **Why Non-Overlapping?** If both VPCs used `10.0.0.0/16`, routing would be impossible because the router couldn't distinguish between "Local" and "Remote" traffic.

### 2. Establishing the Peering Connection
* **Initiation:** Sent a peering request from VPC 1 to VPC 2.
* **Acceptance:** Manually accepted the request in VPC 2.
* **Routing:** Updated the **Route Tables** in *both* VPCs to point traffic destined for the other VPC to the `pcx-xxxxx` (Peering Connection) target.

### 3. Troubleshooting Connectivity
During the EC2 launch, I encountered a connectivity error because the instance lacked a Public IP.
* **Fix:** I allocated an **Elastic IP (EIP)** and associated it with the instance.
* **Validation:** Used `ping` to verify that Instance 1 (VPC 1) could talk to Instance 2 (VPC 2) using only Private IPs.

## 📸 Verification


1.  **Peering Status:** Screenshot showing the Peering Connection in "Active" state.
    <img width="1511" height="855" alt="Screenshot 2025-12-30 at 1 28 51 AM" src="https://github.com/user-attachments/assets/10c0231a-1ecd-40a1-82ba-aec82d02b064" /><br>

2.  **Route Configuration:** Screenshot of the Route Table showing the specific route to the peer VPC.
    <img width="1511" height="855" alt="Screenshot 2025-12-30 at 1 29 21 AM" src="https://github.com/user-attachments/assets/fcca49d9-0fc2-40a2-a968-4d820d7f963a" /><br>
    <img width="1511" height="855" alt="Screenshot 2025-12-30 at 1 29 53 AM" src="https://github.com/user-attachments/assets/88159cab-c239-4cc8-b5f2-a00c5abff62d" /><br>

3.  **Connectivity Test:** Terminal screenshot showing successful ICMP packets (Ping) flowing between VPCs.
    <img width="1511" height="855" alt="Screenshot 2025-12-30 at 1 30 30 AM" src="https://github.com/user-attachments/assets/55a59628-39c6-40bc-9fe7-7e9b981ac34e" /><br>
    <img width="1511" height="855" alt="Screenshot 2025-12-30 at 1 31 01 AM" src="https://github.com/user-attachments/assets/0a5ccc15-85ab-41bc-b94c-638f03de2ca0" /><br>


## 🧠 Key Learnings
* **Peering is Private:** Traffic over a peering connection never traverses the public internet, making it faster and more secure.
* **Routing is Key:** Creating the connection isn't enough; you must explicitly update route tables in **both** directions (VPC A to B, and VPC B to A).
* **Security Groups:** For `ping` to work, the destination Security Group must explicitly allow **ICMP** traffic from the source VPC's CIDR block.
