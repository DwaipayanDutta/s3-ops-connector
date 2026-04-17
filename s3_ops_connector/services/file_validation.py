class FileValidationService:
    def __init__(self, connector):
        self.s3 = connector.s3
        self.parse = connector.parse_path

    def file_size_check(self, s3_path, min_size):
        bucket, key = self.parse(s3_path)
        obj = self.s3.head_object(Bucket=bucket, Key=key)
        return obj["ContentLength"] >= min_size

    def file_format_check(self, s3_path, expected_format):
        return s3_path.endswith(expected_format)
