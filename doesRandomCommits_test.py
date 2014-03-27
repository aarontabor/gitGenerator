#!/usr/bin/python

import pytest
from doesRandomCommits import DoesRandomCommits
import datetime

class TestDoesRandomCommits:

  def test_commits_change(self):
    doesCommits = DoesRandomCommits('testDir')
    now = datetime.datetime.now()
    assert doesCommits.commit(now)

