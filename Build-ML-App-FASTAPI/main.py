from fastapi import FastAPI

# app = FastAPI()
myapp =  FastAPI()
@myapp.get("/") # Path operation decorator

# @myapp.post, @myapp.put,@myapp.delete
async def root():
    return {"message":"Hello World from FASTAPI"}

@myapp.get("/demo")
def demo_function():
    return {"message":"Output from demo function"}

@myapp.post("/post_demo")
def post_function():
    return {"message":"Output from demo post_function"}