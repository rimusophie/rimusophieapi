from fastapi import APIRouter

router = APIRouter()

@router.get("/skills")
async def list_skills():
    pass

@router.post("/skills")
async def create_skill():
    pass

@router.put("/skills/{skill_id}")
async def update_skill():
    pass

@router.delete("/skills/{skill_id}")
async def delete_skill():
    pass