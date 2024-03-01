import requests
from requests.structures import CaseInsensitiveDict

url = "https://apps.allianz.be/GSERest/api/GetBrokerDetails?postal_code=1000&broker_id=NULL&product_code=NULL&search_type=Broker&lang_code=NL&country_code=BE"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"


resp = requests.get(url, headers=headers)

print(resp.content)