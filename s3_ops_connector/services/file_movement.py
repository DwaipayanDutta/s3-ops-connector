class FileMovementService:
    def __init__(self, connector):
        self.s3 = connector.s3
        self.parse = connector.parse_path

    def copy(self, source, destination):
        sb, sk = self.parse(source)
        db, dk = self.parse(destination)
        self.s3.copy_object(
            Bucket=db,
            CopySource={"Bucket": sb, "Key": sk},
            Key=dk
        )
        return True

    def move(self, source, destination):
        self.copy(source, destination)
        self.delete(source)
        return True

    def delete(self, s3_path):
        bucket, key = self.parse(s3_path)
        self.s3.delete_object(Bucket=bucket, Key=key)
