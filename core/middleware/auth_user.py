from fastapi import FastAPI, Request, Response
from core.features.jwt import Token
from core.routers.code_status import JWTStatus, AccessRights

def auth_user(request: Request):
    
	if request.cookies.get("access_token") != None:
		
		access_token = Token.verify_token(request.cookies.get("access_token"))

		if access_token["code"] == JWTStatus.JWT_VALID.value:
			return True

		return False