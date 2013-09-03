#! /usr/bin/python

# .I Identity
# .T Title
# .A Author
# .W Content

fi = open("cacm.all", "r")
fo = open("cacm.xml", "w")
line = fi.readline()
while line:
	words = line.split()
	while words[0] == ".I":
		fo.write("<file>\n\t<index>" + words[1] + "</index>\n")
		line = fi.readline()
		words = line.split()
		if words[0] == ".T":
			fo.write("\t<Title>\n")
			line = fi.readline()
			if line:
				words = line.split()
			while words[0] != ".W" and words[0] != ".B":
				fo.write("\t\t" + line)
				line = fi.readline()
				if line:
					words = line.split()
				else:
					break
			fo.write("\t</Title>\n")
		if words[0] == ".W":
			fo.write("\t<Content>\n")
			line = fi.readline()
			if line:
				words = line.split()
			while words[0] != ".B":
				fo.write("\t\t" + line)
				line = fi.readline()
				if line:
					words = line.split()
				else:
					break
			fo.write("\t</Content>\n")
		if words[0] == ".B":
			line = fi.readline()
			fo.write("\t<B>\n\t\t" + line + "\t</B>\n")
		line = fi.readline()
		words = line.split()
		if words[0] == ".A":
			fo.write("\t<Author>\n")
			line = fi.readline()
			if line:
				words = line.split()
			while words[0] != ".N":
				fo.write("\t\t" + line)
				line = fi.readline()
				if line:
					words = line.split()
				else:
					break
			fo.write("\t</Author>\n")
		fo.write("\t<N>\n")
		line = fi.readline()
		if line:
			fo.write("\t\t" + line + "\t</N>\n")
		line = fi.readline()
		words = line.split()
		if words[0] == ".X":
			fo.write("\t<X>\n")
			line = fi.readline()
			if line:
				words = line.split()
			while words[0] != ".I":
				fo.write("\t\t" + line)
				line = fi.readline()
				if line:
					words = line.split()
				else:
					break
			fo.write("\t</X>\n")
		fo.write("</file>\n")
	line = fi.readline()
fi.close()