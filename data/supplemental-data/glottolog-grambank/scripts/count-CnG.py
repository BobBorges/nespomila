#!/usr/bin/env python3
from tqdm import tqdm
import pandas as pd
import os, json




def is_binary(v):
	try:
		v = int(v)
		if v == 1 or v == 0:
			return True
		else:
			return False
	except:
		return False




def calculate_percent(GBs):
	for gb, info in GBs.items():
		T = sum(info["values"].values())
		info["percent"]["absent"] = (info["values"][0]/T)*100
		info["percent"]["present"] = (info["values"][1]/T)*100
		info["percent"]["other"] = (info["values"]["other"]/T)*100
	return GBs



def calculate_gender_agreement(GBs):
	ag = ["GB170", "GB171", "GB172"]
	agrees = []
	for f in ag:
		for v in GBs[f]["present"]:
			if v not in agrees:
				agrees.append(v)
	return len(agrees)

def main():
	GBs = {
		"GB070": {
			"description": "Are there morphological cases for non-pronominal core arguments (i.e. S, A or P)?",
			"values": {
				0:0,
				1:0,
				"other": 0
			},
			"present": [],
			"percent": {
				"absent": None,
				"present": None,
				"other": None
			}
		}, 
		"GB051": {
			"description": "Is there a noun class/gender system where masculine and feminine categories are a factor in class assignment?",
			"values": {
				0:0,
				1:0,
				"other": 0
			},
			"present": [],
			"percent": {
				"absent": None,
				"present": None,
				"other": None
			}
		}, 
		"GB052": {
			"description": "Is there a noun class/gender system where shape is a factor in class assignment?",
			"values": {
				0:0,
				1:0,
				"other": 0
			},
			"present": [],
			"percent": {
				"absent": None,
				"present": None,
				"other": None
			}
		}, 
		"GB053": {
			"description": "Is there a noun class/gender system where animacy is a factor in class assignment?",
			"values": {
				0:0,
				1:0,
				"other": 0
			},
			"present": [],
			"percent": {
				"absent": None,
				"present": None,
				"other": None
			}
		}, 
		"GB170": {
			"description": "Can an adnominal property word agree with the noun in noun class/gender?",
			"values": {
				0:0,
				1:0,
				"other": 0
			},
			"present": [],
			"percent": {
				"absent": None,
				"present": None,
				"other": None
			}
		}, 
		"GB171": {
			"description": "Can an adnominal demonstrative agree with the noun in noun class/gender?",
			"values": {
				0:0,
				1:0,
				"other": 0
			},
			"present": [],
			"percent": {
				"absent": None,
				"present": None,
				"other": None
			}
		}, 
		"GB172": {
			"description": "Can an article agree with the noun in noun class/gender?",
			"values": {
				0:0,
				1:0,
				"other": 0
			},
			"present": [],
			"percent": {
				"absent": None,
				"present": None,
				"other": None
			}
		}, 
		"GB192": {
			"description": "Is there a gender system where a noun's phonological properties are a factor in class assignment?",
			"values": {
				0:0,
				1:0,
				"other": 0
			},
			"present": [],
			"percent": {
				"absent": None,
				"present": None,
				"other": None
			}
		},
		"GB321": {
			"description": "Is there a large class of nouns whose noun class/gender is not phonologically or semantically predictable?",
			"values": {
				0:0,
				1:0,
				"other": 0
			},
			"present": [],
			"percent": {
				"absent": None,
				"present": None,
				"other": None
			}
		}
	}

	"""
	## Github version

	tsvdir = "original_sheets"
	tsvs = os.listdir(tsvdir)
	tsvs = [t for t in tsvs if t != '.gitattributes']
	for tsv in tqdm(tsvs, total=len(tsvs)):
		df = pd.read_csv(f'{tsvdir}/{tsv}', sep='\t')
		for gb, gbinfo in GBs.items():
			filtered = df[df["Feature_ID"] == gb]
			if not filtered.empty:
				v = filtered.iloc[0]["Value"]
				if is_binary(v):
					gbinfo['values'][int(v)] +=1
					if int(v) == 1:
						gbinfo['present'].append(tsv.split('_')[1][:-4])		
				else:
					gbinfo['values']['other'] +=1
			else:
				gbinfo['values']['other'] +=1
	"""

	# v1.0.3
	df = pd.read_csv("../grambank-v1.0.3/grambank-grambank-7ae000c/cldf/values.csv")
	langs = df["Language_ID"].unique()
	params = df["Parameter_ID"].unique()
	print(len(params))
	print(langs)
	print(type(langs))
	print(len(langs))
	for feature, f_info in GBs.items():
		sub_df = df[df["Parameter_ID"] == feature]
		print(f"    ---|  {feature}  |---")
		VC = sub_df['Value'].value_counts()
		print(VC)
		for i, v in VC.items():
			idx = None
			if i == "?":
				idx = "other"
			else:
				idx = int(i)
			f_info["values"][idx] = v
			if idx == 1:
				[f_info["present"].append(_) for _ in list(sub_df.loc[sub_df["Value"] == str(idx), "Language_ID"].unique())]


	gender_agreement = calculate_gender_agreement(GBs)
	#print(f"There are {gender_agreement} languages that employ some gender agreement across the NP -- {(gender_agreement/len(tsvs))*100}%") # github
	print(f"There are {gender_agreement} languages that employ some gender agreement across the NP -- {(gender_agreement/len(langs))*100}%") # v1.0.3
	# Github: There are 770 languages that employ some gender agreement across the NP -- 25.62396006655574%
	# v1.0.3: There are 643 languages that employ some gender agreement across the NP -- 26.06404539927037%
	print("More details in `IO/case-gender_counts.json`.")

	GBs = calculate_percent(GBs)
	#with open("IO/case-gender_counts_v-github.json", "w+") as outf:
	with open("IO/case-gender_counts_v1.0.3.json", "w+") as outf:
		json.dump(GBs, outf, indent=4)




if __name__ == '__main__':
	main()
