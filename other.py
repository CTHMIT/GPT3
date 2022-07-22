import re

# Extract values from sentences
def text2num(input):
  num = re.findall(r"[-+]?(?:\d*\.\d+|\d+)",input)
  return num

# gpt output have other symbol, clean up redundant symbols in sentences
def replace_progran(input):
  drop_list = ['\n','-',"'",'"']
  replace = filter(lambda item: item not in drop_list, input)
  newsentance = ''.join(replace)
  return newsentance
  
"""
input1 : original sentence
input2 : what you want calculate similarity
"""  
def similarity(input1,input2):
  intersection_cardinality = len(set.intersection(*[set(input1), set(input2)]))
  union_cardinality = len(set.union(*[set(input1), set(input2)]))
  return f"normal similarity (set style) : {round(intersection_cardinality/float(union_cardinality),2)}"
