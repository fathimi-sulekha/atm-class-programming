from fastapi import FastAPI
from api.routes import run_atm
from app.core.logging_config import logger
 

 
# Create the FastAPI application
app = FastAPI(
    title=" FastAPI Service",
    description="A service for checking leap year or a prime number.",
    version="1.0.0",
    contact={
        "name": "Development Team",
        "email": "support@example.com",
    },
)
 
# Include the API routes
app.include_router(router)
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
 


