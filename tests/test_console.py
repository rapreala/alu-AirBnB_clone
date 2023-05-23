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
        self.assertTrue(hasattr(self.console, "do_BaseModel.all"))
        self.assertTrue(hasattr(self.console, "do_Review.all"))
        self.assertTrue(hasattr(self.console, "do_User.all"))
        self.assertTrue(hasattr(self.console, "do_State.all"))
        self.assertTrue(hasattr(self.console, "do_City.all"))
        self.assertTrue(hasattr(self.console, "do_Amenity.all"))
        self.assertTrue(hasattr(self.console, "do_Place.all"))

    def test_count_method_present(self):
        self.assertTrue(hasattr(self.console, "do_BaseModel.count"))
        self.assertTrue(hasattr(self.console, "do_User.count"))
        self.assertTrue(hasattr(self.console, "do_State.count"))
        self.assertTrue(hasattr(self.console, "do_City.count"))
        self.assertTrue(hasattr(self.console, "do_Place.count"))
        self.assertTrue(hasattr(self.console, "do_Amenity.count"))
        self.assertTrue(hasattr(self.console, "do_Review.count"))

    def test_show_method_present(self):
        self.assertTrue(hasattr(self.console, "do_BaseModel.show"))
        self.assertTrue(hasattr(self.console, "do_User.show"))
        self.assertTrue(hasattr(self.console, "do_State.show"))
        self.assertTrue(hasattr(self.console, "do_City.show"))
        self.assertTrue(hasattr(self.console, "do_Amenity.show"))
        self.assertTrue(hasattr(self.console, "do_Place.show"))
        self.assertTrue(hasattr(self.console, "do_Review.show"))

    def test_destroy_method_present(self):
        self.assertTrue(hasattr(self.console, "do_BaseModel.destroy"))
        self.assertTrue(hasattr(self.console, "do_User.destroy"))
        self.assertTrue(hasattr(self.console, "do_City.destroy"))
        self.assertTrue(hasattr(self.console, "do_State.destroy"))
        self.assertTrue(hasattr(self.console, "do_Place.destroy"))
        self.assertTrue(hasattr(self.console, "do_Amenity.destroy"))
        self.assertTrue(hasattr(self.console, "do_Review.destroy"))

    def test_update_method_present(self):
        self.assertTrue(hasattr(self.console, "do_BaseModel.update"))
        self.assertTrue(hasattr(self.console, "do_User.update"))
        self.assertTrue(hasattr(self.console, "do_State.update"))
        self.assertTrue(hasattr(self.console, "do_City.update"))
        self.assertTrue(hasattr(self.console, "do_Place.update"))
        self.assertTrue(hasattr(self.console, "do_Amenity.update"))
        self.assertTrue(hasattr(self.console, "do_Review.update"))

if __name__ == '__main__':
    unittest.main()
