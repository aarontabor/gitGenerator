#!/usr/bin/python

'''
This library will provide an interface to perform git related operations.
'''

import os
import commands

def initialized(repo_path):
  files = os.listdir(repo_path)
  return '.git' in files

def init(repo_path):
  commands.getoutput('git init %s' % repo_path)

def stage(filename):
  basename = os.path.basename(filename)
  dirname = os.path.dirname(filename)
  orig_dir = os.getcwd()
  os.chdir(dirname)
  commands.getoutput('git add %s' % basename)
  os.chdir(orig_dir)

def commit(repo_path, commitMessage, author=None):
  orig_dir = os.getcwd()
  os.chdir(repo_path)

  if author:
    authorOption = '--author="%s"' % author
  else:
    authorOption = ''

  commands.getoutput('git commit %s -m "%s"' % (authorOption, commitMessage))
  os.chdir(orig_dir)


