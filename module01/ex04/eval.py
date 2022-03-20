class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) == len(words):
            return sum([c*len(w) for c, w in zip(coefs, words)])
        return -1

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) == len(words):
            return sum([coefs[i]*len(w) for i, w in enumerate(words)])
        return -1
