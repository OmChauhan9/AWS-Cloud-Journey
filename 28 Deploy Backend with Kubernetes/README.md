# Cloud-Native Deployment: Flask API on Amazon EKS

## 🎯 Project Goal
To deploy a backend microservice to a Kubernetes environment. Moving beyond local testing, I utilized **Amazon EKS** to orchestrate the deployment, **Amazon ECR** to manage the container artifacts, and **Kubernetes Manifests** to define the infrastructure state declaratively.

## ⚙️ Architecture Components
* **Amazon EKS:** Managed Kubernetes Cluster (Control Plane).
* **Amazon ECR:** Private Container Registry hosting the Docker image.
* **Kubernetes Deployment:** Manages the availability of the backend application (3 Replicas).
* **ClusterIP Service:** Exposes the backend securely to internal cluster traffic only.
* **EC2 Admin Host:** Used as a secure bastion for running `kubectl` and `docker` commands.<br>

  <img width="1511" height="790" alt="CC 10" src="https://github.com/user-attachments/assets/ee863de4-c928-43f0-813e-8203137679e0" /><br>


## 🛠️ Implementation Steps

### 1. Artifact Pipeline (Docker & ECR)
* **Build:** Cloned the Flask application code and built the Docker image locally on the EC2 instance.
* **Security:** Configured IAM permissions to allow the EC2 instance to push to the private ECR repository.
* **Push:** Tagged and pushed the image to Amazon ECR, ensuring a centralized "Source of Truth" for the deployment artifact.

### 2. Kubernetes Orchestration
* **Deployment:** Authored `backend-deployment.yaml` to instruct the cluster to pull the image from ECR and run 3 replicas.
* **Networking:** Authored `backend-service.yaml` using `type: ClusterIP`. This ensures the backend is accessible via DNS (`http://backend-service`) to other pods but remains invisible to the public internet.

### 3. Verification & "Secret Mission"
* **Internal Test:** Used `kubectl exec` to enter a separate pod and successfully `curl` the backend service, proving internal connectivity.
* **Console Auditing:** Navigated the **Amazon EKS Console** to inspect Pod Events. Verified the `Pulled` and `Created` events, confirming the successful integration between the EKS Control Plane and the ECR Registry.

## 📸 Verification

1.  **Artifact Storage:** ECR Console displaying the versioned container image.
    <img width="1511" alt="ECR Image" src="PLACEHOLDER_LINK_HERE" /><br>

2.  **Cluster Status:** Terminal output showing healthy Pods and Services.
    <img width="1511" alt="Kubectl Get Pods" src="PLACEHOLDER_LINK_HERE" /><br>

3.  **Deployment Audit:** EKS Console Events tab proving successful image pulling.
    <img width="1511" alt="Pod Events" src="PLACEHOLDER_LINK_HERE" /><br>

## 🧠 Key Learnings
* **The "Code-to-Cloud" Path:** connecting the dots between raw code (Git) -> Artifact (Docker/ECR) -> Running Application (EKS).
* **Security Best Practices:** Why Backend APIs should use `ClusterIP` (Private) instead of `LoadBalancer` (Public).
* **Debugging:** How to use the AWS Console to view Pod Events when troubleshooting deployment failures (e.g., `ImagePullBackOff`).
