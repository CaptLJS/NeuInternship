# -*- coding: utf-8 -*-
import io
import string
from g2p_en import G2p
import re


infile = io.open("/home/reverie/Desktop/text.txt","r",encoding="utf-8")
outfile = io.open("/media/reverie/Speech/kaldi/egs/reverie/org/example.txt","w",encoding="utf-8")
g2p =G2p()
for line in infile:
    word = line.strip()
    output = g2p(word)
    outfile.write(word+"\t")
    for item in output:
        result = ''.join([i for i in item if not i.isdigit()])
        outfile.write(result+" ")
    outfile.write("\n")


infile.close()
outfile.close()



#result = re.sub(r’\d+’, ‘’, input_str)
#print(result)
#res = ''.join([i for i in ini_string if not i.isdigit()])

