from fastapi import FastAPI




# async def lifespan(app: FastAPI):
#     create_db_and_tables()
#     yield


app = FastAPI(
    title="inventory_service",
    description="API for managing inventory",
    version="1.0.0",
    # lifespan=lifespan,
)


@app.get("/")
def home():
    return "Welcome to inventory_service"