#!/usr/bin/env python3
import os

def main():
	tsvdir = "/home/bob/Projects/Grambank/original_sheets"
	tsvs = os.listdir(tsvdir)
	tsvs = [t for t in tsvs if t != '.gitattributes']
	tsvs = [t.split('_')[1][:-4] for t in tsvs]
	with open("IO/langoids.txt", "w+") as outf:
		[outf.write(f"{t}\n") for t in tsvs]


if __name__ == '__main__':
	main()
