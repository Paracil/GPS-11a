import unittest
import transform

class TestStringMethods(unittest.TestCase):
    def test_is_upper(self):
        """Comprueba que el texto pasa a mayusculas."""
        resultado = transform.to_upper_case("hello")
        self.assertEqual(resultado, "HELLO")

    def test_is_lower(self):
        """Comprueba que el texto pasa a minusculas."""
        resultado = transform.to_lower_case("HELLO")
        self.assertEqual(resultado, "hello")

    def test_is_capitalize(self):
        """Comprueba que el texto pasa a capitalizado."""
        resultado = transform.to_capitalize("HELLO")
        self.assertEqual(resultado, "Hello")

if __name__ == '__main__':
    unittest.main()