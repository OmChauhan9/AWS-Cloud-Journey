# Advanced DynamoDB Patterns: Queries & Transactions

## 🎯 Project Goal
To master data retrieval and integrity in a NoSQL environment. Building on a previous data ingestion project, I explored the limitations of **Scans**, the speed of **Queries**, and implemented **ACID Transactions** to maintain data consistency across multiple tables using the AWS CLI.

## ⚙️ Architecture Components
* **Amazon DynamoDB:** Managed NoSQL database service.
* **Composite Keys:** Using Partition Key + Sort Key to model one-to-many relationships.
* **AWS CLI (CloudShell):** Used for advanced operations like `transact-write-items`.
* **Transactions:** A mechanism to ensure multiple database writes succeed or fail as a single unit.<br>

  <img width="966" height="452" alt="Database 4" src="https://github.com/user-attachments/assets/3c5c5a7c-6152-40ac-9f06-8bfe52b31f15" /><br>


## 🛠️ Implementation Steps

### 1. Query Performance (O(N) vs O(1))
* **Observation:** Compared a "Scan" (reading the entire table) vs. a "Query" (direct lookup).
* **Result:** Validated that Queries are significantly more efficient but require the strict use of the **Partition Key**.

### 2. Handling Composite Keys
* **Challenge:** Analyzed the `Comment` table where multiple items shared the same ID.
* **Solution:** Identified the **Sort Key** (`CommentDateTime`) which allows multiple unique items to exist under a single Partition Key partition.

### 3. The "Impossible Query" (Error Handling)
* **Experiment:** Attempted to Query the database using a non-key attribute (`PostedBy`).
* **Outcome:** Received a validation error.
* **Key Learning:** Confirmed that DynamoDB Queries *must* utilize the Partition Key. Filtering by arbitrary attributes requires either a full Table Scan (inefficient) or the creation of a **Global Secondary Index (GSI)**.

### 4. Atomic Transactions (CLI)
* **Scenario:** A "New Comment" event requires two updates:
    1.  Insert the comment into the `Comment` table.
    2.  Increment the `Comments` counter in the `Forum` table.
* **Risk:** If the first succeeds but the second fails, the data is corrupt.
* **Implementation:** executed `aws dynamodb transact-write-items` to bundle both operations.
* **Verification:** Confirmed that the `Forum` table's comment count automatically incremented from 0 to 1 upon successful insertion.

## 📸 Verification

1.  **Query Constraints:** error when attempting to Query without a Partition Key.
    <img width="1509" height="829" alt="Screenshot 2026-01-04 at 2 58 48 AM" src="https://github.com/user-attachments/assets/f4dd3fb0-1eb3-4cd7-819f-6e0c242c3722" /><br>

2.  **CLI Data Retrieval:** Successful `get-item` command retrieving specific record details.
    <img width="1509" height="829" alt="Screenshot 2026-01-04 at 3 02 31 AM" src="https://github.com/user-attachments/assets/b88a397c-acbf-4274-8a76-7a5fc5c8d671" /><br>

3.  **Atomic Transaction:** CloudShell execution of the `transact-write-items` command.
    <img width="1509" height="800" alt="Screenshot 2026-01-04 at 3 05 52 AM" src="https://github.com/user-attachments/assets/ba22361a-1f55-4772-ac58-e9b5f7955a3d" /><br>



## 🧠 Key Learnings
* **Scan vs. Query:** Scans read every item (expensive $$), Queries go directly to the address (cheap $).
* **Schema Design:** Understanding that you cannot simply "Select All where Name=X" in DynamoDB unless you design your Keys or Indexes to support it.
* **ACID Transactions:** Learned that NoSQL databases *can* support strict data consistency across tables if using the correct Transactional API calls.
