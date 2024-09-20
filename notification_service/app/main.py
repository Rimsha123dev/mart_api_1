from fastapi import FastAPI




# async def lifespan(app: FastAPI):
#     create_db_and_tables()
#     yield


app = FastAPI(
    title="notification_service",
    description="API for managing notifications",
    version="1.0.0",
    # lifespan=lifespan,
)


@app.get("/")
def home():
    return "Welcome to notification_service"