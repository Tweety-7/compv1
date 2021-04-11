import unittest
from comp import main_m
from io import StringIO
from unittest.mock import patch, call
# from unittest.mock import patch
str_help = '"Для отображения информации о возможности программы: python computorv1 -h", "для отображение промежуточных шагов -s",\
 "для чтения выражения из файла -f", "для отображение ошибок входа -v",\
 "неравенство должно быть квадратным и не содержать отрицательных стеепней", "общий вид выражения: a*x^2 + b*x^1 +c = 0",\
 "я справлюсь с вещественными числами и сокращением подобных членов,", "смогу вывести ирроцианальные корни и переживу, если ты пропустишь * или ^ для первой степени",\
 "давай поиграем кто быстрее? введи: python comp.py x^2 + 3x - 4 = 0"'


class TestMainCase(unittest.TestCase):
    """тесты для мейн"""
    @patch('builtins.print')
    # @patch('sys.stdout', new_callable=StringIO)
    def test_first(self, mocked_print):
        """ вывод хелпа при пустом входе"""
        in_t = ['']
        out_t = str_help
        with patch('comp.sys.argv', in_t), patch('comp.print') as print_mock:
            main_m()
            print_mock.assert_called_with(out_t)
            # print_mock.
    def test_two(self):
        """D==0"""
        in_t = ['comp.py','x^2.0', '-', '4x', '+',  '4', '=', '0'] #'x^2.0', '-', '4x', '+',  '4', '=', '0'
        out_t = [call('Reduced form: 4X^0 + -4X^1 + 1X^2 = 0'),
 call('Polynomial degree: ', 2),
 call('solution is ', 2.0)]
        #['Reduced form: 4X^0 + -4X^1 + 1X^2 + = 0', 'Polynomial degree:  2', 'solution is  2.0'], 2.0
        # #'Reduced form: 4X^0 + -4X^1 + 1X^2 + = 0', 'Polynomial degree:  2',
        with patch('comp.sys.argv', in_t), patch('comp.print') as print_mock:
            main_m()
            print_mock.assert_has_calls(out_t)
    def test_three(self):
        """D<0"""
        in_t = ['comp.py', 'X^2', '+', '-1X', '+', '-12', '=', '0']
        out_t = [call('Reduced form: -12X^0 + -1X^1 + 1X^2 = 0'),
                 call('Polynomial degree: ', 2),
                 call('Discriminant is strictly positiv, the two solution are: '),
                 call(4),
                 call(-3)]
        with patch('comp.sys.argv', in_t), patch('comp.print') as print_mock:
            main_m()
            print_mock.assert_has_calls(out_t)
    def test_ex_1(self):
        in_t = ['comp.py',"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"]
        out_t = [call('Reduced form: 4X^0 + 4X^1 + -9.3X^2 = 0'),
                 call('Polynomial degree: ', 2),
                 call('Discriminant is strictly positiv, the two solution are: '),
                 call(-0.475131),
                 call(0.905239)]
        with patch('comp.sys.argv', in_t), patch('comp.print') as print_mock:
            main_m()
            print_mock.assert_has_calls(out_t)
    def test_ex_2(self):
        in_t = ['comp.py',"5 * X^0 + 4 * X^1 = 4 * X^0"]
        out_t = [call('Reduced form: 1X^0 + 4X^1 = 0'),
                 call('Polynomial degree: ', 1),
                 call('solution is ', -0.25)]
        with patch('comp.sys.argv', in_t), patch('comp.print') as print_mock:
            main_m()
            print_mock.assert_has_calls(out_t)
    def test_ex_3(self):
        in_t = ['comp.py',"8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"]
        out_t = [call('Reduced form: 5X^0 + -6X^1 + -5.6X^3 = 0'),
                 call("polynomial degree is stricly greater than 2, I can't solve.")]
        with patch('comp.sys.argv', in_t), patch('comp.print') as print_mock:
            main_m()
            print_mock.assert_has_calls(out_t)
    def test_ex_42(self):
        in_t = ['comp.py',"42 * X^0 = 42 * X^0"]
        out_t = [call('Reduced form: 0 = 0'), call('all the real numbers are solution')]
        with patch('comp.sys.argv', in_t), patch('comp.print') as print_mock:
            main_m()
            print_mock.assert_has_calls(out_t)
    def test_ex_bonus(self):
        in_t = ['comp.py',"5 + 4 * X + X^2= X^2"]
        out_t = [call('Reduced form: 5X^0 + 4X^1 = 0'),
                 call('Polynomial degree: ', 1),
                 call('solution is ', -1.25)]
        with patch('comp.sys.argv', in_t), patch('comp.print') as print_mock:
            main_m()
            print_mock.assert_has_calls(out_t)
    def test_bonus_file(self):
        in_t = ['comp.py', '-f', 'minus_d.txt']
        out_t = [call(['-f', '-vs', 'x^2', '-', 'x', '+', '2', '=', '0\n']),
 call('Reduced form: 2X^0 + -1X^1 + 1X^2 = 0'),
 call('Polynomial degree: ', 2),
 call('D = b^2 - 4*a*c => -1^2 - 4 * 2.0'),
 call('D = ', -7.0),
 call('комплексные корни, D < 0'),
 call('Discriminant is strictly negative, the two irrational solution are: '),
 call('1/2 + (√-7 / 2) *i'),
 call('1/2 - (√-7 / 2) *i')]
        with patch('comp.sys.argv', in_t), patch('comp.print') as print_mock:
            main_m()
            print_mock.assert_has_calls(out_t)
if __name__ == "__name__":
    # unittest.main()
    pass
    # print(str_help)
unittest.main()
# print(__name__)
