from fileinput import filename
import logging, boto3, os, time
from turtle import up
from botocore.exceptions import ClientError

REGION = "us-east-1"
KEYNAME = 'basickeypair'
AMI = "ami-026b57f3c383c2eec" 
SUBNET = "subnet-0f07176caf4f9c63c" 
SG_ID = "sg-0e2841db4ef05c06d"
INSTANCE_PROFILE = 'Administrator'

client = boto3.client('ec2')
resource = boto3.resource('ec2', region_name = REGION)

def buildEC2():
    instances = resource.create_instances(
        MinCount = 1,
        MaxCount = 1,
        ImageId = AMI,
        InstanceType = 't3.micro',
        KeyName = KEYNAME,
        SecurityGroupIds = [
            SG_ID,
        ],
        SubnetId = SUBNET,
        TagSpecifications = [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    },
                ]
            },
        ]
    )
    # SAVE NEW RESOURCE IN DICT TO RETRIEVE INSTANCE ID AS 'new_id'
    listEC2two()
    print('pending', end='')
    # PENDING LOOP
    while True:
        EC2_status()
        try:
            if response['InstanceStatuses'][0]['InstanceState']['Name'] == 'pending':
                time.sleep(.5)
                print('.', end='')
            elif response['InstanceStatuses'][0]['InstanceState']['Name'] == 'running':
                print('')
                print(new_id, 'Running! Waiting for health checks...')
                break
        except IndexError:
            print('')
            print(new_id, 'Running! Waiting for health checks...')
            break

def EC2_status():
    global response
    # LISTS PROGRESS
    response = client.describe_instance_status(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'pending',
            ]
        },
    ],
    InstanceIds=[
        new_id,
    ],
    #MaxResults=123,
    #NextToken='string',
    DryRun=False,
    IncludeAllInstances=True
    )

def listEC2():
    global hello
    hello = {}
    while True:
        global instance_name
        instance_name = input('Enter EC2 resource: ')
        instances = resource.instances.filter(
        Filters=[{
            'Name': 'tag:Name',
            'Values': [
                instance_name
            ]
            }]
            )
        for value in instances:
            hello[instance_name] = value
        if instance_name in hello:
            print(hello, 'is already in use, try again. ')
        else:
            print('Creating new EC2 instance...')
            break

def listEC2two():
    global hello2, new_id
    hello2 = {}
    while True:
        instances = resource.instances.filter(
        Filters=[{
            'Name': 'tag:Name',
            'Values': [
                instance_name
            ]
            }]
            )
        for value in instances:
            hello2[instance_name] = value
        # ID FOR CREATED INSTANCE
        created = str(hello2[instance_name])
        new_id = created[17:36]
        print(new_id)
        break

# PROGRAM START
listEC2()
buildEC2()
print('Exiting...')