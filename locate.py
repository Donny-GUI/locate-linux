import os
from sys import argv
from rich.console import Console
from rich.status import Status

try:
	target = argv[1]
except IndexError:
	print("Please provide a target")
	exit()

green = "\033[32m"
red = "\033[31m"
yellow = "\033[33m"
endc = "\033[0m"

def main():
	console = Console()
	with Status(status=f"Searching main drive for {target}", spinner='dots') as status:
		file_count = 0
		for root, dirs, files in os.walk("/"):
			for file in files:
				current_file = f"{root}/{file}"
				if file == target:
					if file_count%2:
						print(f"[{red}{file_count}{endc}]  {green}{current_file}{endc}")
					else:
						print(f"[{red}{file_count}{endc}]  {yellow}{current_file}{endc}")
					file_count+=1

if __name__ == '__main__':
	main()
