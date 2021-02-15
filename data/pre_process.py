import re

import collections
import string

file = 'lda_original_topics.txt'
with open(file,'r') as f:
    content = f.readlines()
abstract_list = []
for line in content:
    text = line.replace('\', \'',' ').lstrip('\']')
    abstract_list.append(text)

with open('lda_original_topics_processed.txt','a') as f:
    for line in abstract_list:
        f.write("%s" % line)
