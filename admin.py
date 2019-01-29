import requests as req

URL = 'https://immense-springs-48842.herokuapp.com/'


def getJson():
    r = req.get(URL + 'api/' + 'getjson')
    print(r.text)


def UpdateStudent(Attendance, Cie, Name, Subject, USN):
    r = req.post(URL + 'api/' + 'update/' +
                 Attendance + '/' +
                 Cie + '/'
                 + Name + '/' +
                 Subject + '/' +
                 USN)
    data = r.text
    print (data)


if __name__ == '__main__':
    UpdateStudent('80','44',"Suhas","Maths","1SI15EC105")
