#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest

"""
更多:
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140137128705556022982cfd844b38d050add8565dcb9000
"""

class TestDict(unittest.TestCase):
	# def setUp(self):

	def test_key(self):
		d = {}
		d["wkz"]='value'
		print d["wkz"]
		self.assertEquals(d["wkz"], 'value')
		d["single"]=True
		self.assertFalse(d["single"],"dog")

