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

v = '1.0.0' # sets the version of the program
layer2 = list() # creates a variable called layer2 and makes it an empty array

def main(url, wordlist = "wordlists/pydirbuster_wordlist_small.txt"): # defines the main function and adds a default wordlist to the parameters
	with open(wordlist) as words: # opens the wordlist file

		words = (words.read()).splitlines() # reads all the lines one by one in the wordlist

		print(f"WORDLIST: {wordlist}")										# tells you what wordlist you are using
		print(f"WORDLIST LINES: {len(words)}")								# tells you how many words/lines are in the wordlist
		print(f"URL: {url}")												# returns the current victim url
		print("-----------------------------]\n\nBusting Directories...\n")	# aesthetics

		for count in words: # iterates through all the words
			try: # catches any errors
				res = get(url=url+count) # sends a response to the given url with the word
				if "200" in str(res): # checks if the url is valid
					print(f"{url}{count}") # if the url is valid, it prints the url onto the screen
					layer2.append(url+count) # appends the valid url to the layer2 array

				res = get(url=url+count+".html") # ", more checks
				if "200" in str(res):
					print(f"{url}{count}.html")
					layer2.append(url+count)

				res = get(url=url+count+"/") # ", more checks
				if "200" in str(res):
					print(f"{url}{count}/")
					layer2.append(url+count)

			except exceptions.ConnectionError: # if an error is in the above code, where you can not access the url, this fallback code will run
				print(f"Unable to reach given url: {url}") # tells the user which url can't be accessed
				quit() # quits the program

		for count in words:
			try:

				for l2 in layer2:

					res = get(url=l2+"/") # TypeError: can only concatenate list (not "str") to list
					if "200" in str(res):
						print(f"{url}{count}/{count}")

					res = get(url=l2+"/"+count+".html")
					if "200" in str(res):
						print(f"{url}{count}/{count}.html")

			except exceptions.ConnectionError: # if an error is in the above code, where you can not access the url, this fallback code will run
				print(f"Unable to reach given url: {url}") # tells the user which url can't be accessed
				quit() # quits the program


		print("\nFinished scanning. All URL's returned back have given a HTML Response Code of 200") # aesthetic

if __name__ == '__main__':

	tprint(f"PyDirbuster         {v}")
	print("-------------------------------------------------------------------------\n\n")
	print("[-----------------------------")

	if len(argv) == 1: # checks if user has inputted anything as an argument
		print("usage: python main.py <url> [./path/to/wordlist.txt]")
		quit()

	elif len(argv) == 2: # checks if user has added a url but not wordlist

		if "http" not in argv[1]:
			print("Not a valid url. please make sure you have the `http://` or `https://` prefix in it.")
			print("-----------------------------]")
			quit()

		if "/" not in (argv[1])[-1]:
			argv[1] = argv[1] + "/"

		main(argv[1])

	elif len(argv) == 3: # checks if user has added a url and wordlist

		if "http" not in argv[1]:
			print("Not a valid url. please make sure you have the `http://` or `https://` prefix in it.")
			print("-----------------------------]")
			quit()

		if "/" not in (argv[1])[-1]:
			argv[1] = argv[1] + "/"

		main(argv[1], argv[2])

	else:

		print("usage: python main.py <url> [./path/to/wordlist.txt]")

###								###
###			END OF PROGRAM 		###
###								###
