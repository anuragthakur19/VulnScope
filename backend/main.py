from fastapi import FastAPI
from app.routes import scan_request
from fastapi.middleware.cors import CORSMiddleware
from app.routes import scan_request

app = FastAPI()

# CORS settings so your frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include scanner API routes
app.include_router(scan_request.router)

@app.get("/")
def read_root():
    return {"message": "Website Vulnerability Scanner API is running."}
