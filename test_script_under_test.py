import unittest

from script_under_test import *


class MyTests(unittest.TestCase):

  def test_HelloWorld(self):

    self.assertEqual(hello_world(), 'HELLO THERE')


  def test_NumList(self):

    self.assertEqual(len(create_num_list(20)), 20)


  def test_ValGreaterPi(self):

    self.assertTrue(getPi() > 3.14)


# Kick off unit testing

unittest.main()
