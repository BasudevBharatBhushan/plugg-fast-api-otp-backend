import uvicorn 
from fastapi import FastAPI, APIRouter
from dbclient import collection

app = APIRouter()

@app.post("/user")
async def create_user(user: dict):
    try:
        print(user)
        collection.insert_one(user)
        return {"message": "User created successfully"}
    except Exception as e:
        return {"message": str(e)}
    
@app.put("/user/{mobileNumber}")
async def update_user(user: dict , mobileNumber: str):
    try:
        collection.find_one_and_update({"phoneNumber":mobileNumber}, {
            "$set": user
        })
        return {"message": "User updated successfully"}
    except Exception as e:
        return {"message": str(e)}
    
@app.get("/user/{mobileNumber}")
async def get_user(mobileNumber: str):
    try:
        user = collection.find_one({"phoneNumber": mobileNumber})
        
        if user is None:
            return {"phoneNumber": mobileNumber, "found": False}
        
        userDict = {
            "phoneNumber": user.get("phoneNumber"),
            "isVerified": user.get("isVerified"),
            "createdAt": user.get("createdAt"),
            "updatedAt": user.get("updatedAt"),
            "found": True
        }
        return userDict
        
    except Exception as e:
        return {"message": str(e)}

@app.get("/users")
async def get_users():
    try:
        users =  collection.find()
        userList = []
        
        for user in users:
            userDict = {
                "mobileNumber":user.get("phoneNumber"),
                "isVerified":user.get("isVerified"),
                "createdAt":user.get("createdAt"),
                "updatedAt":user.get("updatedAt")
            }
            userList.append(userDict)
        return userList

    except Exception as e:
        return {"message": str(e)}