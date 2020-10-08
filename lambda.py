import os
import logging
import boto3
import json
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def notify(report):
    sns = boto3.client('sns')
    response = sns.publish(TopicArn='<SNS ARN>',Message=json.dumps(report))

def lambda_handler(event, context):
    logger.info(event)
    report = {'author':'yunoth'}
    report['sgid'] = event['detail']['requestParameters']['groupId']
    report['userName']	= event['detail']['userIdentity']['userName']
    report['event'] = event['detail']['eventName']
    for x, i in enumerate(event['detail']['requestParameters']['ipPermissions']['items']):
         report[x] = {}
         report[x]['fromport'] = i['fromPort']
         report[x]['toport'] = i['toPort']
         report[x]['ipRanges'] = i['ipRanges']['items']
    notify(report)
    #print(report)
