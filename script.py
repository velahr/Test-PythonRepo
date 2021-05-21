

import requests

#print(sys.version) 


#name = input("Your Name? ")
#print("Hello,", name)




r = requests.get("https://coreyms.com")
print(r.status_code)
## print(greet("World"))
## print(greet("Henry"))
