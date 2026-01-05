# Enterprise Database Architecture: Amazon Aurora & EC2

## 🎯 Project Goal
To deploy a high-performance, cloud-native relational database architecture. Instead of a standard single-instance database, I provisioned an **Amazon Aurora (MySQL Compatible)** cluster and established a secure network connection to an **EC2 Web Server**, preparing the infrastructure for a scalable web application.

## ⚙️ Architecture Components
* **Amazon Aurora:** A relational database engine built for the cloud, compatible with MySQL but with 5x the performance.
* **Database Cluster:** Configured with a "Writer" instance for data entry and the capability for "Reader" replicas for high availability.
* **Amazon EC2:** A virtual server (`t3.micro`) acting as the host for the future web application.
* **VPC Security Groups:** Configured to allow secure internal traffic between the Web Server and the Database.<br>
  <img width="873" height="633" alt="Database 1" src="https://github.com/user-attachments/assets/87d8902e-1f62-4bbc-ade3-a7239150b87a" /><br>


## 🛠️ Implementation Steps

### 1. Compute Layer (The Web Server)
* **Action:** Launched an Amazon Linux 2023 instance to act as the application host.
* **Verification:** Confirmed the instance status was "Running" and public DNS was assigned.

### 2. Persistence Layer (The Cluster)
* **Service:** Amazon Aurora (MySQL Compatible).
* **Configuration:**
    * **Engine:** Aurora Standard.
    * **Instance Class:** Burstable classes (`db.t3.medium`) for cost-effective development testing.
    * **Dev/Test Template:** Optimized for non-production environments to minimize costs.

### 3. Network Connectivity (The "Glue")
* **Challenge:** The database and web server exist separately and cannot communicate by default.
* **Solution:** Utilized the RDS "Connect to EC2 compute resource" feature.
* **Result:** AWS automatically updated the **Security Group Inbound Rules** on the Aurora cluster to accept traffic *only* from the EC2 instance's Security Group ID on port 3306.

## 📸 Verification

1.  **Compute Resources:** EC2 Console showing the active Web Server instance.
    <img width="1511" height="829" alt="Screenshot 2026-01-03 at 10 54 15 PM" src="https://github.com/user-attachments/assets/a6bd5b9b-8b19-4c91-b52e-456f1d14a7c9" /><br>

2.  **Database Cluster Status:** RDS Console displaying the Aurora Cluster with "Available" status.
    <img width="1511" height="829" alt="Screenshot 2026-01-03 at 10 54 30 PM" src="https://github.com/user-attachments/assets/2bd901f0-ecbe-4c4d-acd3-5ddbebb08265" /><br>

3.  **Endpoint Configuration:** Verification of the "Writer" endpoint required for application connection.
    <img width="1511" height="829" alt="Screenshot 2026-01-03 at 10 54 45 PM" src="https://github.com/user-attachments/assets/dc7029f6-fbcf-4e65-a1b2-c2a6c431f32b" /><br>


## 🧠 Key Learnings
* **Aurora vs. RDS:** Learned that Aurora separates *Compute* (Instances) from *Storage* (Cluster Volume), allowing for faster replication and failover compared to standard RDS MySQL.
* **Dependency Management:** Recognized that the Compute resource (EC2) must be provisioned *before* the Database connection can be configured in the Wizard.
* **Security Groups as Firewalls:** Reinforced that "Connecting" resources in AWS is fundamentally about managing Security Group rules (Allowing Port 3306 from Source SG).
