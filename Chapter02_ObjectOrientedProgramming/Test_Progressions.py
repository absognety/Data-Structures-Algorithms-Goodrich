from Progression_Example import Progression
from ArithmeticProgression import ArithmeticProgression
from Geometric_Progression import GeometricProgression
from Fibonacci_Series import Fibonacci_Series


if __name__ == '__main__' :
    print('Default progression: ')
    Progression().print_progression(10)
    print('Arithmetic progression with increment 5: ')
    ArithmeticProgression(5).print_progression(10)
    print('Arithmetic progression with increment 5 and start 2: ')
    ArithmeticProgression(5,2).print_progression(10)
    print('Geometric progression with default base: ')
    GeometricProgression().print_progression(10)
    print('Geometric progression with base 3: ')
    GeometricProgression(3).print_progression(10)
    print('Fibonacci progression with default start values: ')
    Fibonacci_Series().print_progression(10)
    print('Fibonacci progression with start values 4 and 6: ')
    Fibonacci_Series(4,6).print_progression(10)
