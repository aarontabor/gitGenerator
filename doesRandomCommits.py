#!/usr/bin/python

class DoesRandomCommits:
  def __init__(self, repoPath, authors = [('John Doe', 'jdoe@email.com')]):
    self.repoPath = repoPath
    self.authors = authors

  def commit(self, authoredDate):
    return True
