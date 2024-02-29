class ApplicationException(Exception):
    """Custom exception"""
    def __init__(self, *args: object, message: str, code: int) -> None:
        super().__init__(*args)
        self.message = message
        self.code = code
