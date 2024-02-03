import re
import os
import json

# read all .md files
readmefiles = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
             readmefiles.append(os.path.join(root, file))

# load variable json
with open('readme.json') as f:
  var_dic = json.load(f)

# match pattern (<variable-*.?-tag>)(`*.?`)
# example: (<variable-VERSION-tag>)(`1.1`)
for filename in readmefiles:
    with open(filename,"r") as f:
      content = f.read()
    
    # update readme variables
    for key, value in var_dic.items():
      pattern = r"(<variable-{}-tag>)(`.*?`)".format(key)
      replacement = r"\1`{}`".format(value)
      content = re.sub(pattern, replacement, content)

    with open(filename,"w") as f:
      f.write(content)
