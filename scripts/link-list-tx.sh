#!/bin/bash

##################################################
#												 #
# This script links data files from the working  #
# environment to this archive repository.        #
#                                                #
##################################################

NES="/home/bob/NESPOMILA/project-data/transcriptions/"
NSW="/home/bob/NESPOMILA/HVC-stuff/post-analyses/HVC-transcriptions/"
CSB="/home/bob/NESPOMILA/csb-pilot/csb-pilot-data/transcriptions/"

NESlist="data/NESPOMILA-transcriptions.txt"
NSWlist="data/NSW-HVC-transcriptions.txt"
CSBlist="data/CSB-pilot-transcriptions.txt"

outdir="data/transcriptions/"




do_NES () {
	for f in $NES* ; do
		fbase=$(basename $f)
		echo $fbase;
		mkdir $outdir$fbase
		echo $ourdir$fbase/$fbase.eaf >> $NESlist
		ln $NES$fbase/$fbase.eaf $outdir$fbase/$fbase.eaf
	done
}




do_NSW () {
	for f in $NSW* ; do
		fbase=$(basename $f)
		echo $fbase;
		mkdir $outdir$fbase
		echo $ourdir$fbase/$fbase.eaf >> $NSWlist
		ln $NSW$fbase/$fbase.eaf $outdir$fbase/$fbase.eaf
	done
}




do_CSB () {
	for f in $CSB* ; do
		fbase=$(basename $f)
		echo $fbase;
		mkdir $outdir$fbase
		echo $ourdir$fbase/$fbase.eaf >> $CSBlist
		ln $CSB$fbase/$fbase.eaf $outdir$fbase/$fbase.eaf
	done
}




do_NES
do_NSW
do_CSB
