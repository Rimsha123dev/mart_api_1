from fastapi import FastAPI




# async def lifespan(app: FastAPI):
#     create_db_and_tables()
#     yield


app = FastAPI(
    title="order_service",
    description="API for managing orders",
    version="1.0.0",
    # lifespan=lifespan,
)


@app.get("/")
def home():
    return "Welcome to order_service"