from fastapi import FastAPI



class APIServer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.app = FastAPI(title=name)
