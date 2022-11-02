import requests
from fastapi import HTTPException, status

from settings import Settings

settings = Settings()


def validate_token_client(login_token: str):
    request_url = f"{settings.LOGIN_API_URL}/login/token/validate/{login_token}"
    response = requests.get(
        url=request_url,
    )

    if response.status_code == status.HTTP_202_ACCEPTED:
        return response
    if response.status_code == status.HTTP_401_UNAUTHORIZED:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "client": "validate_token_client",
                "detail": "Invalid token",
            },
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={
                "client": "validate_token_client",
                "detail": "Invalid token, can't connect with DB to check user info",
            },
        )
