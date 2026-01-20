# Deploying Microservices on Amazon EKS

## 🎯 Project Goal
To deploy a scalable, containerized application on a production-grade Kubernetes cluster. Building on the previous infrastructure setup, I utilized **Kubernetes Manifests (YAML)** to define the desired state of a "Storefront" microservice and leveraged **Services** to expose it to the public internet via an AWS Load Balancer.

## ⚙️ Architecture Components
* **Deployment (Controller):** Manages the lifecycle of the application, ensuring 3 replicas are always running for High Availability.
* **Pod:** The atomic unit of the application (hosting the Container).
* **Service (LoadBalancer):** An abstraction layer that provides a stable endpoint for traffic, automatically provisioning an **AWS Classic Load Balancer** to route requests to the dynamic pods.
* **kubectl:** The command-line tool used to send instructions to the Kubernetes API Server.<br>

  <img width="1570" height="818" alt="CC 9" src="https://github.com/user-attachments/assets/2906afe7-fe23-4e95-bfa8-7692cbec40fd" /><br>


## 🛠️ Implementation Steps

### 1. Defining the State (YAML Manifests)
* **Deployment Strategy:** Created `store-deployment.yaml` to define the application logic:
    * **Image:** Pulled a custom container image from ECR (`public.ecr.aws/nextwork/store-app`).
    * **Scale:** Configured `replicas: 3` to distribute load and handle failures.
* **Network Strategy:** Created `store-service.yaml` to handle ingress traffic:
    * **Type:** Set to `LoadBalancer` to trigger the creation of an external AWS ELB.
    * **Port Mapping:** Mapped external Port 80 to internal Container Port 80.

### 2. Deployment & Orchestration
* **Execution:** Applied the manifests using `kubectl apply -f .`.
* **Observation:** Verified that the **Scheduler** distributed the 3 pods across the available Worker Nodes.

### 3. Resilience Testing
* **Test:** Manually deleted a running Pod (`kubectl delete pod ...`).
* **Result:** The **ReplicaSet Controller** immediately detected the deviation from the "Desired State" (2 vs 3) and spun up a new Pod instantly, proving the self-healing nature of the architecture.

### 4. Public Access
* **Discovery:** Retrieved the `EXTERNAL-IP` using `kubectl get service`.
* **Access:** Successfully accessed the web application via the provisioned AWS Load Balancer DNS, confirming end-to-end connectivity from the Internet -> Load Balancer -> Worker Node -> Pod.

## 📸 Verification

1.  **Deployment and Service YAML file:**<br>
    <img width="1512" height="856" alt="Screenshot 2026-01-13 at 2 07 58 AM" src="https://github.com/user-attachments/assets/83a78f29-3a97-471f-9342-fcbb30f8ad26" /><br>

    <img width="1512" height="856" alt="Screenshot 2026-01-13 at 2 08 08 AM" src="https://github.com/user-attachments/assets/f22db91c-082f-4b16-a431-001220e2b074" /><br>



## 🧠 Key Learnings
* **Imperative vs. Declarative:** Shifted from "launching servers" (Imperative) to "defining states" (Declarative) using YAML.
* **The Service Abstraction:** Understood that Pods are ephemeral (they die and change IPs), so a **Service** is required to provide a stable, permanent address for clients to connect to.
* **Cloud Integration:** Witnessed the seamless integration where a Kubernetes command (`type: LoadBalancer`) triggers a physical AWS infrastructure event (creating an ELB).
