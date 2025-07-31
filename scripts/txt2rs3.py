import sys,os,re

"""convert \\n-split text with to RS3 segment, read from stdin, write to stdout"""

print("<rst>")
print("	<header><relations/></header>")
print("	<body>")
nr=0
for line in sys.stdin:
	line=line.strip()
	if len(line)>0:
		nr+=1
		print(f'		<segment id="{nr}">{line}</segment>')
print("	</body>")
print("</rst>")
