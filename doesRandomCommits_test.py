#!/usr/bin/python

import pytest
from doesRandomCommits import DoesRandomCommits
import datetime

class TestDoesRandomCommits:

  def test_commits_change(self):
    doesCommits = DoesRandomCommits()
    now = datetime.datetime.now()
    assert doesCommits.commit('Alice', now)

  def test_it_calls_the_api(self):
    pass


