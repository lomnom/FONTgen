from sys import argv

def read(file,backup):#read file function
	try: #load slot
		with open(file) as content: #save save slot
			return content.read()
	except OSError:
		write(file,backup)
		return backup

def write(file,data): #function to write to file
	with open(file, 'w') as content: #save save slot
		content.write(str(data))
		return True

args=argv #allow modifying of argv
args.pop(0) #remove path of script

from yaml import full_load
path="/Volumes/MINE/CODE/SWIFT/FONTGEN/DONEFONTS.yaml"
with open(path,"r") as file:
	font = full_load(file)

original=font["nothing"]["text"]

target=args.pop() #get target from last arg

for key in args: #get font
	font=font[key]

for command in font:
	toAppend=""
	if command.startswith("appendAfterChar"):
		toAppend=font[command]
	
		words=target.replace(" "," Ϡ").split(" ") #change spaces with Ϡ and split into words
	
		target=[]
		for word in words:
			appendedWord=[]
	
			word=list(word)
	
			if word[0]=="Ϡ":
				space=word.pop(0)
			else:
				space=""
	
			appendedWord=space+toAppend.join(word)+toAppend
			target+=appendedWord
	
		target="".join(target).replace("Ϡ"," ")
	
	if command.startswith("appendBetweenChar"):
		toAppend=font[command]
	
		words=target.replace(" "," Ϡ").split(" ") #change spaces with Ϡ and split into words
	
		target=[]
		for word in words:
			appendedWord=[]
	
			word=list(word)
	
			if word[0]=="Ϡ":
				space=word.pop(0)
			else:
				space=""
	
			appendedWord=space+toAppend.join(word)
			target+=appendedWord
	
		target="".join(target).replace("Ϡ"," ")
	
	if command.startswith("replace"):
		toReplace=font[command]
		normal=toReplace[0].split("Ϡ")
		to=toReplace[1].split("Ϡ")
		for n in range(len(normal)):
			target=target.replace(normal[n],to[n])
	
	if command.startswith("appendAfterAll"):
		toAppend=font[command]
		target=toAppend.join(target)+toAppend
	
	if command.startswith("appendBetween"):
		toAppend=font[command]
		target=toAppend.join(target)
	
	if command.startswith("reverse"):
		if font["reverse"]:
			target=target[::-1]
	
	if command.startswith("appendToEnd"):
		toAppend=font[command]
		target+=toAppend
	
	if command.startswith("appendToStart"):
		toAppend=font[command]
		target=toAppend+target
	
	if command.startswith("appendToStartOfWord"):
		toAppend=font[command]
		wordsTarget=target.replace(" ","Ϡ ").split(" ")
		target=toAppend+toAppend.join(wordsTarget).replace("Ϡ"," ")
	
	if command.startswith("appendToEndOfWord"):
		toAppend=font[command]
		wordsTarget=target.replace(" "," Ϡ").split(" ")
		target=toAppend.join(wordsTarget).replace("Ϡ"," ")+toAppend
	
	if command.startswith("font"):
		fontFace=font[command]
		if "Ϡ" in fontFace:
			fontFace=fontFace.split("Ϡ")
		else:
			fontFace=list(fontFace)
		
		for n in range(len(original)):
			target=target.replace(original[n],fontFace[n])
	
print(target)	