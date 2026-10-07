##AWS Resource Automation Tool Using Python and Boto3
Overview

The AWS Resource Automation Tool is a Python-based command-line application that automates common AWS resource management tasks using Boto3, the AWS SDK for Python.

Instead of manually performing operations from the AWS Management Console, users can manage Amazon S3 and Amazon EC2 resources directly from a simple CLI menu.

#Features

Amazon S3
Create an S3 bucket
List existing S3 buckets
Upload files to an S3 bucket
Amazon EC2
Launch an EC2 instance
List EC2 instances
Start an EC2 instance
Stop an EC2 instance
Terminate an EC2 instance
Wait for an EC2 instance to reach the running state after starting
Technologies Used
Python
Boto3
AWS IAM
Amazon S3
Amazon EC2
AWS CLI


##Architecture
                User
                  |
                  v
        Python CLI Application
                  |
                Boto3
                  |
                  v
             AWS IAM
                  |
        +---------+---------+
        |                   |
        v                   v
   Amazon S3            Amazon EC2
        |                   |
   - Buckets           - Launch
   - Upload            - List
   - List              - Start
                       - Stop
                       - Terminate

#Project Structure

aws-resource-automation/
│
├── aws_automation.py
├── requirements.txt
└── screenshots/
    ├── 01-iam-permissions.png
    ├── 02-running-python-application.png
    ├── 03-s3-bucket.png
    ├── 04-s3-file-upload.png
    ├── 05-s3-list-buckets.png
    ├── 06-ec2-running.png
    └── 07-ec2-information.png


#Prerequisites

Before running the project, install:

Python 3.x
AWS CLI
An AWS account
An IAM user or role with the required permissions
Boto3

Check Python:

python --version

Check AWS CLI:

aws --version

Installation

1. Clone the repository

git clone https://github.com/yFarande/aws-resource-automation.git

Move into the project:

cd aws-resource-automation

2. Create a virtual environment

python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1

3. Install dependencies

pip install -r requirements.txt

If requirements.txt does not exist yet:

pip install boto3
pip freeze > requirements.txt
AWS Configuration


Configure AWS CLI:

aws configure

Enter your AWS credentials when prompted.

Example:

AWS Access Key ID: YOUR_ACCESS_KEY
AWS Secret Access Key: YOUR_SECRET_KEY
Default region name: ap-south-1
Default output format: json

Verify the configuration:

aws sts get-caller-identity

Do not upload AWS access keys or secret keys to GitHub.

IAM Permissions

The IAM identity used by the application requires permissions for the AWS operations used by the project.

Typical permissions include:

S3
s3:CreateBucket
s3:ListAllMyBuckets
s3:PutObject
EC2
ec2:RunInstances
ec2:DescribeInstances
ec2:StartInstances
ec2:StopInstances
ec2:TerminateInstances

For a real production environment, use a more restrictive least-privilege IAM policy.

#Running the Application

Run:

python aws_automation.py

The application displays:

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
S3 Operations
Create S3 Bucket

Select:

1

Enter a globally unique bucket name.

Example:

automated-s3-bucket-2026
Upload File

Select:

2

Enter the bucket name and complete file path.

Example:

Enter bucket name: automated-s3-bucket-2026
Enter complete file path: C:\Users\Nikhil Farande\Downloads\sample.pdf

Do not include quotation marks around the path.

List S3 Buckets

Select:

3

The application displays the existing S3 buckets.

EC2 Operations
Launch EC2 Instance

Select:

4

The application asks for:

AMI ID
Key Pair Name
Security Group ID

#Example:

Enter AMI ID: ami-xxxxxxxxxxxxxxxxx
Enter key pair name: MySQl-key
Enter security group ID: sg-xxxxxxxxxxxxxxxxx

The instance type used by the application should be an instance type that is available and eligible for your AWS account.

List EC2 Instances

Select:

5

#Example output:

EC2 Instances
-------------
Instance ID: i-xxxxxxxxxxxxxxxxx
State: running
Type: t3.micro
AMI: ami-xxxxxxxxxxxxxxxxx
-----------------------------
Start EC2 Instance

Select:

6

Enter:

i-xxxxxxxxxxxxxxxxx

The application sends the start request and waits for the instance to reach:

running
Stop EC2 Instance

Select:

7

Enter the EC2 instance ID.

The instance changes from:

running → stopping → stopped
Terminate EC2 Instance

Select:

8

The application asks for confirmation:

Are you sure you want to terminate i-xxxxxxxxxxxxxxxxx? (yes/no):

Enter:

yes

Warning: Termination permanently deletes the EC2 instance.

Security

This project follows basic AWS security practices:

AWS credentials are configured through AWS CLI.
Credentials are not hard-coded in Python.
Secret keys should not be committed to GitHub.
.pem files should not be uploaded to GitHub.
IAM permissions should follow the principle of least privilege.
S3 buckets should remain private unless public access is specifically required.
.gitignore

Create a .gitignore file:

venv/
__pycache__/
*.pyc
.env
*.pem
.aws/
Testing

#The application can be tested using the following workflow:

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
Launch EC2
       |
       v
List EC2 Instances
       |
       v
Start EC2
       |
       v
Stop EC2
       |
       v
Terminate EC2

## Future Enhancements

The project can be extended with:

Automatic AMI discovery
Automatic key pair selection
Automatic security group selection
EC2 instance type selection
EC2 tagging
CloudWatch monitoring
