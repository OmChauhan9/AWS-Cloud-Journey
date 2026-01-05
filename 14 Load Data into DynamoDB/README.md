# Serverless Data Engineering: Amazon DynamoDB & AWS CloudShell

## 🎯 Project Goal
To implement a "Serverless" NoSQL database architecture using **Amazon DynamoDB**. Unlike previous relational database projects, this project focused on **schema flexibility** and **high-performance data ingestion**. I used **AWS CloudShell** to simulate a real-world Data Engineering task: batch-loading raw JSON data into a live database environment.

## ⚙️ Architecture Components
* **Amazon DynamoDB:** A fully managed, serverless Key-Value NoSQL database.
* **AWS CloudShell:** A browser-based shell with AWS CLI pre-installed, used for automation.
* **JSON:** The data format used for the source files (`ContentCatalog.json`, `Forum.json`).
* **Partition Keys:** The unique identifiers used to distribute data across physical partitions for speed.<br>

  <img width="966" height="452" alt="Database 3" src="https://github.com/user-attachments/assets/afefcb34-e13e-42f8-aaca-95034e62568b" /><br>


## 🛠️ Implementation Steps

### 1. Database Provisioning (Console & CLI)
* **Manual Setup:** Created the initial `aws-task13-db` table via the Console to understand the settings (Partition Keys, Capacity Units).
* **Automated Setup:** Leveraged **AWS CLI** within CloudShell to programmatically create four additional tables (`ContentCatalog`, `Forum`, `Post`, `Comment`) instantly.

### 2. Capacity Planning (Cost Optimization)
* **Challenge:** DynamoDB scales automatically, which can incur costs if unchecked.
* **Solution:** Manually configured **Provisioned Capacity** to 1 RCU (Read Capacity Unit) and 1 WCU (Write Capacity Unit) and disabled Auto-Scaling to strictly adhere to the AWS Free Tier limits.

### 3. Data Ingestion Pipeline
* **Source:** Downloaded a zipped dataset of JSON files from S3 using `wget`.
* **Processing:** Unzipped and inspected the data structure using Linux commands (`ls`, `cat`).
* **Ingestion:** Executed the `aws dynamodb batch-write-item` command to parse the JSON files and bulk-insert records into the database.

### 4. NoSQL Structure Analysis
* **Flexibility Test:** Manually added a unique attribute (`StudentsComplete`) to a single item.
* **Result:** Verified that unlike SQL databases, DynamoDB allowed this item to have a unique schema without requiring a table-wide migration or empty columns for other records.

## 📸 Verification

1.  **Infrastructure as Code:** CloudShell terminal showing the successful batch ingestion of data.
    <img width="1509" height="829" alt="Screenshot 2026-01-04 at 2 34 47 AM" src="https://github.com/user-attachments/assets/9ba8704e-7664-4e99-93d7-ea8889dabc1b" /><br>

2.  **Database Overview:** DynamoDB Console displaying the suite of 5 active tables.
    <img width="1509" height="829" alt="Screenshot 2026-01-04 at 2 35 08 AM" src="https://github.com/user-attachments/assets/cd8144b5-8485-4f80-abd0-43ed63db6196" /><br>

3.  **Data Verification:** `ContentCatalog` table populated with diverse items (Videos, Projects) and attributes.
    <img width="1509" height="829" alt="Screenshot 2026-01-04 at 2 36 14 AM" src="https://github.com/user-attachments/assets/6c662588-c189-4282-b935-be31ab995e69" /><br>


## 🧠 Key Learnings
* **SQL vs. NoSQL:** Deepened understanding of when to use Relational (structured, rigid) vs. Non-Relational (flexible, high-speed) databases.
* **CLI Automation:** Gained proficiency in `aws dynamodb` CLI commands (`create-table`, `batch-write-item`) to perform tasks faster than the Console allows.
* **Throughput Management:** Learned how RCU and WCU settings directly impact both performance and cost.
