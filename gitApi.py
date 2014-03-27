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

def commit(repo_path, commitMessage, author=None, date=None):
  orig_dir = os.getcwd()
  os.chdir(repo_path)

  if author:
    authorOption = '--author="%s"' % author
  else:
    authorOption = ''

  if date:
    overrideDateOption = 'GIT_AUTHOR_DATE="%s" GIT_COMMITTER_DATE="%s"' % \
        (date, date)
  else:
    overrideDateOption = ''

  commands.getoutput('%s git commit %s -m "%s"' % \
      (overrideDateOption, authorOption, commitMessage))
  os.chdir(orig_dir)


