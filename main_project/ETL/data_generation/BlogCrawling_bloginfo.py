#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## An example of how to run from command line:
##       ipython BlogCrawling_bloginfo.py blognames output_filename
## where output_filename is the output zip file name
## The output is tumblrdata/output_filename.gz
## Make sure to run it with ipython and not python


# In[ ]:


import sys, os
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
import json
from zipfile import ZipFile 
import gzip
import pandas as pd

sys.path.append("./etl_tumblr_to_cassandra.py")
from etl_tumblr_to_cassandra import *

#     get_ipython().run_line_magic('run', 'etl_tumblr_to_cassandra.ipynb')


# Output : Dictionary
# Input : Series sources
# Summary : getPostInfo(sources) runs through sources, which is a pandas Series, and returns a dictionay with the blogname as key and necessary data as value
def getPostInfo(sources):
    info_dict = {}
    for blog in sources:
        info_dict[blog] = make_json(blog) # make_json is from etl_tumblr_to_cassandra.ipynb
    return info_dict

# In[ ]:
def main(seeds, output_filename):             
    seed_list = seeds.split(';') 
    s = json.dumps(getPostInfo(seed_list))
    jsonfilename = 'tumblrdata/output/' + output_filename
    with gzip.open(jsonfilename + ".gz", "wb") as f:
        f.write(bytes(s,"utf-8"))     
                 
        
# In[ ]:
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        startingpoint = (sys.argv[1]).split('&')
    else:
        print("Input Error")
        sys.exit(1)

    print("*******************")
    print(os.getpid())
    print(startingpoint)    
        
    try:
        seeds = startingpoint[0]
        output_filename = startingpoint[1] + '_' + startingpoint[2]
    except:
        print("Please check data format")

    main(seeds, output_filename)