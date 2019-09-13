def sift(datum, sieve):
    """
    Sift properties of a given dict using a Boolean sieve.
    :param datum: the dict to recursively filter.
    :type datum: dict
    :param sieve: a dict indicating which datum fields to keep
    :type sieve: dict
    :return: result
    :rtype: dict
    """

    result = {}

    for key, value in datum.items():
        if key not in sieve:
            continue
        elif isinstance(value, dict):
            result[key] = sift(value, sieve[key])
        elif isinstance(value, list):
            result[key] = [sift(item, sieve[key]) for item in value]
        else:
            result[key] = value

    return result
