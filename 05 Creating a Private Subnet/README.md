# Project: Creating a Private Subnet

## 🎯 Project Goal
To implement a "Zero Trust" network foundation by creating a **Private Subnet** that is completely isolated from the public internet. The goal was to configure routing and firewalls (NACLs) to strictly control traffic flow.

## ⚙️ Architecture Stats
* **VPC CIDR:** `10.0.0.0/16`
* **Private Subnet CIDR:** `10.0.1.0/24`
* **Availability Zone:** `us-east-1a`
* **Internet Access:** **None** (No Internet Gateway attached)

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
*Proof of configuration can be found in the `/screenshots` folder.*

1.  **Routing Table Proof:** Screenshot shows the absence of an `igw-xxxxx` target, verifying total isolation.
2.  **Subnet Configuration:** Screenshot confirms the specific CIDR block and correct route table association.
3.  **Security Layer:** Screenshot of the NACL showing the explicit traffic rules.

## 🧠 Key Learnings
* **Isolation is Routing:** A subnet is only "private" if its Route Table says so. IP settings alone are not enough.
* **NACL vs. Security Groups:** I learned that Network ACLs act as a "Subnet Firewall" (Stateless), providing an extra layer of security before traffic even reaches the instance.
* **Implicit Associations:** I had to explicitly associate my subnet with the new Route Table to break the link with the VPC's main public table.
