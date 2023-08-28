from typing import Any
from custom_types import *

class GovermentForm(Enum):
    """
    Constants for Goverment Forms.
    """
    UNKNOWN = "Неизвестно"
    UNITARY = "Унитарная"
    FEDERAL = "Федеративная"
    CONFEDERAL= "Конфедеративная"
    
    UNITARY_ADMIN = "Унитарный"

class GovermentType(Enum):
    """
    Constants for Goverment Types.
    """
    UNKNOWN = "Неизвестно"
    PRESIDENT_RESPUBLIC = "Президентская республика"
    MIXED_RESPUBLIC = "Смешанная республика"
    PARLAMENT_RESPUBLIC = "Парламентская республика"
    PARLAMENT_MONACHY = "Парламентская монархия"
    DUALISTIC_MONACHY = "Дуалистическая монархия"
    ABSOLUTE_MONACHY = "Абсолютная монархия"
    ONE_PARTY_SYSTEM = "Однопартийная система"
    MILITARY_DICTATORSHIP = "Военная диктатура"
    
    ADMIN = "Администический Режим"

class PoliticalType(Enum):
    """
    Constants for Political Types.
    """
    UNKNOWN = "Неизвестно"
    DEMOCRATIC = "Демократический"
    HYBRID = "Гибридный"
    AUTHORITARIAN = "Авторитарный"
    TOTALITARIAN = "Тоталитарный"
    ANARCHY = "Анархия"

class Ideology(Enum):
    """
    Constants for Ideologies.
    """
    NONE = "Отсутствует"
    ANARCHISM = "Анархизм"
    CONSERVATISM = "Консерватизм"
    NEOCONSERVATISM = "Неоконсерватизм"
    LIBERALISM = "Либерализм"
    NEOLIBERALISM = "Неолиберализм"
    LIBERTARIANISM = "Либертарианство"
    MERITOCRACY = "Меритократия"
    ANARCHO_COMMUNISM = "Анархо-коммунизм"
    ANARCHO_CAPITALISM = "Анархо-капитализм"
    MONARCHISM = "Монархизм"
    SOCIAL_DARWINISM = "Социальный дарвинизм"
    SOCIAL_DEMOCRACY = "Социал-демократия"
    SOCIALISM = "Социализм"
    COMMUNISM = "Коммунизм"
    FASCISM = "Фашизм"
    RACISM = "Расизм"
    NAZISM = "Нацизм"
    NATIONALISM = "Национализм"
    CHAUVINISM = "Шовинизм"
    HUMANISM = "Гуманизм"
    FEMINISM = "Феминизм"
    MASCULISM = "Маскулизм"
    TRANSHUMANISM = "Трансгуманизм"
    ECOLISM = "Экологизм"
    
    ADMIN = "Слава Админам"

class Check(Enum):
    """
    Constants for Checks.
    """
    QUERY = "query"
    NO = "no"
    PARTIAL = "partial"
    FULL = "full"


class Account():
    """
    Class for Account.
    """    
    moderation: bool = False
    banned: bool = False
    admin: bool = False
    id: str = "000000000"
    cid: str = "unknown"
    vid: str = "unknown"

    def __init__(self, id: str, registration: bool = False):
        if registration:
            self.moderation = False
            self.banned = False
            self.admin = False
            self.id = id
            self.cid = "unknown"
            self.cid = "unknown"
        else:
            if id in os.listdir("./data/"):
                with open(f"./data/{id}/account.json", "r", encoding="utf8") as f:
                    data = json.loads(f.read())
                    self.moderation = data["moderation"]
                    self.banned = data["banned"]
                    self.admin = data["admin"]
                    self.id = data["id"]
                    self.cid = data["cid"]
                    self.vid = data["vid"]
            else:
                for country_id in os.listdir("./data/"):
                    with open(f"./data/{country_id}/account.json", "r", encoding="utf8") as f:
                        data = json.loads(f.read())
                        if data["id"] == id or data["cid"] == id or data["vid"] == id:
                            self.moderation = data["moderation"]
                            self.banned = data["banned"]
                            self.admin = data["admin"]
                            self.id = data["id"]
                            self.cid = data["cid"]
                            self.vid = data["vid"]
                            
                            break
                else:
                    self.error_code = 404
                    self.error = "Account not found"
            
    def to_json(self):
        if "error" in self.__dict__:
            return {
                "error_code": self.error_code,
                "error": self.error
            }
        else:
            return {
                "moderation": self.moderation,
                "banned": self.banned,
                "admin": self.admin,
                "id": self.id,
                "cid": self.cid,
                "vid": self.vid
            }
            


class Country():
    """
    Class for Country.
    """   
    id: str = "000000000"
    cid: str = "unknown"
    name: str = "Неизвестная страна"
    flag: str = "/static/images/defaults/profile_flag.png"
    group: str = "unknown"
    goverment_form: GovermentForm = GovermentForm.UNITARY
    goverment_type: GovermentType = GovermentType.PRESIDENT_RESPUBLIC
    political_type: PoliticalType = PoliticalType.DEMOCRATIC
    ideology: Ideology = Ideology.NONE
    desc: str = ""
    date: date = date(2000, 1, 1)
    add: str = ""
    check: Check = Check.NO
    
    def __init__(self, id: str, registration: bool = False):
        account = Account(id, registration)
        if "error" in account.__dict__:
            self.error_code = account.error_code
            self.error = account.error
        if account.id != "000000000" and not registration:
            with open(f"./data/{account.id}/country.json", "r", encoding="utf8") as f:
                data = json.loads(f.read())
                self.id = account.id
                self.cid = account.cid
                self.name = data["name"]
                self.flag = data["flag"]
                self.group = data["group"]
                try:
                    self.goverment_form = GovermentForm(data["goverment_form"])
                except:
                    self.goverment_form = GovermentForm.UNKNOWN
                try:
                    self.goverment_type = GovermentType(data["goverment_type"])
                except:
                    self.goverment_type = GovermentType.UNKNOWN
                try:
                    self.political_type = PoliticalType(data["political_type"])
                except:
                    self.political_type = PoliticalType.UNKNOWN
                try:
                    self.ideology = Ideology(data["ideology"])
                except:
                    self.ideology = Ideology.NONE
                self.desc = data["desc"]
                try:
                    self.date = datetime.strptime(data["date"], '%d.%m.%Y').date()
                except:
                    self.date = date(2000, 1, 1)
                self.add = data["add"]
                try:
                    self.check = Check(data["check"])
                except:
                    self.check = Check.QUERY
        
        
        if registration:
            self.id = id
            self.cid = "unknown"
            self.name = ""
            self.flag = ""
            self.group = "unknown"
            self.goverment_form = GovermentForm.UNITARY
            self.goverment_type = GovermentType.PRESIDENT_RESPUBLIC
            self.political_type = PoliticalType.DEMOCRATIC
            self.ideology = Ideology.NONE
            self.desc = ""
            self.date = date(2000, 1, 1)
            self.add = ""
            self.check = Check.NO
            
    def to_json(self):
        if "error" in self.__dict__:
            return {
                "error_code": self.error_code,
                "error": self.error
            }
        else:
            return {
                "id": self.id,
                "cid": self.cid,
                "name": self.name,
                "flag": self.flag,
                "group": self.group,
                "goverment_form": self.goverment_form.value,
                "goverment_type": self.goverment_type.value,
                "political_type": self.political_type.value,
                "ideology": self.ideology.value,
                "desc": self.desc,
                "date": self.date.strftime('%d.%m.%Y'),
                "add": self.add,
                "check": self.check.value
            }
            
class CountryGEO():
    """
    Class for Country geojson.
    """   
    id: str = "000000000"
    data: list = []
    
    def __init__(self, id: str):
        account = Account(id, False)
        if "error" in account.__dict__:
            self.error_code = account.error_code
            self.error = account.error
        if account.id != "000000000":
            self.id = account.id
            if os.path.exists(f"./data/{account.id}/geo.geojson"):
                with open(f"./data/{account.id}/geo.geojson", "r", encoding="utf8") as f:
                    self.data = json.loads(f.read())["features"]
            
    def to_json(self):
        if "error" in self.__dict__:
            return {
                "error_code": self.error_code,
                "error": self.error
            }
        else:
            return json.dumps(self.data, indent=4, ensure_ascii=False)
        
    def write(self):
        with open(f"./data/{self.id}/geo.geojson", "w", encoding="utf8") as f:
            f.write(self.data)
                
                
class Valute():
    """
    Class for Valute.
    """   
    id: str = "000000000"
    vid: str = "unknown"
    name: str = "Неизвестно"
    photo: str = "/static/images/defaults/profile_photo.png"
    desc: str = ""
    change: float = 0.0
    abbreviation: str = "UNK"
    symbol: str = "U"
    add: str = ""
    check: Check = Check.QUERY
    
    def __init__(self, id: str, registration: bool = False):
        account = Account(id, registration)
        if "error" in account.__dict__:
            self.error_code = account.error_code
            self.error = account.error
        if account.id != "000000000" and not registration:
            with open("./data/"+account.id+"/valute.json", "r", encoding="utf8") as f:
                data = json.loads(f.read())
                self.id = account.id
                self.vid = account.vid
                self.name = data["name"]
                self.photo = data["photo"]
                self.desc = data["desc"]
                self.change = data["change"]
                self.abbreviation = data["abbreviation"]
                self.symbol = data["symbol"]
                self.add = data["add"]
                try:
                    self.check = Check(data["check"])
                except:
                    self.check = Check.QUERY
        if registration:
            self.id = id
            self.vid = "unknown"
            self.name = ""
            self.photo = ""
            self.desc = ""
            self.change = 0
            self.abbreviation = ""
            self.symbol = ""
            self.add = ""
            self.check = Check.NO

                
    def to_json(self):
        if "error" in self.__dict__:
            return {
                "error_code": self.error_code,
                "error": self.error
            }
        else:
            return {
                "id": self.id,
                "vid": self.vid,
                "name": self.name,
                "photo": self.photo,
                "desc": self.desc,
                "change": self.change,
                "abbreviation": self.abbreviation,
                "symbol": self.symbol,
                "add": self.add,
                "check": self.check.value
            }

class User():
    """
    Class for full User Data.
    """   
    account: Account = Account("000000000")
    country: Country = Country("000000000")
    valute: Valute = Valute("000000000")
    
    def __init__(self, id: str):
        self.account = Account(id)
        self.country = Country(id)
        self.valute = Valute(id)
        if "error" in self.account.__dict__:
            self.error_code = self.account.error_code
            self.error = self.account.error
        
    def to_json(self):
        if "error" in self.__dict__:
            return {
                "error_code": self.error_code,
                "error": self.error
            }
        else:
            return {
                "account": self.account.to_json(),
                "country": self.country.to_json(),
                "valute": self.valute.to_json()
            }

    def write(self):
        if not "error" in self.account.__dict__:
            with open(f"./data/{self.account.id}/account.json", "w", encoding="utf8") as f:
                f.write(json.dumps(self.account.to_json(), indent=4, ensure_ascii=False))
            with open(f"./data/{self.account.id}/country.json", "w", encoding="utf8") as f:
                f.write(json.dumps(self.country.to_json(), indent=4, ensure_ascii=False))
            with open(f"./data/{self.account.id}/valute.json", "w", encoding="utf8") as f:
                f.write(json.dumps(self.valute.to_json(), indent=4, ensure_ascii=False))

            return self
    
