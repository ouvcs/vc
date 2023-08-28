from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import *
from pydantic_settings import BaseSettings
from enum import Enum
from datetime import date, datetime
from urllib.parse import ParseResult, urlparse
from fuzzywuzzy.fuzz import WRatio
import os
import json

class PrettyJSONResponse(Response):
    media_type = "application/json"
    
    def render(self, content: Any) -> bytes:
        return json.dumps(content, allow_nan=False, ensure_ascii=False, indent=4).encode("utf-8")
