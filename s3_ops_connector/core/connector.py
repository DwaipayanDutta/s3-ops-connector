import boto3

class S3Connector:
    def __init__(self, region="us-east-1"):
        self.s3 = boto3.client("s3", region_name=region)

    def parse_path(self, s3_path):
        bucket, key = s3_path.replace("s3://", "").split("/", 1)
        return bucket, key
