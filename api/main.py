from fastapi import FastAPI
from api.routers import skill, job_career, portfolio

app = FastAPI()
app.include_router(skill.router)
app.include_router(job_career.router)
app.include_router(portfolio.router)
