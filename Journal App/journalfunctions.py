import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: The base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print('... saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
            for entry in journal_data:
                fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)


def delete_entry(index, journal_data):
    if index not in list(range(len(journal_data))):
        print('There is no journal entry with that index yet. If you just added the entry during this session, '
              'please exit then rerun the program to save the entry before deleting it.')
    else:
        print("Deleting entry {}, '{}'".format(index+1, journal_data[index]))
        journal_data.pop(index)
