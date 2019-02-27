import requests as req

URL = 'https://attendancesit00.herokuapp.com/'


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

def restAttendanceByUSN(USN):
    r = req.post(URL + 'api/' + 'reset/' + 'attendance/' + USN)
    data = r.text
    print(data)

def updateStudent(Attendance, Cie, Name, Subject, USN):
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

def setAttendanceByUSN(usn,value):
     r = req.post(URL + 'api/' + 'set/' + 'attendance/' + usn + '/' + value)
     data = r.text
     return data


if __name__ == '__main__':
    # UpdateStudent('90', '44', "Supreeth", "Maths", "1SI16EC099")
    # deleteByUSN("1SI15EC105")
    # updateAttendanceByUSN('1SI15EC027')
    response = setAttendanceByUSN('1SI15EC027','80')
    if response == 'SET':
        print('Attendance set successfully')
    else:
        print('Error')