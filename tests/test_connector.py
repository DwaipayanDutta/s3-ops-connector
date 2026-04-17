from s3_ops_connector import S3OpsClient

def test_init():
    client = S3OpsClient()
    assert client is not None
