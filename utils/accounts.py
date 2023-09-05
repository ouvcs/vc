from .settings import settings
from .custom_types import *

class User():
    account: dict = {}
    country: dict = {}
    valute: dict = {}
    
    def __init__(self, id: str, registration: bool = False, need_vk: bool = False):
        if id.endswith(".json"):
            id = id[:-5]
        if registration:
            os.mkdir(f"./accounts/{id}")
            with open(f"./accounts/000000000.json", "r", encoding="utf8") as f:
                account = json.loads(f.read())
                self.account = account["account"]
                self.country = account["country"]
                self.valute = account["valute"]
            self.write()
        else:
            if not id in os.listdir("./accounts/"):
                for id_ in os.listdir("./accounts/"):
                    with open(f"./accounts/{id_}", "r", encoding="utf8") as f:
                        account = json.loads(f.read())
                        if account["account"]["id"] == id or account["account"]["cid"] == id or account["account"]["vid"] == id:
                            self.account = account["account"]
                            self.country = account["country"]
                            self.valute = account["valute"]
                            break
                else:
                    with open(f"./accounts/000000000.json", "r", encoding="utf8") as f:
                        account = json.loads(f.read())
                        self.account = account["account"]
                        self.country = account["country"]
                        self.valute = account["valute"]
            else:
                with open(f"./accounts/{id}.json", "r", encoding="utf8") as f:
                    account = json.loads(f.read())
                    self.account = account["account"]
                    self.country = account["country"]
                    self.valute = account["valute"]
        
        if need_vk:
            self.vk_needed()
                
    def to_json(self):
        if not "name" in self.account:
            self.vk_needed()
        return {"account": self.account, "country": self.country, "valute": self.valute}
                
    def write(self):
        if not "name" in self.account:
            self.vk_needed()
            
        self.country["id"] = self.account["id"]
        self.valute["id"] = self.account["id"]
        self.country["cid"] = self.account["cid"]
        self.valute["vid"] = self.account["vid"]
        
        with open(f"./accounts/{self.account['id']}.json", "w", encoding="utf8") as f:
            f.write(json.dumps({"account": self.account, "country": self.country, "valute": self.valute}, indent=4, ensure_ascii=False))
            
        return self
    
    def vk_needed(self):
        vkresponse = requests.get(f"https://api.vk.com/method/users.get?user_ids={str(self.account['id'])}&fields=photo_200,screen_name&access_token={settings.vk_admin}&v=5.131").json()
        try:
            self.account["name"] = vkresponse["response"][0]["first_name"] + " " + vkresponse["response"][0]["last_name"]
            self.account["screen_name"] = vkresponse["response"][0]["screen_name"]
            self.account["photo"] = vkresponse["response"][0]["photo_200"]
        except Exception as e:
            print(vkresponse)
            print(e)
            self.account["name"] = "Неизвестно"
            self.account["screen_name"] = "unknown"
            self.account["photo"] = "/static/images/defaults/profile.png"