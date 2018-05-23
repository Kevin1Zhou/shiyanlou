#!/usr/bin/env/ python3
import sys

def copyfile(src,dst):
	with open(src,'r') as srcfile:
		with open(dst,'w') as dstfile:
			dstfile.write(srcfile.read())
if __name__ == '__main__':
	if len(sys.argv) == 3:
		copyfile(sys.argv[1],sys.argv[2])
	else:
		print("Parameter Error")
		print(sys.argv[0], "srcfile dstfile")
		sys.exit(-1)


