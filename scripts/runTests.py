#!/usr/bin/env python
"""
Run the microdata testing locally
"""

import sys

# You may want to adapt this to your environment...
import sys, getopt

from pyMicrodatamod import pyMicrodata, __version__

###########################################

test_path      = "./tests/"
test_file_base = test_path + ("%s" % str(sys.argv[1]))
#test_file_base = test_path + ("sdo_eg_md_%d" % int(sys.argv[1]))
test_html = test_file_base + ".html"
#test_ttl  = test_file_base + ".ttl"

processor = pyMicrodata()
print(processor.rdf_from_source(test_html))
print("----")
#with open(test_ttl) as f :
#	for l in f:
#		print(l)

print("----")
with open(test_html) as f :
	for l in f:
		print(l)




