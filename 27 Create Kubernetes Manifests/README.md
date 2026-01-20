# Infrastructure as Code: Defining Microservices for EKS

## 🎯 Project Goal
To translate a containerized application into a production-ready Kubernetes architecture. Following the containerization of the Backend API (Docker/ECR), this phase focused on **Infrastructure as Code (IaC)**. I authored **Kubernetes Manifests (YAML)** to define the desired state of the application's compute (Deployment) and networking (Service) layers before deployment.

## ⚙️ Architecture Design
* **Kubernetes Deployment:** chosen to manage the stateless Flask backend, ensuring High Availability through replica management.
* **ClusterIP Service:** Selected as the networking model to restrict access. Unlike the public-facing Storefront, the Backend API is designed to be accessible *only* by other pods within the cluster, not the public internet.
* **Declarative Configuration:** Used YAML to define the *end state* of the system rather than imperative commands.<br>

  <img width="1570" height="818" alt="CC 9" src="https://github.com/user-attachments/assets/2906afe7-fe23-4e95-bfa8-7692cbec40fd" /><br>


## 🛠️ Implementation Steps

### 1. Designing the Compute Layer (Deployment)
* **Objective:** Define how the application should run on the cluster.
* **Configuration:** Authored `backend-deployment.yaml` with the following specifications:
    * **Replicas:** Set to `3` to ensure redundancy and load distribution.
    * **Image Source:** Configured to pull the `nextwork-flask-backend` image securely from my private **Amazon ECR** repository.
    * **Selectors:** Defined strict `matchLabels` to ensure the Deployment Controller manages the correct set of Pods.

### 2. Designing the Network Layer (Service)
* **Objective:** Define how other applications (like the Frontend) will talk to this Backend.
* **Configuration:** Authored `backend-service.yaml`.
* **Security Decision:** Specifically chose `type: ClusterIP`.
    * **Why:** The backend handles business logic and should not be exposed to the public web. `ClusterIP` assigns it a stable internal IP address reachable only by internal cluster traffic (Service Discovery).
* **Port Strategy:** Mapped internal Container Port `5000` (Flask default) to Service Port `5000`.

### 3. Service Discovery Logic
* **Concept:** By naming the Service object `backend-service`, I enabled Kubernetes' internal DNS (CoreDNS) to resolve this name.
* **Result:** The Frontend application will be able to reach the backend simply by calling `http://backend-service:5000`, decoupling the architecture from changing IP addresses.

## 📸 Verification

1.  **Deployment and Service YAML file:**<br>
    <img width="1512" height="856" alt="Screenshot 2026-01-13 at 2 07 58 AM" src="https://github.com/user-attachments/assets/83a78f29-3a97-471f-9342-fcbb30f8ad26" /><br>

    <img width="1512" height="856" alt="Screenshot 2026-01-13 at 2 08 08 AM" src="https://github.com/user-attachments/assets/f22db91c-082f-4b16-a431-001220e2b074" /><br>



## 🧠 Key Learnings
* **Declarative Syntax:** Mastered the structure of Kubernetes YAML (`apiVersion`, `kind`, `metadata`, `spec`) and the importance of precise indentation.
* **Internal vs. External Traffic:** Deepened understanding of Kubernetes Service types—specifically why a Backend requires `ClusterIP` (Private) while a Frontend requires `LoadBalancer` (Public).
* **Label Selectors:** Learned how the `selector` field acts as the "glue" that binds a Service to a specific set of Pods managed by a Deployment.
