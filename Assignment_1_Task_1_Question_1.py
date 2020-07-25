import re

# Matching capital letters

str = """COBOL is a compiled English-like computer programming language designed for 
business use. 122. On 2015/10/10 is a big date unlike 2010/11/1 """

all = re.findall(r"[\d]{4}/[\d]{1,2}/[\d]{1,2}", str)

for s in all:
    print(s)