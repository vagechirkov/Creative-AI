import boto3

import config


def upload_file(file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket_name: Bucket to upload to
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    s3 = get_s3_resource()

    # check if bucket exists
    bucket = get_bucket(config.S3_BUCKET_NAME, s3)

    try:
        bucket.upload_file(file_name, object_name,
                           ExtraArgs={
                               'ACL': 'public-read'
                           })
        url = f'https://{config.S3_BUCKET_NAME}.s3.amazonaws.com/{object_name}'
        return url
    except Exception as e:
        print(e)
        return False


def get_bucket(bucket_name, s3):
    if bucket_name not in [bucket.name for bucket in s3.buckets.all()]:
        # create bucket
        s3.create_bucket(Bucket=bucket_name)
    else:
        # get bucket
        bucket = s3.Bucket(bucket_name)
    return bucket


def get_s3_resource():
    # boto3 client
    sts = boto3.client(
        'sts',
        aws_access_key_id=config.S3_ACCESS_KEY_ID,
        aws_secret_access_key=config.S3_SECRET_ACCESS_KEY)
    # get credentials
    credentials = sts.assume_role(
        RoleArn=config.S3_ROLE_ARN,
        RoleSessionName='AssumeRoleSession1'
    )['Credentials']
    # get service resource
    s3 = boto3.resource(
        's3',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
    )
    return s3
