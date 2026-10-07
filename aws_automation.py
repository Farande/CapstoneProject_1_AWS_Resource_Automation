import boto3
from botocore.exceptions import ClientError


REGION = "ap-south-1"

s3 = boto3.client("s3", region_name=REGION)
ec2 = boto3.client("ec2", region_name=REGION)


def create_s3_bucket():
    bucket_name = input("Enter S3 bucket name: ").strip()

    if not bucket_name:
        print("Bucket name cannot be empty.")
        return

    try:
        if REGION == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    "LocationConstraint": REGION
                }
            )

        print(f"S3 bucket '{bucket_name}' created successfully.")

    except ClientError as e:
        print("Error:", e)


def list_s3_buckets():
    try:
        response = s3.list_buckets()

        buckets = response.get("Buckets", [])

        if not buckets:
            print("No S3 buckets found.")
            return

        print("\nExisting S3 Buckets")
        print("-------------------")

        for bucket in buckets:
            print(bucket["Name"])

    except ClientError as e:
        print("Error:", e)


def upload_file_to_s3():
    bucket_name = input("Enter bucket name: ").strip()
    file_path = input("Enter complete file path: ").strip()

    try:
        file_name = file_path.split("\\")[-1]

        s3.upload_file(
            file_path,
            bucket_name,
            file_name
        )

        print("File uploaded successfully.")

    except FileNotFoundError:
        print("File not found.")

    except ClientError as e:
        print("Error:", e)


def launch_ec2_instance():
    ami_id = input("Enter AMI ID: ").strip()
    key_name = input("Enter key pair name: ").strip()
    security_group_id = input("Enter security group ID: ").strip()

    try:
        response = ec2.run_instances(
            ImageId=ami_id,
            InstanceType="t3.micro",
            MinCount=1,
            MaxCount=1,
            KeyName=key_name,
            SecurityGroupIds=[security_group_id]
        )

        instance = response["Instances"][0]

        print("\nEC2 instance launched successfully.")
        print("Instance ID:", instance["InstanceId"])
        print("State:", instance["State"]["Name"])

    except ClientError as e:
        print("Error:", e)


def list_ec2_instances():
    try:
        response = ec2.describe_instances()

        print("\nEC2 Instances")
        print("-------------")

        found = False

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                found = True

                print("Instance ID:", instance["InstanceId"])
                print("State:", instance["State"]["Name"])
                print("Type:", instance["InstanceType"])
                print("AMI:", instance["ImageId"])
                print("-----------------------------")

        if not found:
            print("No EC2 instances found.")

    except ClientError as e:
        print("Error:", e)


def start_ec2_instance():
    instance_id = input("Enter EC2 instance ID: ").strip()

    try:
        response = ec2.start_instances(
            InstanceIds=[instance_id]
        )

        print(f"\nStart request sent for {instance_id}.")
        print("Waiting for instance to become running...")

        waiter = ec2.get_waiter("instance_running")
        waiter.wait(InstanceIds=[instance_id])

        response = ec2.describe_instances(
            InstanceIds=[instance_id]
        )

        instance = response["Reservations"][0]["Instances"][0]

        print("\nEC2 instance started successfully!")
        print("Instance ID:", instance["InstanceId"])
        print("State:", instance["State"]["Name"])

    except ClientError as e:
        print("Error:", e)


def stop_ec2_instance():
    instance_id = input("Enter EC2 instance ID: ").strip()

    try:
        ec2.stop_instances(
            InstanceIds=[instance_id]
        )

        print(f"Stop request sent for {instance_id}.")

    except ClientError as e:
        print("Error:", e)


def terminate_ec2_instance():
    instance_id = input("Enter EC2 instance ID: ").strip()

    confirmation = input(
        f"Are you sure you want to terminate {instance_id}? (yes/no): "
    ).strip().lower()

    if confirmation != "yes":
        print("Termination cancelled.")
        return

    try:
        ec2.terminate_instances(
            InstanceIds=[instance_id]
        )

        print(f"Termination request sent for {instance_id}.")

    except ClientError as e:
        print("Error:", e)


def main():
    while True:

        print("\n========================================")
        print("       AWS RESOURCE AUTOMATION TOOL")
        print("========================================")
        print("1. Create S3 Bucket")
        print("2. Upload File to S3")
        print("3. List S3 Buckets")
        print("4. Launch EC2 Instance")
        print("5. List EC2 Instances")
        print("6. Start EC2 Instance")
        print("7. Stop EC2 Instance")
        print("8. Terminate EC2 Instance")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            create_s3_bucket()

        elif choice == "2":
            upload_file_to_s3()

        elif choice == "3":
            list_s3_buckets()

        elif choice == "4":
            launch_ec2_instance()

        elif choice == "5":
            list_ec2_instances()

        elif choice == "6":
            start_ec2_instance()

        elif choice == "7":
            stop_ec2_instance()

        elif choice == "8":
            terminate_ec2_instance()

        elif choice == "9":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()