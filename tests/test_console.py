#!/usr/bin/python3
"""tests for the console"""
import unittest
from io import StringIO
from unittest.mock import patch
import pep8
import os
import console
import tests
from console import OLIVEBOOMCommand


class TestConsole(unittest.TestCase):
    """tests for the console, quit and empty"""

    @classmethod
    def setUpClass(cls):
        """setup console class for test"""
        cls.consol = OLIVEBOOMCommand()

    @classmethod
    def teardown(cls):
        """tears down"""
        del cls.consol

    def tearDown(self):
        """delete file"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Pep8 test"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        """check for doc strings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(OLIVEBOOMCommand.emptyline.__doc__)
        self.assertIsNotNone(OLIVEBOOMCommand.do_quit.__doc__)
        self.assertIsNotNone(OLIVEBOOMCommand.do_EOF.__doc__)
        self.assertIsNotNone(OLIVEBOOMCommand.do_create.__doc__)
        self.assertIsNotNone(OLIVEBOOMCommand.do_show.__doc__)
        self.assertIsNotNone(OLIVEBOOMCommand.do_destroy.__doc__)
        self.assertIsNotNone(OLIVEBOOMCommand.do_all.__doc__)
        self.assertIsNotNone(OLIVEBOOMCommand.do_update.__doc__)
        self.assertIsNotNone(OLIVEBOOMCommand.default.__doc__)

    def test_emptyline(self):
        """test for empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("test")
            self.assertEqual("*** Unknown syntax: test\n", f.getvalue())

    def test_quit(self):
        """test the quit command works"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())
