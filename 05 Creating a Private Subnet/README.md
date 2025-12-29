[Private subnet.drawio](https://github.com/user-attachments/files/24364207/Private.subnet.drawio)# Creating a Private Subnet

## 🎯 Project Goal
To implement a "Zero Trust" network foundation by creating a **Private Subnet** that is completely isolated from the public internet. The goal was to configure routing and firewalls (NACLs) to strictly control traffic flow.

## ⚙️ Architecture Stats
* **VPC CIDR:** `10.0.0.0/16`
* **Private Subnet CIDR:** `10.0.1.0/24`
* **Availability Zone:** `us-east-1a`
* **Internet Access:** **None** (No Internet Gateway attached)<br>

<img width="976" height="621" alt="Screenshot 2025-12-28 at 10 47 05 PM" src="https://github.com/user-attachments/assets/c6954f33-9c90-41e5-b279-fd0780e0955a" />

## 🛠️ Implementation Steps

### 1. The "Hidden" Subnet
I created a subnet specifically designed for sensitive workloads (like Databases).
* **Configuration:** Unlike standard subnets, I disabled "Auto-assign Public IP".
* **Result:** Instances launched here have no public addressable identity.

### 2. Custom Route Table (The Logic)
The defining feature of a private subnet is its routing.
* I created a custom Route Table: `aws-task5-private-rt`
* **The Critical Step:** I explicitly **did not** add a route to the Internet Gateway (`0.0.0.0/0`).
* **Traffic Flow:** The route table only allows `10.0.0.0/16 -> local`, meaning resources can talk to the VPC, but the internet cannot see them.

### 3. Network ACLs (The Firewall)
To implement **Defense in Depth**, I replaced the default "Allow All" Network ACL with a custom one.
* **Resource:** `aws-task5-private-nacl`
* **Rule Set:** Configured with a default **DENY** posture to act as a strict boundary for the subnet.

## 📸 Verification
<img width="1480" height="286" alt="Screenshot 2025-12-28 at 5 02 48 PM" src="https://github.com/user-attachments/assets/4f5b43d3-0457-442d-bd0d-beadba7960b5" /><br>


1.  **Routing Table Proof:** Screenshot shows the absence of an `igw-xxxxx` target, verifying total isolation.
   <img width="1512" height="810" alt="Screenshot 2025-12-28 at 5 28 25 PM" src="https://github.com/user-attachments/assets/40a63253-2ee5-431a-9c9e-7a1cd19a1aba" /><br>

2.  **Subnet Configuration:** Screenshot confirms the specific CIDR block and correct route table association.
   <img width="1512" height="810" alt="Screenshot 2025-12-28 at 5 28 04 PM" src="https://github.com/user-attachments/assets/bbd910e9-ebce-4cbe-8062-a2b7bd41a05c" /><br>

3.  **Security Layer:** Screenshot of the NACL showing the explicit traffic rules.
   <img width="1512" height="810" alt="Screenshot 2025-12-28 at 5 28 45 PM" src="https://github.com/user-attachments/assets/0e885b4b-f125-46e8-8d68-78d872a931ca" /><br>
   

## 🧠 Key Learnings
* **Isolation is Routing:** A subnet is only "private" if its Route Table says so. IP settings alone are not enough.
* **NACL vs. Security Groups:** I learned that Network ACLs act as a "Subnet Firewall" (Stateless), providing an extra layer of security before traffic even reaches the instance.
* **Implicit Associations:** I had to explicitly associate my subnet with the new Route Table to break the link with the VPC's main public table.
