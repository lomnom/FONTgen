from sys import argv
from yaml import full_load, dump

def write(file,data): #function to write to file
	with open(file, 'w') as content: #save save slot
		content.write(str(data))
		return True

path="/Volumes/MINE/CODE/SWIFT/FONTGEN/TEST.yaml"
with open(path,"r") as file:
	font = full_load(file)

if argv[1]=="addUser":
	if not argv[2] in font:
		font[argv[2]]={"none":{"none":{"font": "none"}}}
	else:
		print("user already exists.")

elif argv[1]=="deleteUser": #deleteUser user
	if argv[2] in font:
		del font[argv[2]]
	else:
		print("user not found!!")

elif argv[1]=="addTransformer": #addTransformer user folder name data
	try: 
		font[argv[2]][argv[3]][argv[4]]
	except:
		font[argv[2]][argv[3]][argv[4]]=argv[5]

write("TEST.yaml",dump(font, default_flow_style=False,allow_unicode=True))
