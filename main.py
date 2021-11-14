# 
#			PyDirbuster - 2.0.3
#
#							   - made by ducky
#
#
#	PyDirbuster is an open source tool created and maintained
#	by Ducky#9982, if you have any questions with safety of
#	this product as well as any suggestions for additions,
#	please contact Ducky on discord or open a new issue on github
#
#
#

from requests import get, exceptions
from sys import argv
from art import tprint

version = "1.0.0"
deep = list()

def main(url, wordlist = ".\\wordlists\\pydirbuster_wordlist_small.txt"):
	with open(wordlist) as words:

			words = (words.read()).splitlines()

			print(f"WORDLIST: {wordlist}")
			print(f"WORDLIST LINES: {len(words)}")
			print(f"URL: {url}")
			print("---------------]\n\nBusting Directories...\n")

			for count in words:
				try:
					res = get(url=url+count)
				except exceptions.ConnectionError:
					print(f"Unable to reach given url: {url}")
					quit()

				if "200" in str(res):
					print(f"{url}{count}")
					deep.append(url+count)

			for count in words:
				try:
					res = get(url=deep+"/"+count)
				except exceptions.ConnectionError:
					print(f"Unable to reach given url: {url}")
					quit()

			print("\nFinished scanning. All URL's returned back have returned HTML Response Code 200")


if __name__ == "__main__":

	tprint(f"PyDirbuster              {version}")
	print("-------------------------------------------------------------------------------------------------------\n\n")
	print("[---------------")



	if len(argv) == 1:
		print("usage: python3 main.py <url> [./path/to/wordlist.txt]")
		print("---------------]")

	elif len(argv) == 2:

		if "http" not in argv[1]:
			print("Not a valid url. please make sure you have the `http://` or `https://` prefix in it.")
			print("---------------]")
			quit()

		if "/" not in (argv[1])[-1]:
			argv[1] = argv[1] + "/"

		main(argv[1])

	elif len(argv) == 3:

		if "http" not in argv[1]:
			print("Not a valid url. please make sure you have the `http://` or `https://` prefix in it.")
			print("---------------]")
			quit()
			
		if "/" not in (argv[1])[-1]:
			argv[1] = argv[1] + "/"

		main(argv[1], argv[2])

	else:
		print("usage: python3 main.py <url> [./path/to/wordlist.txt]")