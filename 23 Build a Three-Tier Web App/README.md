# Three-Tier Serverless Web Application (Full Integration)

## 🎯 Project Goal
To build and integrate a complete **Three-Tier Architecture** on AWS. This project combines a Frontend (Presentation), Backend API (Logic), and NoSQL Database (Data) into a cohesive application. The focus of this final phase was **Integration Debugging**, specifically solving **CORS** security challenges and **CloudFront Caching** issues to enable secure cross-origin data fetching.

## ⚙️ Architecture Components
* **Presentation Tier:** Amazon S3 (Storage) & CloudFront (CDN) hosting a static website (`index.html`, `script.js`).
* **Logic Tier:** API Gateway (REST API) & AWS Lambda (Node.js) handling incoming requests.
* **Data Tier:** Amazon DynamoDB storing user profiles.
* **Security:** IAM Roles for service permissions & CORS headers for browser security.<br>

  <img width="990" height="775" alt="CC 4" src="https://github.com/user-attachments/assets/5d320f40-3f81-40cd-9962-cacbd19d4354" /><br>

## 🛠️ Implementation Steps

### 1. Frontend Integration
* **Action:** Updated the client-side JavaScript (`script.js`) to replace the placeholder variable with the live **API Gateway Prod Stage URL**.
* **Deployment:** Re-uploaded the assets to S3.
* **Challenge:** The browser continued to serve the old code.
* **Solution:** Executed a **CloudFront Invalidation** (`/*`) via CLI to clear the Edge Cache and force the propagation of the new script.

### 2. CORS Configuration (The Security Layer)
* **Issue:** The browser blocked the frontend from calling the API due to the `Same-Origin Policy` (CloudFront domain ≠ API Gateway domain).
* **Fix Layer 1 (Gateway):** Enabled CORS on the API Gateway resource to handle `OPTIONS` pre-flight requests.
* **Fix Layer 2 (Lambda):** Updated the Node.js function to include standard CORS headers (`Access-Control-Allow-Origin: *`) in the JSON response object.

### 3. End-to-End Testing
* **Scenario:** A user enters `User ID: 1` on the website and clicks "Get Data".
* **Data Flow:**
    1.  Browser sends `GET` request to API Gateway.
    2.  API Gateway triggers Lambda.
    3.  Lambda queries DynamoDB table `UserData`.
    4.  DynamoDB returns the item `{ "Name": "Test User" }`.
    5.  Lambda adds CORS headers and returns JSON to the browser.
    6.  Website DOM updates to display the user's name.

## 📸 Verification

1.  **Logic Update:** Lambda function code including the critical `Access-Control-Allow-Origin` headers.
    <img width="1511" height="856" alt="Screenshot 2026-01-11 at 3 27 34 PM" src="https://github.com/user-attachments/assets/381d2fd8-bca7-4a6b-b21c-2bfe7de551ef" /><br>

2.  **Final Application:** The fully functional Three-Tier Web App displaying data fetched from the backend.
    <img width="1511" height="856" alt="Screenshot 2026-01-11 at 3 26 42 PM" src="https://github.com/user-attachments/assets/8be39530-806f-44a1-afe3-426063e8b8f9" /><br>

## 🧠 Key Learnings
* **CORS vs. IAM:** Learned that IAM handles *AWS Permission* (Can Lambda talk to DynamoDB?), while CORS handles *Browser Permission* (Can Chrome talk to this API?).
* **Cache Invalidation:** Understood that updating S3 does not immediately update the live site if a CDN is involved; explicit invalidation is required for rapid development.
* **Full Stack Troubleshooting:** Gained experience debugging a distributed system by tracing errors from the Browser Console -> API Gateway Logs -> Lambda Execution Logs.
