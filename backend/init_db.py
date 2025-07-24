from app.database.database import Base, engine
from app.database.models import ScanResult

print("Using database at:", engine.url)
print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database initialization complete.")
