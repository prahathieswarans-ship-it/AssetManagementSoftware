from fastapi import FastAPI
from app.database.db_init import create_assets_table, create_procurements_table,create_maintenance_table,create_assignments_table,create_users_table
from app.routes.asset_routes import router as asset_router
from routes.procurement_routes import router as procurement_router
from routes.maintenance_routes import router as maintenance_router
from routes.assignment_routes import router as assignment_router
from routes.user_routes import router as user_router

app = FastAPI()

create_assets_table()
create_users_table()
create_procurements_table()
create_maintenance_table()
create_assignments_table()
app.include_router(asset_router)
app.include_router(procurement_router)
app.include_router(maintenance_router)
app.include_router(assignment_router)
app.include_router(user_router)
@app.get("/")
def home():
    return {"message": "IDEA Lab Asset Management API running"}
