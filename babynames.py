#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re

"""Baby Names exercise
Define the extract_names() function below and change main()
to call it.
For writing regex, it's nice to include a copy of the target
text for inspiration.
Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
 names={}
 list1= []
 text= open(filename,'rU')
 data= text.read()
 #print(data)
 tag= re.findall(r'<td>(.*?)</td>',str(data))
 p= [tag[i:i+3] for i in range (0,len(tag),3)]
 #print(p)
 date= re.findall(r'[in]\s\d\d\d\d',str(data))
 for i in date:
    d= i[-4:] 
 list1.append(d)
  
 for e in p:
    rank, m_name, f_name= e   
    if m_name not in names:
        names[m_name]= rank
    if f_name not in names :
        names[f_name]= rank

 #print(list1)
 k=sorted(names.items())
 for i in range(0,len(k)):
       list1.append(k[i][0]+" "+k[i][1])

 return (list1)

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  #print(len(args))
  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)
  
  
  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  filename= (str(args[0])) 
  #print(filename)
  if filename:
      extract_name = extract_names(filename)  
  if summary == True :
      text_file= open('%s.summary','w'%filename)
      for i in extract_name:
          text_file.write('{}{}'.format(i,'\n'))
      text_file.close() 
  else:
      print(*extract_name, sep= '\n')

  
if __name__ == '__main__':
  main()


  
    
