#!/usr/bin/python

import pytest
import gitApi 
import os
import shutil
import commands
import re

test_repo = 'just_for_test'

class TestGitApi:

############################
  @pytest.fixture
  def initializedRepo(self):
    gitApi.init(test_repo)
    return test_repo

  @pytest.fixture
  def editedFile(self):
    filename = os.path.join(test_repo, 'foo.txt')
    writeChange(filename)
    return filename

  @pytest.fixture
  def stagedFile(self, editedFile):
    gitApi.stage(editedFile) # I don't like calling the Api here... but intention better
    return editedFile

############################
  def setup_method(self, method):
    if os.path.exists(test_repo):
      shutil.rmtree(test_repo)
    os.mkdir(test_repo)

  def teardown_method(self, method):
    shutil.rmtree(test_repo)

############################
  def test_can_init_repo(self):
    gitApi.init(test_repo)
    assert isInitialized(test_repo)

  def test_initialized_happy(self, initializedRepo):
    assert gitApi.initialized(initializedRepo)

  def test_initialized_sad(self):
    assert not gitApi.initialized(test_repo)

  def test_can_stage_change(self, initializedRepo, editedFile):
    gitApi.stage(editedFile)
    assert isStaged(editedFile)
    
  def test_can_commit_change(self, initializedRepo, stagedFile):
    gitApi.commit(initializedRepo, 'test commit')
    assert isCommitted(stagedFile)

  def test_can_commit_author_name(self, initializedRepo, stagedFile):
    gitApi.commit(initializedRepo, 'test commit', author='Joe Blow <jb@email.com>')
    log = getCommitLog(initializedRepo)
    assert 'Joe Blow' in log

  def test_can_commit_another_date(self, initializedRepo, stagedFile):
    gitApi.commit(initializedRepo, 'test commit', date='2010/01/01 0:00:00')
    log = getCommitLog(initializedRepo)
    assert '2010' in log

############################
def writeChange(filename):
    f = open(filename, 'w')
    f.write('garbage')
    f.close()


def initializeRepo(repoPath):
  filename = os.path.join(repoPath, '.git')
  f = open(filename, 'w')
  f.write('')
  f.close()

def isInitialized(repoPath):
    filename = os.path.join(test_repo, '.git')
    return os.path.exists(filename)

def isStaged(filename):
  basename = os.path.basename(filename)
  dirname = os.path.dirname(filename)
  origDir = os.getcwd()
  os.chdir(dirname)
  status = commands.getoutput('git status')
  matches = re.findall('Changes to be committed:.*%s' % basename, status, flags=re.DOTALL)
  os.chdir(origDir)
  return len(matches) > 0

def isCommitted(filename):
  basename = os.path.basename(filename)
  dirname = os.path.dirname(filename)
  origDir = os.getcwd()
  os.chdir(dirname)
  log = commands.getoutput('git log')
  os.chdir(origDir)
  return 'commit' in log

def getCommitLog(repo_path):
  origDir = os.getcwd()
  os.chdir(repo_path)
  log = commands.getoutput('git log')
  os.chdir(origDir)
  return log


