from enum import Enum
class status(Enum):
    DONE = "done"
    PENDING = "pending"
    PROCESSING = "processing"
    FAILED = "failed"




class Status:
    def __init__(self, status, filename, timestamp, explanation):
        self.status = status
        self.filename = filename
        self.timestamp = timestamp
        self.explanation = explanation

    def is_done(self):
        return self.status == "done"