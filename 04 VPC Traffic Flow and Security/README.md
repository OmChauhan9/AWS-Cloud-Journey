# VPC Traffic Flow & Security

## 🎯 Project Goal
To configure the "nervous system" of the Virtual Private Cloud (VPC) by establishing internet connectivity via Route Tables and implementing a defense-in-depth security strategy using both Security Groups and Network ACLs.

## ⚙️ Architecture Components
* **Traffic Control:** Custom Route Table pointing to an Internet Gateway.
* **Instance Security:** Security Group acting as a **Stateful Firewall** (allowing Web & SSH).
* **Subnet Security:** Network ACL (NACL) acting as a **Stateless Firewall** for traffic filtering.<br>

  <img width="828" height="538" alt="Screenshot 2025-12-29 at 12 22 59 AM" src="https://github.com/user-attachments/assets/52780910-b9dd-4be4-bfb1-0aca72f62087" />


## 🛠️ Implementation Steps

### 1. Enabling Internet Traffic (The "Pipes")
A subnet is only public if it has a path to the internet.
* **Action:** I configured a Route Table to direct all external traffic (`0.0.0.0/0`) to the **Internet Gateway** (`igw-xxxxx`).
* **Result:** Resources in this subnet can now receive public internet requests.

### 2. Configuring the Security Group (The "Doorman")
I set up a Security Group to act as the primary firewall for the EC2 instances.
* **Rule:** Allowed **HTTP (Port 80)** from `Anywhere`.
* **Concept:** Security Groups are **Stateful**. By allowing the request *in*, the response is automatically allowed *out*.

### 3. Configuring Network ACLs (The "Perimeter Fence")
I added an extra layer of security at the subnet level.
* **Action:** Created a Custom NACL with Rule #100.
* **Concept:** NACLs are **Stateless**. I learned that unlike Security Groups, I must explicitly allow return traffic if I want it to pass.

## 📸 Verification

<img width="1496" height="394" alt="Screenshot 2025-12-29 at 12 31 02 AM" src="https://github.com/user-attachments/assets/914abd34-01cb-4648-887c-8cfa82976b16" /><br>


1.  **Public Routing:** the Route Table has an active path to the Internet Gateway.
   <img width="1510" height="854" alt="Screenshot 2025-12-29 at 12 11 27 AM" src="https://github.com/user-attachments/assets/ef7f4d76-866b-4e1c-b6e0-2b33c782a53f" /><br>
   
2.  **Security Rules:** the Security Group Inbound rules permitting web traffic.
   <img width="1510" height="854" alt="Screenshot 2025-12-29 at 12 11 59 AM" src="https://github.com/user-attachments/assets/df40f1e6-bf24-40b5-b7d5-72fb1377111d" /><br>
   
3.  **NACL Logic:** the specific Inbound/Outbound rulesets applied to the subnet.
   
    <img width="1510" height="854" alt="Screenshot 2025-12-29 at 12 12 53 AM" src="https://github.com/user-attachments/assets/3eec41cb-a852-402b-87cc-7cfb6615f9dd" />
    <img width="1510" height="854" alt="Screenshot 2025-12-29 at 12 12 58 AM" src="https://github.com/user-attachments/assets/5ba639d7-ca0c-4a3b-94aa-3219c185b9d6" /><br>


## 🧠 Key Learnings
* **Route Tables are Maps:** Without a route to `0.0.0.0/0`, an Internet Gateway is useless. The Route Table bridges the gap.
* **Defense in Depth:** Using both SGs and NACLs ensures that if one layer fails (e.g., a permissive SG), the other (NACL) can still block malicious traffic.
* **The "Stateful" Advantage:** Security Groups are easier to manage because they handle return traffic automatically, whereas NACLs require strict management of both directions.
