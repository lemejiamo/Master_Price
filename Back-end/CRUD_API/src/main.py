import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import controllers.product as product
import controllers.store as store
import controllers.user as user
import controllers.company as company
from settings import Settings

settings = Settings()

app = FastAPI(
    title="CRUD API",
    description="API for CRUD operations in a Firebase DB",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS,
)

app.include_router(user.router)
app.include_router(product.router)
app.include_router(store.router)
app.include_router(company.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.PORT,
        debug=True,
        reload=True,
        reload_delay=1.5,
    )
