import string

"""
File contains a dict `cataloge` with sets from which custome sets can be created.
"""

cataloge = {
    'ltrs': set(string.ascii_letters),
    'nmbrs': set(string.digits),
    'spchars': {'!',
                '@',
                '#',
                '$',
                '%',
                '^',
                '&',
                '*',
                '<',
                '>',
                '?',
                '-',
                '_'
    }
}

def custome_set(requirements):
    """
    IMPUT:
        - touple.
    OUTPUT:
        - set
    DESCRIPTION: Creates a set with the requirements needed from base sets.
    """
    
    custome = set()

    for item in requirements:
        custome |= cataloge[item]

    return custome
