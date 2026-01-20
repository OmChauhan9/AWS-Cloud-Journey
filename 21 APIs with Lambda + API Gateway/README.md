# Serverless Logic Tier: API Gateway & AWS Lambda

## 🎯 Project Goal
To implement the **Logic Tier** of a serverless Three-Tier Architecture. Following the deployment of the frontend (Presentation Tier), this project focuses on building the backend "brains" using **AWS Lambda** for compute and **Amazon API Gateway** as the secure entry point for API requests.

## ⚙️ Architecture Components
* **AWS Lambda:** A serverless compute service that runs the application logic (Node.js) in response to events.
* **Amazon API Gateway:** A managed service that creates, publishes, and secures APIs at any scale.
* **Rest API:** The architectural style used to design the API, utilizing standard HTTP methods (GET).
* **Lambda Proxy Integration:** A configuration that allows the API to pass the full client request directly to the Lambda function for processing.<br>

  <img width="798" height="546" alt="CC 2" src="https://github.com/user-attachments/assets/cd9a9663-0bad-4cb2-8bda-4c3e555da795" /><br>


## 🛠️ Implementation Steps

### 1. The "Brain" (Lambda Function)
* **Action:** Provisioned a Node.js Lambda function (`RetrieveUserData`).
* **Logic:** The function is designed to receive a `UserID` from an event and prepares to query a database (to be implemented in the Data Tier).
* **Permissions:** Configured an IAM Execution Role allowing the function to write logs to CloudWatch for debugging.

### 2. The "Front Door" (API Gateway)
* **API Type:** Created a **REST API** (`UserRequestAPI`) to handle HTTP requests.
* **Resource Design:** Defined a resource path `/users` to logically organize user-related operations.
* **Method Definition:** Implemented a `GET` method to handle data retrieval requests.

### 3. Integration & Deployment
* **Connection:** Configured **Lambda Proxy Integration** to connect the API method directly to the backend function.
* **Deployment:** Deployed the API to a **Stage** named `prod`, generating a public Invoke URL.
* **Verification:** Tested the endpoint to confirm the API successfully triggers the Lambda function (verified via CloudWatch logs).

## 📸 Verification

1.  **Serverless Compute:** Lambda console showing the deployed python function.
    <img width="1511" height="856" alt="Screenshot 2026-01-10 at 12 29 21 AM" src="https://github.com/user-attachments/assets/53415ecd-7ee0-489d-9332-8f8380669cfc" /><br>

2.  **API Structure:** API Gateway console displaying the `/users` resource and `GET` method.
    <img width="1511" height="856" alt="Screenshot 2026-01-10 at 12 29 47 AM" src="https://github.com/user-attachments/assets/0c033bd5-88fe-4a4d-b17b-562bd7f87065" /><br>

3.  **Live Endpoint:** The Stage Editor showing the `prod` Invoke URL.
    <img width="1511" height="856" alt="Screenshot 2026-01-10 at 12 30 16 AM" src="https://github.com/user-attachments/assets/b621369f-2719-467a-baa1-6ecba6b1f2c5" /><br>

## 🧠 Key Learnings
* **Decoupling Services:** Understood how API Gateway acts as an abstraction layer, allowing the backend logic (Lambda) to change without affecting the frontend client.
* **Serverless Cost Model:** Learned that unlike EC2 (paying for uptime), Lambda and API Gateway are "Pay-as-you-go," charging only when requests are made.
* **Stages & Versioning:** Discovered how API Gateway uses "Stages" (e.g., `dev`, `prod`) to manage different versions of an API, allowing for safe testing before live deployment.
