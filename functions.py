from custom_types import *
import accounts

def countries(search: str = ""):
    """
    Returns a list of all countries.
    """
    response = []
    for country_id in os.listdir("./data/"):
        country = accounts.Country(country_id)
        if search == "":
            response.append(country.to_json())
        else:
            search = search.lower()
            searches = [0]
            for v in country.__dict__.values():
                if isinstance(v, Enum):
                    searches.append(WRatio(v.value.lower(), search))
                else:
                    searches.append(WRatio(str(v).lower(), search))
                    
            if max(searches) >= 80:
                response.append(country.to_json())
        
    return response

def country(id: str = ""):
    """
    Returns a country.
    """
    response = accounts.Country(id).to_json()
        
    return response

def countries_geo(id: str = ""):
    """
    Returns a geo of all countries.
    """
    response = {"type": "FeatureCollection", "features": []}
    
    for country_id in os.listdir("./data/"):
        country_geo = json.loads(accounts.CountryGEO(country_id).to_json())
        for f in country_geo:
            response["features"].append(f)
        
    return response

def country_geo(id: str = ""):
    """
    Returns a geo of single country.
    """
    response = accounts.Country(id).to_json()
        
    return response


def valutes(search: str = ""):
    """
    Returns a list of all valutes.
    """
    response = []
    for valute_id in os.listdir("./data/"):
        valute = accounts.Valute(valute_id)
        if valute.check == accounts.Check.QUERY:
            continue
        if search == "":
            response.append(valute.to_json())
        else:
            search = search.lower()
            searches = [0]
            for v in valute.__dict__.values():
                if isinstance(v, Enum):
                    searches.append(WRatio(v.value.lower(), search))
                else:
                    searches.append(WRatio(str(v).lower(), search))
                    
            if max(searches) >= 80:
                response.append(valute.to_json())
        
    return response

def valute(id: str = ""):
    """
    Returns a valute.
    """
    response = accounts.Valute(id).to_json()
        
    return response

def admin(key: str = "", subkey: str = "", value: str = "", id: str = ""):
    if key != "" and subkey != "" and value != "" and id != "":
        if subkey in ["flag", "name", "group", "goverment_type", "goverment_form", "ideology", "political_type" ,"desc", "date", "photo", "change", "abbreviation", "symbol", "id", "cid", "vid"]:
            return {"error_code": 404, "error": "Invalid key, value or account."}
        else:
            account = accounts.User(id)
            if key == "country":
                if subkey == "check":
                    account.country.check = accounts.Check(value)
                else:
                    setattr(account.country, subkey, str(value))
            elif key == "valute":
                if subkey == "check":
                    account.valute.check = accounts.Check(value)
                else:
                    setattr(account.valute, subkey, str(value))
            elif key == "account":
                if subkey == "moderation" or subkey == "banned" or subkey == "admin":
                    setattr(account.account, subkey, value == "true")
                else:
                    setattr(account.account, subkey, str(value))

            account.write()
            return account.to_json()
            
    else:
        return {"error_code": 404, "error": "Invalid key, value or account."}

        
class Settings(BaseSettings):
    api_key: str = os.environ.get("API_KEY")
    api_admin: str = os.environ.get("API_ADMIN")