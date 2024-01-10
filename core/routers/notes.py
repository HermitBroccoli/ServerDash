from fastapi import APIRouter, status, Response, Request
from fastapi.responses import JSONResponse
from core.middleware.auth_user import auth_user
from core.features.datadase import DatabaseCRUD
from core.routers.code_status import AccessRights
from pydantic import BaseModel
from typing import Optional
from datetime import date
import json

class Note(BaseModel):
	title: str
	description: str
	status: str
	due_date: Optional[date] = ""


app = APIRouter(
	tags=['notes'],
	prefix="/notes"
)

@app.get("/all_notes/{id}")
async def get_all_notes(id):
	res = await DatabaseCRUD.select_all_notes(id)
	
	return JSONResponse(status_code=status.HTTP_200_OK,
					 content={
						 "code": AccessRights.FULL_ACCESS.value,
						 "type": "access",
						 "msg": "Access",
						 "data": res
					 })

@app.post("/create")
async def create_notes(note: Note):
	pass