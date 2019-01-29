import requests as req

URL = 'https://immense-springs-48842.herokuapp.com/'


def getJson():
    r = req.get(URL + 'api/' + 'getjson')
    print(r.text)


def deleteByName(Name):
    r = req.delete(URL + 'api/' + 'delete/' + Name)
    data = r.text
    print(data)


def UpdateStudent(Attendance, Cie, Name, Subject, USN):
    r = req.post(URL + 'api/' + 'update/' +
                 Attendance + '/' +
                 Cie + '/'
                 + Name + '/' +
                 Subject + '/' +
                 USN)
    data = r.text
    if data == 'Done':
        print('Successfully updated Data')
    else:
        print('Error Uploading Data')


if __name__ == '__main__':
    # UpdateStudent('90', '44', "Suhas", "Maths", "1SI15EC105")
    deleteByName("Suhas")
