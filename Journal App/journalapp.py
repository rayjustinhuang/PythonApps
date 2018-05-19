
def journal_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_data = []

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Done, goodbye.')


def list_entries(data):
    print('Your journal entries:')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    data.append(text)


if __name__=='__main__':
    journal_loop()
