import urllib.request, urllib.error, pytube.exceptions
from pytube import YouTube
from pprint import pprint

# Install pytube
# pip install pytube

print("""
	[\033[36m+\033[0;0m] Baixar videos do Youtube - Dyou.py 1.0v
	[\033[36m+\033[0;0m] By : \033[36mLuisSilva\033[0;0m
	[\033[36m+\033[0;0m] Pasta padrão : tmp
	""")

def Dyou():
	link = input("URL: ")
	if not "https://" in link:
		link = "https://"+link
	else:
		link = link
	try:
		urllib.request.urlopen(link)
		
		url = YouTube(link)
		print("\n\033[36mNome\033[0;0m: \n\033[31m", url.filename, "\033[0;0m")
		print("\033[36mformatos:\033[0;0m")
		pprint(url.get_videos())

		try:
			formato = input("Formato: exemplo: \033[31mmp4\033[0;0m\n")
			resolucao = input("Resolução: exemplo: \033[31m720p\033[0;0m\n")
			print ("Você escolheu :\033[36m", formato+", "+resolucao, "\033[0;0m")
			video = url.get(formato, resolucao)
			print("[Baixando...!]")
			video.download("/tmp/")
			print("[Download concluido]")
		except pytube.exceptions.DoesNotExist:
			print("Formato não valido!")

	except (urllib.error.HTTPError, urllib.error.URLError, urllib.error.ContentTooShortError):
		print(link, "\nNome: \n\033[31m[Não válido]\033[0;0m")
Dyou()
