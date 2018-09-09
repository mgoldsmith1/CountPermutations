import unittest
import random

N_RANGE = (1, 100000)


def solution(X, A):

    #if there is no sequence there is no permutation
    if len(A) == 0:
        return -1
    
    # initialize count array. stores distinct leaf positions
    count = {}

    # k indicates seconds and while not equal to X
    # we have not yet reached the destination
    for k in range(0, len(A)):
        count[A[k]] = True
        if len(count) == X:
            return k
    return -1


class TestCountPermutations(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]), 6)

    def test_extreme_single(self):
        self.assertEqual(solution(1, [1]), 0)
        self.assertEqual(solution(0, [2]), -1)
        self.assertEqual(solution(2, [2]), -1)
        self.assertEqual(solution(2, [2,1]), 1)
        self.assertEqual(solution(2, [1, 2]), 1)
        self.assertEqual(solution(2, [1, 1]), -1)
        self.assertEqual(solution(2, [2, 2]), -1)
        self.assertEqual(solution(3, [1, 2]), -1)

    def test_simple(self):
        self.assertEqual(solution(3, [1, 2, 3]), 2)
        self.assertEqual(solution(3, [2, 3, 1]), 2)
        self.assertEqual(solution(3, [3, 2, 1]), 2)
        self.assertEqual(solution(4, [3, 2, 1]), -1)
        self.assertEqual(solution(3, [3, 2, 2]), -1)
        self.assertEqual(solution(3, [3, 3, 3, 1, 1, 2]), 5)

    def test_extreme_max(self):
        X = 100000
        A = range(1, X)
        random.shuffle(A)
        A.append(X)
        self.assertEqual(solution(X, A), X - 1)


if __name__ == '__main__':
    unittest.main()
