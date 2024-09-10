"""
CS50 task1.3
Checking string values.
"""


def get_mime(file_type: str) -> str:
	mime_types = {
		".gif": "image/gif",
		".jpg": "image/jpeg",
		".jpeg": "image/jpeg",
		".png": "image/png",
		".pdf": "application/pdf",
		".txt": "text/plain",
		".zip": "application/zip",
	}
	return mime_types[f".{file_type}"]


def get_extension(file_name: str) -> str:
	if "." in file_name:
		return file_name.split(".")[-1]
	else:
		raise ValueError("Invalid file name.")


def main():
	file_name = input("Enter file name: ")
	try:
		print(get_mime(get_extension(file_name)))
	except (ValueError, KeyError):
		print("Invalid file name.")


if __name__ == "__main__":
	main()
