import boto3

sts = boto3.client('sts')

credentials = sts.assume_role(
    RoleArn='arn:aws:iam::540467641217:role/S3_creativeai',
    RoleSessionName='AssumeRoleSession1'
)['Credentials']

s3_resource = boto3.resource(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
)
