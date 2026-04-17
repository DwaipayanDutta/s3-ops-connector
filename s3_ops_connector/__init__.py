from .version import __version__
from .core.connector import S3Connector
from .services.file_detection import FileDetectionService
from .services.file_validation import FileValidationService
from .services.file_read import FileReadService
from .services.file_movement import FileMovementService
from .services.dq import DataQualityService

class S3OpsClient:
    def __init__(self, region="us-east-1"):
        connector = S3Connector(region)
        self.detect = FileDetectionService(connector)
        self.validate = FileValidationService(connector)
        self.read = FileReadService(connector)
        self.move = FileMovementService(connector)
        self.dq = DataQualityService()
