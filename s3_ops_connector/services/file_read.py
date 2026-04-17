import pandas as pd

class FileReadService:
    def __init__(self, connector):
        self.s3 = connector.s3
        self.parse = connector.parse_path

    def preview(self, s3_path, n=5):
        bucket, key = self.parse(s3_path)
        obj = self.s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(obj["Body"])
        return df.head(n)

    def full_read(self, s3_path):
        bucket, key = self.parse(s3_path)
        obj = self.s3.get_object(Bucket=bucket, Key=key)
        return pd.read_csv(obj["Body"])
