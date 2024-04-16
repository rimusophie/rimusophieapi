from fastapi import APIRouter

router = APIRouter()

@router.get("/portfolios")
async def list_portfolios():
    pass

@router.post("/portfolios")
async def create_portfolio():
    pass

@router.put("/portfolios/{portfolio_id}")
async def update_portfolio():
    pass

@router.delete("/portfolios/{portfolio_id}")
async def delete_portfolio():
    pass