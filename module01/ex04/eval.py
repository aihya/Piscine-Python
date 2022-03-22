class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        try:
            assert type(words) == list, None
            assert type(coefs) == list, None
            assert len(words) == len(coefs), None
            _sum = 0
            for coef, word in zip(coefs, words):
                assert type(word) == str, None
                assert type(coef) == float, None
                _sum += coef * len(word)
        except AssertionError:
            return -1
        return _sum


    @staticmethod
    def enumerate_evaluate(coefs, words):
        try:
            assert type(words) == list, None
            assert type(coefs) == list, None
            assert len(words) == len(coefs), None
            _sum = 0
            for index, word in enumerate(words):
                assert type(word) == str, None
                assert type(coefs[index]) == float, None
                _sum += coefs[index] * len(word)
        except AssertionError:
            return -1
        return _sum
