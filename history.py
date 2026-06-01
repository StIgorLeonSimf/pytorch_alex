s = """Вороне Бог послал кусочек сыра   
На ель ворона взгромоздясь..."""

print(s)
ls = s.split()
print(ls)
s1 = 'Anna:Fantasy,Classic;Pit:History;Bob:Classic,Fable '
s2 = 'Avatar:Fantasy,Cesar:History,Djim:Classic'
print(s2)

class Reader:
    def __init__(self, name, ganry):
        self.ganry = ganry.split(',')
        self.name = name

    def __repr__(self):
        return f'{self.name} {self.ganry}'


def create_reader(readers:str):
    ls = readers.split(';')
    result = []
    for n in ls:
        lsn = n.split(':')
        result.append(Reader(lsn[0], lsn[1]))
    return result


class Library:
    def __init__(self, data):
        data = data.split(',')
        self.data = { d.split(':')[1]: d.split(':')[0] for d in data}
        print(self.data)

    def get_books(self, list_reads):
        books = []
        for read in list_reads:
            for interest in read.ganry:
                bk = self.data.get(interest)
                if bk:
                    print(f'{read.name} - {bk}')



l1 = Library(s2)
# print(create_reader(s1))
l1.get_books(create_reader(s1))