# tests/test_console.py
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

            self.assertFalse(self.console.onecmd("create SomeClass"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(len(f.getvalue()) > 0)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

            self.assertFalse(self.console.onecmd("show SomeClass"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

            self.assertFalse(self.console.onecmd("show BaseModel"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

            self.assertFalse(self.console.onecmd("destroy SomeClass"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

            self.assertFalse(self.console.onecmd("destroy BaseModel"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all SomeClass"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

            self.assertTrue(self.console.onecmd("all"))
            self.assertTrue(len(f.getvalue()) > 0)

            self.assertTrue(self.console.onecmd("all BaseModel"))
            self.assertTrue(len(f.getvalue()) > 0)

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("count SomeClass"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

            self.assertTrue(self.console.onecmd("count BaseModel"))
            self.assertTrue(len(f.getvalue()) > 0)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

            self.assertFalse(self.console.onecmd("update SomeClass"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

            self.assertFalse(self.console.onecmd("update BaseModel"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("help"))
            self.assertTrue(len(f.getvalue()) > 0)

            self.assertTrue(self.console.onecmd("help quit"))
            self.assertTrue(len(f.getvalue()) > 0)

            self.assertTrue(self.console.onecmd("help EOF"))
            self.assertTrue(len(f.getvalue()) > 0)

            self.assertTrue(self.console.onecmd("help create"))
            self.assertTrue(len(f.getvalue()) > 0)

            self.assertTrue(self.console.onecmd("help show"))
            self.assertTrue(len(f.getvalue()) > 0)

            self.assertTrue(self.console.onecmd("help destroy"))
            self.assertTrue(len(f.getvalue()) > 0)

            self.assertTrue(self.console.onecmd("help all"))
            self.assertTrue(len(f.getvalue()) > 0)

            self.assertTrue(self.console.onecmd("help count"))
            self.assertTrue(len(f.getvalue()) > 0)

            self.assertTrue(self.console.onecmd("help update"))
            self.assertTrue(len(f.getvalue()) > 0)

    def test_default(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("non_existent_command"))
            self.assertEqual(f.getvalue(), "*** Unknown syntax: non_existent_command\n")

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIsNone(self.console.emptyline())


if __name__ == '__main__':
    unittest.main()
