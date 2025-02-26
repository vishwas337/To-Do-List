import boto3
import time

# Initialize AWS clients
ec2 = boto3.client('ec2', region_name='us-east-1')  # Change region if needed
asg = boto3.client('autoscaling', region_name='us-east-1')

def check_instance_health(instance_id):
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    return state == 'running'

def get_instance_id_from_asg(asg_name):
    response = asg.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
    if response['AutoScalingGroups']:
        instances = response['AutoScalingGroups'][0]['Instances']
        if instances:
            return instances[0]['InstanceId']
    return None

def monitor_and_recover():
    asg_name = 'EC2MonitorASG'  # Replace with your Auto Scaling Group name
    instance_id = get_instance_id_from_asg(asg_name)

    if not instance_id:
        print("No instances found in Auto Scaling Group.")
        return

    while True:
        if check_instance_health(instance_id):
            print(f"Instance {instance_id} is running.")
        else:
            print(f"Instance {instance_id} is down. Triggering recovery...")
            asg.update_auto_scaling_group(
                AutoScalingGroupName=asg_name,
                DesiredCapacity=1  # Ensure 1 instance is running
            )
            # Wait for recovery (adjust time as needed)
            time.sleep(300)  # Wait 5 minutes
            instance_id = get_instance_id_from_asg(asg_name)  # Update instance ID

        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    monitor_and_recover()
