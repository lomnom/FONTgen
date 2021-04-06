from benedict import benedict
path="/Volumes/MINE/CODE/SWIFT/FONTGEN/TEST.yaml"
font=benedict.from_yaml(path) #load yaml

target="Cwm fjord bank glyphs vext quiz"
fontFolder=font["all"]
original=fontFolder["text"]

def main(font,target,fontFolder,original,key):
	if not (key.endswith("-appendToStart") or key.endswith("-appendToEnd") or key.endswith("-reverse") or key.endswith("-appendAfterAll") or key.endswith("-appendBetween") or key.endswith("-appendToStartOfWord") or key.endswith("-appendToEndOfWord") or key.endswith("appendBetweenChar") or key.endswith("-appendAfterChar") or key.endswith("replace")):
		print(key)
		try: #replace
			toReplace=fontFolder[fontName+"-replace"]
			normal=toReplace[0].split("Ϡ")
			to=toReplace[1].split("Ϡ")
			for n in range(len(normal)):
				target=target.replace(normal[n],to[n])
		except:
			pass

		try: #appendBetweenChar
			toAppend=fontFolder[fontName+"-appendBetweenChar"]
	
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
		except:
			pass

		try: #appendAfterChar
			toAppend=fontFolder[fontName+"-appendAfterChar"]
	
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
		except:
			pass
	
		try: #appendAfterAll
			toAppend=fontFolder[fontName+"-appendAfterAll"]
			target=toAppend.join(target)+toAppend
		except:
			pass
	
		try: #appendBetween
			toAppend=fontFolder[fontName+"-appendBetween"]
			target=toAppend.join(target)
		except:
			pass
	
		try: #reverse
			fontFolder[fontName+"-reverse"]
			target=target[::-1]
		except:
			pass
	
		try: #appendToEnd
			toAppend=fontFolder[fontName+"-appendToEnd"]
			target+=toAppend
		except:
			pass
	
		try: #appendToStart
			toAppend=fontFolder[fontName+"-appendToStart"]
			target=toAppend+target
		except:
			pass
	
		try: #appendToStartOfWord
			toAppend=fontFolder[fontName+"-appendToStartOfWord"]
			wordsTarget=target.replace(" ","Ϡ ").split(" ")
			target=toAppend+toAppend.join(wordsTarget).replace("Ϡ"," ")
		except:
			pass
	
		try: #appendToEndOfWord
			toAppend=fontFolder[fontName+"-appendToEndOfWord"]
			wordsTarget=target.replace(" "," Ϡ").split(" ")
			target=toAppend.join(wordsTarget).replace("Ϡ"," ")+toAppend
		except:
			pass
	
		if not fontFolder[fontName]=="none":
			font=fontFolder[fontName]
			if "Ϡ" in font:
				font=font.split("Ϡ")
			else:
				font=list(font)

			for n in range(len(original)):
				target=target.replace(original[n],font[n])
	
		print(target+"\n")	

for key in fontFolder:
	fontName=key
	main(font,target,fontFolder,original,key)
