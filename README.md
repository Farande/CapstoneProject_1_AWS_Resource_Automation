# AWS Resource Automation Tool Using Python and Boto3

## Overview

The AWS Resource Automation Tool is a Python-based command-line application that automates common AWS resource management tasks using **Boto3**, the AWS SDK for Python.

Instead of manually performing operations through the AWS Management Console, users can manage **Amazon S3** and **Amazon EC2** resources through a simple CLI menu.

The project is designed to demonstrate AWS automation, Python programming, Boto3, IAM permissions, and basic cloud resource management.

---

# Features

## Amazon S3

* Create an S3 bucket
* List existing S3 buckets
* Upload files to an S3 bucket

## Amazon EC2

* Launch an EC2 instance
* List EC2 instances
* Start an EC2 instance
* Stop an EC2 instance
* Terminate an EC2 instance
* Wait for an EC2 instance to reach the `running` state after starting

---

# Technologies Used

* Python
* Boto3
* AWS CLI
* AWS IAM
* Amazon S3
* Amazon EC2

---

# Architecture


                         User
                           |
                           v
                Python CLI Application
                           |
                           v
                         Boto3
                           |
                           v
                       AWS IAM
                           |
                +----------+----------+
                |                     |
                v                     v
           Amazon S3              Amazon EC2
                |                     |
          +-----+-----+        +------+------+
          |     |     |        |      |      |
          v     v     v        v      v      v
       Create Upload List    Launch  Start  Stop
       Bucket  File   Buckets        /      /
                                  Terminate


---

# Project Structure


aws-resource-automation/
│
├── aws_automation.py
├── requirements.txt
├── .gitignore
└── screenshots/
    ├── 01-iam-permissions.png
    ├── 02-running-python-application.png
    ├── 03-s3-bucket.png
    ├── 04-s3-file-upload.png
    ├── 05-s3-list-buckets.png
    ├── 06-ec2-running.png
    └── 07-ec2-information.png


---

# Prerequisites

Before running the project, make sure you have:

* Python 3.x
* AWS CLI
* An AWS account
* An IAM user or IAM role with the required permissions
* Boto3

Check Python:


python --version


Check AWS CLI:


aws --version


---

# Installation

## 1. Clone the Repository


git clone https://github.com/Farande/aws-resource-automation.git


Move into the project directory:


cd aws-resource-automation


---

## 2. Create a Virtual Environment


python -m venv venv


Activate the virtual environment on Windows PowerShell:


.\venv\Scripts\Activate.ps1


---

## 3. Install Dependencies

If `requirements.txt` is already available:


pip install -r requirements.txt


If it does not exist yet:


pip install boto3


Then create the requirements file:


pip freeze > requirements.txt


---

# AWS Configuration

Configure the AWS CLI using:

aws configure


Enter your AWS credentials when prompted.

Example:


AWS Access Key ID: YOUR_ACCESS_KEY
AWS Secret Access Key: YOUR_SECRET_KEY
Default region name: ap-south-1
Default output format: json


Verify the AWS configuration:


aws sts get-caller-identity


If the configuration is correct, AWS will display information about the IAM identity being used.

### Security Warning

Do not upload AWS credentials to GitHub.

Never commit:

* AWS Access Keys
* AWS Secret Keys
* `.pem` files
* `.env` files containing secrets

---

# IAM Permissions

The IAM identity used by the application requires permissions for the AWS operations performed by the project.

## Amazon S3 Permissions

Typical permissions include:


s3:CreateBucket
s3:ListAllMyBuckets
s3:PutObject


## Amazon EC2 Permissions

Typical permissions include:


ec2:RunInstances
ec2:DescribeInstances
ec2:StartInstances
ec2:StopInstances
ec2:TerminateInstances


For a production environment, use a more restrictive **least-privilege IAM policy** instead of granting unnecessary permissions.

---

# Running the Application

Run the application using:


python aws_automation.py


The application displays a CLI menu similar to:

========================================
       AWS RESOURCE AUTOMATION TOOL
========================================

1. Create S3 Bucket
2. Upload File to S3
3. List S3 Buckets
4. Launch EC2 Instance
5. List EC2 Instances
6. Start EC2 Instance
7. Stop EC2 Instance
8. Terminate EC2 Instance
9. Exit

Enter your choice:


---

# Amazon S3 Operations

## 1. Create S3 Bucket

Select:


1


The application asks for a globally unique bucket name.

Example:


automated-s3-bucket-2026


S3 bucket names must be globally unique.

---

## 2. Upload File to S3

Select:


2


Enter the bucket name and complete file path.

Example:


Enter bucket name: automated-s3-bucket-2026
Enter complete file path: C:\Users\Nikhil Farande\Downloads\sample.pdf


Do not include quotation marks around the file path.

The selected file will be uploaded to the specified S3 bucket.

---

## 3. List S3 Buckets

Select:


3


The application displays the S3 buckets available to the configured AWS account.

Example:


S3 Buckets
----------
automated-s3-bucket-2026
my-project-bucket


---

# Amazon EC2 Operations

## 4. Launch EC2 Instance

Select:


4


The application asks for:


AMI ID
Key Pair Name
Security Group ID


Example:


Enter AMI ID: ami-xxxxxxxxxxxxxxxxx
Enter key pair name: MySQL-key
Enter security group ID: sg-xxxxxxxxxxxxxxxxx


The AMI ID, key pair name, and security group ID must exist in your AWS account and region.

The instance type used by the application should be available and suitable for your AWS account.

---

# 5. List EC2 Instances

Select:


5


The application displays EC2 instance information.

Example:


EC2 Instances
-------------

Instance ID: i-xxxxxxxxxxxxxxxxx
State: running
Type: t3.micro
AMI: ami-xxxxxxxxxxxxxxxxx

-----------------------------


This allows you to check the current state and basic information about EC2 instances.

---

# 6. Start EC2 Instance

Select:


6


Enter the EC2 instance ID:


i-xxxxxxxxxxxxxxxxx


The application sends the start request and waits for the instance to reach:


running


This demonstrates how Boto3 can perform an EC2 lifecycle operation and wait for the requested state.

---

# 7. Stop EC2 Instance

Select:


7


Enter the EC2 instance ID:


i-xxxxxxxxxxxxxxxxx


The instance changes through:


running
    |
    v
stopping
    |
    v
stopped


---

# 8. Terminate EC2 Instance

Select:


8


The application asks for confirmation:


Are you sure you want to terminate i-xxxxxxxxxxxxxxxxx? (yes/no):


Enter:


yes


The EC2 instance will be terminated.

### Warning

EC2 termination is a destructive operation. A terminated instance cannot normally be restarted.

Use this option carefully.

---

# Testing Workflow

The complete application workflow can be tested as follows:


Run Application
       |
       v
Create S3 Bucket
       |
       v
Upload File
       |
       v
List S3 Buckets
       |
       v
Launch EC2 Instance
       |
       v
List EC2 Instances
       |
       v
Start EC2 Instance
       |
       v
Stop EC2 Instance
       |
       v
Terminate EC2 Instance


Each operation can be verified both from the CLI output and from the AWS Management Console.

---

# Security

This project follows basic AWS security practices:

* AWS credentials are configured through AWS CLI.
* Credentials are not hard-coded in the Python application.
* AWS access keys should never be committed to GitHub.
* `.pem` files should not be uploaded to GitHub.
* IAM permissions should follow the principle of least privilege.
* S3 buckets should remain private unless public access is specifically required.
* EC2 instances should use appropriate security group rules.
* Destructive operations such as EC2 termination should require confirmation.

---

# .gitignore

Create a `.gitignore` file in the project root:


venv/
__pycache__/
*.pyc
.env
*.pem
.aws/


This helps prevent sensitive or unnecessary files from being uploaded to GitHub.

---

# Future Enhancements

The project can be extended with:

* Automatic AMI discovery
* Automatic key pair selection
* Automatic security group selection
* EC2 instance type selection
* EC2 instance tagging
* CloudWatch monitoring

# Conclusion

The **AWS Resource Automation Tool** demonstrates how Python and Boto3 can be used to automate common AWS resource management tasks.

Instead of manually creating and managing resources through the AWS Management Console, users can perform S3 and EC2 operations from a simple command-line application.

The project provides a practical foundation for building more advanced AWS automation tools and cloud management applications.
