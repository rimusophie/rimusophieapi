from fastapi import APIRouter

router = APIRouter()

@router.get("/job_careers")
async def list_job_careers():
    pass

@router.post("/job_careers")
async def create_job_career():
    pass

@router.put("/job_careers/{job_career_id}")
async def update_job_career():
    pass

@router.delete("/job_careers/{job_career_id}")
async def delete_job_career():
    pass