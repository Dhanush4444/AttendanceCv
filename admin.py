import requests as req

URL = 'https://immense-springs-48842.herokuapp.com/'


def getJson():
    r = req.get(URL + 'api/' + 'getjson')
    print(r.text)


def deleteByUSN(USN):
    r = req.delete(URL + 'api/' + 'delete/' + USN)
    data = r.text
    print(data)

def updateAttendanceByUSN(USN):
    r = req.post(URL + 'api/' + 'update/' + 'attendance/' + USN)
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
    # UpdateStudent('90', '44', "Rakesh", "Maths", "1SI15EC105")
    # deleteByUSN("Suhas")
    updateAttendanceByUSN('1SI15EC105')