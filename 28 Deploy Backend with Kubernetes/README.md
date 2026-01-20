# Microservices on EKS: Deploying the Backend

## 🎯 Project Goal
To complete the microservices architecture on Amazon EKS. Having deployed the Frontend (Storefront) and containerized the Backend (Flask API), this project focused on **deploying the Backend** to the cluster and establishing secure, internal communication between the services using **Kubernetes Service Discovery**.

## ⚙️ Architecture Components
* **Backend Microservice:** A Flask-based API containerized with Docker.
* **ClusterIP Service:** A Kubernetes Service type that exposes the application on an internal IP, accessible only within the cluster.
* **CoreDNS:** The internal DNS server in Kubernetes that allows services to resolve each other by name (e.g., `backend-service`).
* **Service Discovery:** The mechanism allowing the Frontend to find the Backend without hardcoding IP addresses.<br>

  <img width="1511" height="790" alt="CC 10" src="https://github.com/user-attachments/assets/ee863de4-c928-43f0-813e-8203137679e0" /><br>


## 🛠️ Implementation Steps

### 1. Deployment Configuration
* **Manifest Creation:** Authored `backend-deployment.yaml` to define the desired state.
* **Image Linking:** Configured the deployment to pull the specific Docker image (`nextwork-flask-backend`) from my private **Amazon ECR** repository.
* **Resiliency:** Set `replicas: 2` to ensure redundancy.

### 2. Internal Network Configuration
* **Security Decision:** Chose `ClusterIP` instead of `LoadBalancer` for the `backend-service`. This ensures the API is **not** exposed to the public internet, adhering to the Principle of Least Privilege.
* **Port Mapping:** Exposed the application on Port 5000.

### 3. Verification (Internal Connectivity)
* **Challenge:** Since the backend is private, I could not test it via a web browser.
* **Solution:** Used `kubectl exec` to log into a running **Storefront Pod**.
* **Test:** Executed a `curl` command from the Storefront to the Backend using its DNS name:
    ```bash
    curl http://backend-service:5000/api/status
    ```
* **Result:** Received a `200 OK` JSON response, confirming that the Frontend can successfully talk to the Backend via the internal network.

## 📸 Verification

1.  **Pod Overview:** Terminal showing all microservices (Store & Backend) running in the cluster.
    <img width="1511" alt="All Pods Running" src="PLACEHOLDER_LINK_HERE" /><br>

2.  **Deployment Manifest:** The YAML file configured with the ECR Image URI.
    <img width="1511" alt="Backend Manifest" src="PLACEHOLDER_LINK_HERE" /><br>

3.  **Service List:** Evidence of the distinction between Public (LoadBalancer) and Private (ClusterIP) services.
    <img width="1511" alt="Service List" src="PLACEHOLDER_LINK_HERE" /><br>

4.  **Connectivity Proof:** Successful `curl` response proving internal Service Discovery is working.
    <img width="1511" alt="Internal Curl Test" src="PLACEHOLDER_LINK_HERE" /><br>

## 🧠 Key Learnings
* **Public vs. Private:** Mastered the use cases for `LoadBalancer` (Ingress/Frontend) vs. `ClusterIP` (Internal/Backend).
* **Service Discovery:** Learned that in Kubernetes, apps don't talk to IPs; they talk to **Service Names**, and CoreDNS handles the routing.
* **Debugging Pods:** Gained experience using `kubectl exec` to troubleshoot connectivity issues from *inside* the cluster environment.
