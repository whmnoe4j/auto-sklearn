import sklearn.linear_model

from autosklearn.pipeline.components.classification.passive_aggressive import \
    PassiveAggressive

from .test_base import BaseClassificationComponentTest


class PassiveAggressiveComponentTest(BaseClassificationComponentTest):

    __test__ = True

    res = dict()
    res["default_iris"] = 0.98
    res["default_iris_iterative"] = 0.95999999999999996
    res["default_iris_proba"] = 0.2185197378302077
    res["default_iris_sparse"] = 0.38
    res["default_digits"] = 0.9174256223436551
    res["default_digits_iterative"] = 0.9174256223436551
    res["default_digits_binary"] = 0.99332119004250152
    res["default_digits_multilabel"] = 0.94149891011963693
    res["default_digits_multilabel_proba"] = 1.0

    sk_mod = sklearn.linear_model.PassiveAggressiveClassifier
    module = PassiveAggressive
