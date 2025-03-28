from fastapi import FastAPI, HTTPException
from typing import Type, Callable

class KRDecorator:
    def __init__(self, app: FastAPI):
        self.app = app

    def k_r(self, path: str, client_class: Type, method_name: str):
        def decorator(func: Callable):
            async def wrapper():
                client = client_class()
                try:
                    method = getattr(client, method_name)
                    if not callable(method):
                        raise HTTPException(status_code=500, detail="Method not callable")
                    
                    result = await method()
                    
                    # Check if result is JSON-compatible (dict or list)
                    if isinstance(result, (dict, list)):
                        return result  # Directly return if JSON-compatible
                    else:
                        # Wrap non-JSON responses in a JSON structure
                        return {"message": str(result)}
                finally:
                    await client.close()

            self.app.add_api_route(path, wrapper, methods=["GET"])
            return wrapper
        return decorator