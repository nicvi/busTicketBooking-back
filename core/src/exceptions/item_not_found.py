class ItemNotFoundError(Exception):
    def __init__(self, error_msg: str = "Item not found in data"):
        super().__init__(error_msg)

        self.error_msg = error_msg
