# Review Trackers Project
This project builds a docker image containing a sample python flask web application and deploys it to AWS ECS. All deployments are done using terraform. Below you will find steps on how to run this project.
## Folder Structure
```
├── Dockerfile
├── K8
│   └── deploy.yml
├── README.md
├── main.py
├── requirements.txt
└── terraform
    ├── cluster.tf
    ├── iam.tf
    ├── lb.tf
    ├── outputs.tf
    ├── provider.tf
    ├── security_groups.tf
    ├── terraform.tfstate
    ├── terraform.tfstate.backup
    └── vpc.tf
```

## Requirements
- Terraform 

## How to Run Application
### Step 1
- `git clone https://github.com/lseino/reviewtrackers`
- `cd reviewtrackers`

### Optional - Build docker image with Git Actions
- add your DOCKERHUB_USERNAME & DOCKERHUB_TOKEN as secrets in the project
- optionally you can build and push image locally using 
     - `docker build -t $dockerhub_username/image_name:tag .`
     - `docker push $dockerhub_username/image_name:tag` (you might need to authenticate your registry)

### Step 2 - Run Terraform Code
- `cd terraform`
- `terraform init && terraform plan`
- `terraform apply`
- After completion, the terraform code will output the load balancer DNS name. Copy it and paste on your web browser and add `/status` eg `python-lb-tf-1584404261.us-east-1.elb.amazonaws.com/status` to see results

## Clean Up
- `terraform destroy`

## Stretch goals Completed 
- Build and push container image via CI
- Write Kubernetes manifests
- The application should be exposed as a service such that it can be accessed from a browser
- Create a `/ip` endpoint that returns the city and state of the IP requesting the page

