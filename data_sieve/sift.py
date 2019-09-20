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
        # Ignore elements not defined in the sieve
        if key not in sieve:
            continue
        # Sift all values in a dict, allowing nested data
        elif isinstance(value, dict):
            result[key] = sift(value, sieve[key])
        # Sift all elements of lists, allowing nested data
        elif isinstance(value, list):
            result[key] = [sift(item, sieve[key]) for item in value]
        elif value == True:
            # Check for truthiness of value, since we expect a Boolean sieve
            # i.e. some values can be explicitly filtered out
            result[key] = value

    return result
