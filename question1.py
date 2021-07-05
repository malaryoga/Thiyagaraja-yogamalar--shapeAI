import hashlib
def main():
	text="Hi Shape AI!"
	textUtf8 =text.encode("Utf-8")
	hash = hashlib.md5(textUtf8)
	hexa = hash.hexdigest()
	print(hexa)
	return

main()
