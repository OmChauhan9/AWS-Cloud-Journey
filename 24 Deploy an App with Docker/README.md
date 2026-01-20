# Containerized Web Deployment: Docker & AWS Elastic Beanstalk

## 🎯 Project Goal
To containerize a custom web application and deploy it to a scalable cloud environment. I moved beyond simple VM hosting by using **Docker** to package my application and its dependencies into a portable image, and then used **AWS Elastic Beanstalk** to orchestrate the deployment on the AWS Cloud.

## ⚙️ Architecture Components
* **Docker:** Used to containerize the application (Nginx Web Server + Custom HTML).
* **Dockerfile:** The "Infrastructure as Code" script that defines how the image is built.
* **AWS Elastic Beanstalk:** A PaaS service that automatically provisions and manages the underlying EC2 infrastructure for Docker containers.
* **Amazon S3:** Used (in the CLI workflow) to store the application source bundle before deployment.<br>

  <img width="998" height="338" alt="CC 5" src="https://github.com/user-attachments/assets/7124a9c2-1582-4502-94f5-7de8dff1ecba" /><br>

## 🛠️ Implementation Steps

### 1. Docker Image Creation
* **Base Image:** Utilized `nginx:latest` to leverage a pre-configured, high-performance web server.
* **Customization:** Wrote a `Dockerfile` to inject my custom `index.html` into the container's web root.
* **Build:** Executed `docker build -t my-web-app .` to compile the image locally.

### 2. Local Testing & Troubleshooting
* **Execution:** Ran the container mapping Local Port 8080 to Container Port 80.
* **Conflict Resolution:** Encountered a `Bind for 0.0.0.0:8080 failed` error because a previous container was occupying the port.
* **Fix:** Used `docker ps` to identify the rogue container and `docker stop [ID]` to terminate it, freeing the port for the new application.

### 3. Cloud Deployment (Elastic Beanstalk)
* **Packaging:** Zipped the `Dockerfile` and `index.html` into a deployable bundle.
* **Infrastructure:** Created an Elastic Beanstalk Application configured for the **Docker Platform**.
* **Automation:** EB automatically provisioned an EC2 instance, installed the Docker runtime, pulled the base image, and ran my container.

### 4. CLI Upskilling (AWS CLI)
* Instead of just using the Console, I explored the CLI commands to manage the deployment:
    ```bash
    aws elasticbeanstalk create-application --application-name Aws-task24-app-bs-env
    aws elasticbeanstalk create-environment --environment-name Production-Env --solution-stack-name "64bit Amazon Linux 2023 v4.3.0 running Docker"
    ```

## 📸 Verification

1.  **Container Configuration:** The `Dockerfile` defining the build process.
    <img width="1511" height="860" alt="Screenshot 2026-01-11 at 10 51 42 PM" src="https://github.com/user-attachments/assets/c1dd3cde-ea9b-4550-a858-dc9ce3d54435" /><br>

2.  **Platform Health:** Elastic Beanstalk Console showing a healthy, deployed environment.
    <img width="1511" height="860" alt="Screenshot 2026-01-11 at 10 51 51 PM" src="https://github.com/user-attachments/assets/b78ea040-8b4f-406a-af0f-d416d55165e3" /><br>

3.  **Live Deployment:** The application accessible via the public AWS Domain.
    <img width="1511" height="944" alt="Screenshot 2026-01-11 at 10 52 07 PM" src="https://github.com/user-attachments/assets/eef58a66-6637-4ae7-8b4b-4faa4b307c29" /><br>

## 🧠 Key Learnings
* **Port Mapping:** Understood how `-p 8080:80` bridges the gap between my host machine and the isolated container network.
* **PaaS Power:** Elastic Beanstalk abstracts away the complexity of setting up EC2s, Security Groups, and Load Balancers manually.
* **Container Portability:** The exact same container that ran on my laptop ran on AWS without changing a single line of code—solving the "It works on my machine" problem.
