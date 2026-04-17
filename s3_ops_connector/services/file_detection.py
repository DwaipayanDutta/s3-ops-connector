class FileDetectionService:
    def __init__(self, connector):
        self.s3 = connector.s3

    def check_file_arrival(self, bucket, prefix, pattern=None):
        response = self.s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
        files = [obj["Key"] for obj in response.get("Contents", [])]
        if pattern:
            files = [f for f in files if pattern in f]
        return {"status": "present" if files else "missing", "files": files}
