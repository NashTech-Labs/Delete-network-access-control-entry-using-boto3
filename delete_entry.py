import boto3
from botocore.exceptions import ClientError
import logging

import time

# Taking input from the user for the region
REGION= input("Please, Enter the region name where you want to Delete this NACL:-")

# setup the logger configuration
logger_info = logging.getLogger()
logging.basicConfig(level=logging.INFO,format='%(message)s')


vpc = boto3.client("ec2", region_name=REGION)

# function to delete the NACL entry
def delete_entry(id, rule_no):

    try:
        response = vpc.delete_network_acl_entry(Egress=False,
                                                       NetworkAclId=id,
                                                       RuleNumber=rule_no)

    except ClientError:

        logger_info.exception('Sorry, Not able to create the network ACL in given VPC')

        raise

    else:
        return response


if __name__ == '__main__':

    # For taking the NACL IN from the user
    NACL_ID = input("Enter the NACL ID to create a NACL entry:- ")

    # Taking the rule number from user which defined while create
    RULE_NUMBER = int(input("Enter the rule number for the NACL entry:- ")) #101

    network_acl = delete_entry(NACL_ID, RULE_NUMBER)

    logger_info.info('Please wait ......  \nWe are creating your NACL...\U0001F570')
    time.sleep(3)

    print("We are creating your NACL...\U0001F570")
    time.sleep(2)
    
    logger_info.info('Hurry, Your NACL Entry has been deleted successfully \U0001F44D')
