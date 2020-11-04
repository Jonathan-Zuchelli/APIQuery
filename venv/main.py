from requests import post
from base64 import b64encode

authentication = "Regression:f8cd3f4554f74a89bdb625bc".encode("utf-8")
encryptedAuth = b64encode(authentication)

r = post("https://ccm.cps.golf/RegressionSRCCM/Transactions.svc/GetTerminalIdentifiers",
          headers={"Authorization": encryptedAuth})

print(r.json())
