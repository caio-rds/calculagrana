from fastapi import APIRouter, HTTPException, Request
from fastapi.encoders import jsonable_encoder

from app.src.model.user import CreateUser, UpdateUser, ReadUser
from app.src.controller.user import create, read, update, delete

router = APIRouter()


@router.post("/", response_model=ReadUser)
async def create_user(new_user: CreateUser, request: Request) -> ReadUser:
    ip = request.client.host
    print(ip)
    creation = await create(new_user)
    return jsonable_encoder(creation)


@router.get("/{u_id}", response_model=ReadUser)
async def get_user(u_id: str) -> ReadUser:
    if user := await read(u_id):
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/", response_model=ReadUser)
async def update_user(user: UpdateUser) -> ReadUser:
    pass
    # return await update(user.u_id, user.dict(exclude_unset=True))


@router.delete("/{u_id}")
async def delete_user(u_id: str):
    pass
    # return await delete(u_id=u_id)