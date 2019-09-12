def filter(datum, sieve):
    """
    Filter properties of a given dict using a Boolean sieve.
    :param datum: the dict to recursively filter.
    :type datum: dict
    :param sieve: a dict indicating which datum fields to keep
    :type sieve: dict
    :return: sanitized_datum
    :rtype: sieve
    """
    keys = datum.keys()
    datum_copy = datum.copy()

    for key in keys:
        if key not in sieve.keys():
            del datum_copy[key]
        elif type(datum_copy[key]) is dict:
            datum_copy[key] = filter(datum_copy[key], sieve[key])
        elif type(datum_copy[key]) is list:
            for index, item in enumerate(datum_copy[key]):
                datum_copy[key][index] = filter(
                    datum_copy[key][index], sieve[key])
        else:
            pass

    return datum_copy
