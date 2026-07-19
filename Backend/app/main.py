from fastapi import FastAPI
from app.routes.health import router as health_router
from app.database import engine

app = FastAPI(
    title="AI GitHub Repository Assistant",
    version="1.0.0"
)

app.include_router(health_router)


@app.get("/db-test")
def test_db():
    try:
        connection = engine.connect()
        connection.close()
        return {"message": "Database connected successfully!"}
    except Exception as e:
        return {"error": str(e)}