import os
from typing import Annotated, Any, Dict
from typing_extensions import Doc

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse

from src.routes.ethereum import router as EthereumRouter

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")

# CORS
origins = [
    'https://zapsign-gpt-client-production.up.railway.app',
    'https://zapsign-gpt-client-production.up.railway.app:443'
    ]



description = """
Documentação volta para a integração da ZapSign com Deceval
"""

swagger_ui_default_parameters: Annotated[
    Dict[str, Any],
    Doc(
        """
        Default configurations for Swagger UI.

        You can use it as a template to add any other configurations needed.
        """
    ),
] = {
    "dom_id": "#swagger-ui",
    "layout": "BaseLayout",
    "deepLinking": True,
    "showExtensions": True,
    "showCommonExtensions": True,
    "syntaxHighlight.theme": "obsidian"
}

app = FastAPI(swagger_ui_parameters=swagger_ui_default_parameters)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="ZapSign API - Assinatura Blockchain",
        description=description,
        version="0.0.1",
        terms_of_service="https://mvp-zapsign-ai.netlify.app/#terms",
        routes=app.routes,
        contact={
        "name": "Sulivan T. Leite",
        "url": "https://jogatinando.com/#contact",
        "email": "contato@jogatinando.com",
    },    
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(EthereumRouter, tags=["Ethereum"], prefix="/ethereum")
    