#!/usr/bin/python

import pytest
from doesCommits import DoesCommits
import datetime

class TestDoesCommits:

  def test_commits_change(self):
    doesCommits = DoesCommits()
    now = datetime.datetime.now()
    assert doesCommits.commit('Alice', now)

  def test_it_calls_the_api(self):
    pass


