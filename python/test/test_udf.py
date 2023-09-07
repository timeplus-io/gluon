from timeplus import UDF


def test_udf(test_environment):
    UDF(env=test_environment).list()
