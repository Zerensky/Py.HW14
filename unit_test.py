import unittest as ut

from Python_next_deep.Seminar_14.doc_test_t import remove_chars


class TestChars(ut.TestCase):
    def test_no_change(self):
        self.assertEqual(remove_chars('dddddd dddd'), 'dddddd dddd')

    def test_lover(self):
        self.assertEqual(remove_chars('AAA AA'), 'aaa aa')

    def test_sign(self):
        self.assertEqual(remove_chars('a,a,n: v.v;'), 'aan vv')

    def test_cyrillic(self):
        self.assertEqual(remove_chars('БВАОПоао ваов'), ' ')

    def test_upper(self):
        self.assertEquals(remove_chars('WWW,3322,ГГ:'), 'www')

    def main(self, verbosity):
        pass


if __name__ == '__main__':
    unit_test = TestChars()
    unit_test.main(verbosity=True)