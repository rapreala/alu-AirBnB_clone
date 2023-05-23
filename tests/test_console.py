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

    def test_all_method_present(self):
        self.assertTrue(hasattr(self.console, "do_BaseModel_all"))
        self.assertTrue(hasattr(self.console, "do_User_all"))
        self.assertTrue(hasattr(self.console, "do_State_all"))
        self.assertTrue(hasattr(self.console, "do_City_all"))
        self.assertTrue(hasattr(self.console, "do_Place_all"))
        self.assertTrue(hasattr(self.console, "do_Amenity_all"))
        self.assertTrue(hasattr(self.console, "do_Review_all"))

    def test_count_method_present(self):
        self.assertTrue(hasattr(self.console, "do_BaseModel_count"))
        self.assertTrue(hasattr(self.console, "do_User_count"))
        self.assertTrue(hasattr(self.console, "do_State_count"))
        self.assertTrue(hasattr(self.console, "do_City_count"))
        self.assertTrue(hasattr(self.console, "do_Place_count"))
        self.assertTrue(hasattr(self.console, "do_Amenity_count"))
        self.assertTrue(hasattr(self.console, "do_Review_count"))

    def test_show_method_present(self):
        self.assertTrue(hasattr(self.console, "do_BaseModel_show"))
        self.assertTrue(hasattr(self.console, "do_User_show"))
        self.assertTrue(hasattr(self.console, "do_State_show"))
        self.assertTrue(hasattr(self.console, "do_City_show"))
        self.assertTrue(hasattr(self.console, "do_Amenity_show"))
        self.assertTrue(hasattr(self.console, "do_Place_show"))
        self.assertTrue(hasattr(self.console, "do_Review_show"))

    def test_destroy_method_present(self):
        self.assertTrue(hasattr(self.console, "do_BaseModel_destroy"))
        self.assertTrue(hasattr(self.console, "do_User_destroy"))
        self.assertTrue(hasattr(self.console, "do_City_destroy"))
        self.assertTrue(hasattr(self.console, "do_State_destroy"))
        self.assertTrue(hasattr(self.console, "do_Place_destroy"))
        self.assertTrue(hasattr(self.console, "do_Amenity_destroy"))
        self.assertTrue(hasattr(self.console, "do_Review_destroy"))

    def test_update_method_present(self):
        self.assertTrue(hasattr(self.console, "do_BaseModel_update"))
        self.assertTrue(hasattr(self.console, "do_User_update"))
        self.assertTrue(hasattr(self.console, "do_State_update"))
        self.assertTrue(hasattr(self.console, "do_City_update"))
        self.assertTrue(hasattr(self.console, "do_Place_update"))
        self.assertTrue(hasattr(self.console, "do_Amenity_update"))
        self.assertTrue(hasattr(self.console, "do_Review_update"))


if __name__ == '__main__':
    unittest.main()
