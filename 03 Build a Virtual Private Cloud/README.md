# Project: Build a Virtual Private Cloud (VPC)

## 🎯 Project Goal
To establish a custom, isolated network environment in AWS, moving away from the "Default VPC" to gain full control over IP addressing, subnets, and external connectivity.

## ⚙️ Architecture Components
* **VPC:** `10.0.0.0/16` (The isolated network container).
* **Subnet:** `10.0.0.0/24` (The "Public" neighborhood).
* **Internet Gateway:** Attached to allow communication with the outside world.<br>

  <img width="831" height="433" alt="Screenshot 2025-12-29 at 1 22 14 AM" src="https://github.com/user-attachments/assets/a4c1510e-31a5-4c01-b332-5e8557402b80" />


## 🛠️ Implementation Steps

### 1. Defining the Network (VPC Creation)
I created a custom VPC to host my infrastructure.
* **CIDR Block:** Chosen `10.0.0.0/16` to allow for up to 65,536 private IP addresses.
* **Tenancy:** Default (Shared hardware).

### 2. Carving Out a Subnet
Inside the VPC, I created a specific sub-network for resources.
* **Zone:** `us-east-1a` (Fixed Availability Zone for high availability planning).
* **CIDR:** `10.0.0.0/24` (Allocating 256 IPs for this specific subnet).

### 3. Enabling Public Connectivity
To ensure future servers in this subnet can be reached from the internet:
* **Action:** Enabled **"Auto-assign public IPv4 address"** on the subnet.
* **Infrastructure:** Created and attached an **Internet Gateway (IGW)** to the VPC.

## 📸 Verification

1.  **Resource Map:** Screenshot showing the visual relationship between the VPC, Subnet, and IGW.
   <img width="1496" height="394" alt="Screenshot 2025-12-29 at 1 07 54 AM" src="https://github.com/user-attachments/assets/538c822d-f81a-48f1-b9d7-67302c2d122b" /><br>
   <img width="1512" height="857" alt="Screenshot 2025-12-29 at 1 16 57 AM" src="https://github.com/user-attachments/assets/c801e2b5-393d-4d29-8e0c-706848d1bdf5" /><br>

2.  **Subnet Settings:** Proof that "Auto-assign Public IP" is enabled.
   <img width="1512" height="857" alt="Screenshot 2025-12-29 at 1 11 16 AM" src="https://github.com/user-attachments/assets/851163a0-e92f-4167-bf0a-741b4ad19964" /><br>

## 🧠 Key Learnings
* **CIDR Math:** Learned that a `/16` network is the "City" and a `/24` is a "Neighborhood" inside it.
* **The "Gateway" Concept:** A VPC is private by default. It physically cannot talk to the internet without an Internet Gateway attachment.
* **Regional Isolation:** VPCs belong to a specific AWS Region (e.g., N. Virginia) and span all Availability Zones, but Subnets must live in *one* specific Zone.
