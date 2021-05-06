from DictTable import DictTableItem

if __name__ == '__main__' or __name__ == 'Test':
    path='..\Vocabulary.db'
    for r in get_data(path):
        print(dict(r))
        if r.Word == r.Stem:
            print(f"{r.Word} - {r.Translate}")
        else:
            print(f"{r.Word}({r.Stem}) - {r.Translate}")
