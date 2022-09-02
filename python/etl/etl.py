'''Module to transform the legacy data into the new format.'''

def transform(legacy_data):
    '''
    Return a dictionary in the new format.
    '''
    new_system = {}
    for i, letters in legacy_data.items():
        for letter in letters:
            new_system[letter.lower()] = i
    return new_system
    