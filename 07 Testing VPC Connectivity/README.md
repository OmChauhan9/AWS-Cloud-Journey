# Testing VPC Connectivity & Network Troubleshooting

## 🎯 Project Goal
To validate the integrity of the VPC network by testing connectivity paths (Public-to-Internet and Public-to-Private). The primary focus was identifying and resolving traffic blocking issues caused by **Stateful (SG)** vs. **Stateless (NACL)** firewalls.

## ⚙️ Test Scenarios
1.  **SSH Access:** Connecting from my local machine to the Public "Bastion" Server.
2.  **Internal Ping:** Testing reachability from the Public Server to the Private Server.
3.  **Internet Access:** Verifying the Public Server can fetch data from the web (`example.com`).

## 🛠️ Implementation & Troubleshooting

### 1. The SSH Challenge
* **Issue:** Initial connection to the Public Server failed.
* **Diagnosis:** The Security Group allowed HTTP (80) but blocked SSH (22).
* **Fix:** Updated the **Public Security Group** to allow `TCP Port 22` from `0.0.0.0/0`.

### 2. The "Silent Drop" (Ping Test)
* **Issue:** When running `ping 10.0.1.x` from the Public Server, the terminal hung (no response, no error).
* **Diagnosis:**
    1.  **Protocol Mismatch:** Ping uses **ICMP**, not TCP. I had to add `All ICMP` to the Security Groups.
    2.  **Stateless Firewall:** The **Network ACL** allowed the request *IN* but silently dropped the reply *OUT*.
* **Fix:** Added an **Outbound Rule** to the Private NACL allowing `All ICMP` traffic to return to the Public Subnet.

### 3. Verifying Internet Access
* **Command:** `curl example.com`
* **Result:** Successfully received HTML content, confirming the **Internet Gateway** and **Route Tables** are correctly configured for outbound traffic.

## 📸 Verification


1.  **SSH Terminal:** Screenshot confirming successful login to the Bastion Host.
    <img width="1512" height="857" alt="Screenshot 2025-12-29 at 11 47 52 PM" src="https://github.com/user-attachments/assets/0836a5eb-2991-4ebe-96ce-cb51bca2de26" /><br>

2.  **Ping Success:** Terminal showing continuous ICMP replies from the Private Server.
    <img width="1512" height="857" alt="Screenshot 2025-12-29 at 11 53 41 PM" src="https://github.com/user-attachments/assets/aa80ddbf-f7c1-4727-83fa-2efac025ef63" /><br>

3.  **Curl Output:** Terminal showing HTML data fetched from an external domain.
    <img width="1512" height="857" alt="Screenshot 2025-12-29 at 11 54 36 PM" src="https://github.com/user-attachments/assets/bc83c9c0-206a-4df5-8cbc-bf381f8cb604" /><br>


## 🧠 Key Learnings
* **Protocols Matter:** Opening Port 80 (HTTP) does not enable Ping (ICMP). They are distinct languages.
* **The "Hang" vs. "Refused":** A "Connection Refused" error usually means the server is down. A "Hang" (timeout) almost always means a **Firewall (SG or NACL)** is dropping packets.
* **Statelessness:** This project reinforced that **NACLs** do not automatically allow return traffic—you must explicitly build the return path.
