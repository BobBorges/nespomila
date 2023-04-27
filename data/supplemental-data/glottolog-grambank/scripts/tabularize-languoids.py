#!/usr/bin/env python3
#from pyglottolog import Glottolog
from tqdm import tqdm
import glob, os
import pandas as pd


with open("/home/bob/Projects/Grambank/IO/langoids.txt", "r") as inf:
	grambank_languoids = inf.readlines()
	grambank_languoids = [_.strip() for _ in grambank_languoids] 

def main():
	
	languoid_paths = []
	start_dir = os.getcwd()
	os.chdir("/home/bob/Projects/glottolog/languoids/tree")
	print("Finding paths...")
	for l in tqdm(grambank_languoids, total=len(grambank_languoids)):
		p_list = glob.glob(f"**/{l}", recursive=True)
		[languoid_paths.append(p) for p in p_list]

	os.chdir(start_dir)

	with open("IO/languoid-path-list.txt", "w+") as outf:
		[outf.write(f"{l}\n") for l in languoid_paths]
	"""
	with open("IO/languoid-path-list.txt", "r+") as inf:
		languoid_paths = inf.readlines()
		languoid_paths = [l.strip() for l in languoid_paths]
	"""

	max_len=0
	rows = []
	print("Splitting into family info...")
	for lp in tqdm(languoid_paths, total=len(languoid_paths)):
		spl = lp.split('/')
		if max_len < len(spl):
			max_len = len(spl)
		rows.append(spl)

	print("Padding rows...")
	rows2 = []
	for row in rows:
		while len(row) < max_len:
			row.insert(-1, None)
		print(len(row))
		rows2.append(row)
			
	print("Writing...")
	cols = []
	for i in range(max_len-1):
		cols.append(f"node_{i}")
	cols.append("leaf")
	print(len(cols), cols)

	df = pd.DataFrame(rows2, columns=cols)
	df.to_csv("IO/tabular-languoids.csv", index=False)
	print("done")



if __name__ == '__main__':
	main()
