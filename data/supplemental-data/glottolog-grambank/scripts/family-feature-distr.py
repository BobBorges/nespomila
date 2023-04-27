#!/usr/bin/env python3
import pandas as pd
from pyglottolog import Glottolog
g = Glottolog('/home/bob/Projects/glottolog')

GBs = {
	"GB070": {
		"description": "Are there morphological cases for non-pronominal core arguments (i.e. S, A or P)?"
	}, 
	"GB051": {
		"description": "Is there a noun class/gender system where masculine and feminine categories are a factor in class assignment?"
	}, 
	"GB052": {
		"description": "Is there a noun class/gender system where shape is a factor in class assignment?"
	}, 
	"GB053": {
		"description": "Is there a noun class/gender system where animacy is a factor in class assignment?"
	}, 
	"GB170": {
		"description": "Can an adnominal property word agree with the noun in noun class/gender?"
	}, 
	"GB171": {
		"description": "Can an adnominal demonstrative agree with the noun in noun class/gender?"
	}, 
	"GB172": {
		"description": "Can an article agree with the noun in noun class/gender?"
	}, 
	"GB192": {
		"description": "Is there a gender system where a noun's phonological properties are a factor in class assignment?"
	},
	"GB321": {
		"description": "Is there a large class of nouns whose noun class/gender is not phonologically or semantically predictable?"
	}
}


def main():
	df = pd.read_csv("IO/featureized-languoids.csv")
	uc = pd.DataFrame(df.node_0.value_counts())
	#print(type(uc), uc)
	largest_fam = uc[uc['count'] > 100]
	
	node_0_names = list(largest_fam.index.unique())
	print("* Families:")
	[print(f"\t{g.languoid(_).name}\n") for _ in node_0_names]

	for f, ff in GBs.items():
		print('\n\n')
		print("*", f, ff['description'])
		for n in node_0_names:
			x = df[df['node_0'] == n]
			#print(x)
			try:
				n = g.languoid(n).name
			except:
				pass 
			print('**', n, x[f'{f}'].value_counts())
			node_1_names = list(x.node_1.unique())
			for nn in node_1_names:
				xx = x[x['node_1'] == nn]
				try:
					nn = g.languoid(nn).name
				except:
					pass
				print('*** ---->', nn, xx[f'{f}'].value_counts())
				node_2_names = list(xx.node_2.unique())
				for nnn in node_2_names:
					xxx = xx[xx['node_2'] == nnn]
					try:
						nnn = g.languoid(nnn).name
					except:
						pass
					print('**** -------->', nnn, xxx[f'{f}'].value_counts())
					node_2_names = list(xx.node_2.unique())

			print("\n\n==============================\n\n")




if __name__ == '__main__':
	main()
