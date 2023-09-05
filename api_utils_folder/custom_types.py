from fastapi import FastAPI, APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import *
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from pydantic_settings import BaseSettings
from typing import Any
from enum import Enum
from datetime import date, datetime
from urllib.parse import ParseResult, urlparse
from fuzzywuzzy.fuzz import WRatio
import os
import json
import requests
import hashlib

class PrettyJSONResponse(Response):
    media_type = "application/json"
    
    def render(self, content: Any) -> bytes:
        return json.dumps(content, allow_nan=False, ensure_ascii=False, indent=4).encode("utf-8")
