# Review Trackers Project

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
- add your docker hub password in secrets $dockerhub_pass
- change the username env variable in the *./github/workflows/build.yml file to your docker* hub username
- push repo

### Step 2 - Run Terraform Code
- `cd terraform`
- `terraform plan && terraform apply`

## Clean Up
- `terraform destroy`

