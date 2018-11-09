import sys
import re
import os
import shutil
import subprocess
#import commands


def get_special_paths(dir):
    filenames = os.listdir(dir)
    files=[]
    
    for i in filenames:
        match = re.search(r'__(\w+)__', i)
        if match:
            files.append(os.path.abspath(os.path.join(dir, i)))
    return(files)

def copy_to(s, des):
    if not os.path.isdir(des):
        os.mkdir(des)

    for p in s:
         f_n = os.path.basename(p)
         shutil.copy(p, os.path.join(des, f_n))
        
def zip_to(s, des):
    # using 7zip
    command = 'C:\\"Program Files"\\7-Zip\\7z a -t7z "%s" %s' % (des, ' '.join(s))
    #command = "zip -j"+ des + ' ' + ' '.join(s)
    print("Command I'm going to do"+ command)
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    out = pipe.stdout.readlines()
    sts = pipe.wait()
    print(sts)
    print(out)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  p= []
  for dir in args:
    p.extend(get_special_paths(dir))

  if todir:
    copy_to(p, todir)
  elif tozip:
    zip_to(p, tozip)
  else:
    print('\n'.join(p))

if __name__ == "__main__":
  main()
