from django.shortcuts import render
from . import Pool
import uuid
import os


def DriverInterface(request):
    return render(request, "DriverInterface.html")


def SubmitDriverRecord(request):
    try:
        drivername = request.POST['drivername']
        contactno = request.POST['contactno']
        address = request.POST['address']
        licence = request.POST['licence']
        gender = request.POST['gender']
        salary = request.POST['salary']
        age = request.POST['age']
        picture = request.FILES['picture']

        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]

        db, cmd = Pool.connectionPolling()

        q = "insert into driver(drivername, contactno, address, licence, gender, salary, age, picture)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(drivername, contactno, address, licence, gender, salary, age, filename)

        cmd.execute(q)

        f = open("D:/BusReservation/assets/DriverImages/" + filename, "wb")

        for chunk in picture.chunks():
            f.write(chunk)
        f.close()

        db.commit()
        db.close()
        return render(request, "DriverInterface.html", {'msg': "Record Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "DriverInterface.html", {'msg': "Record Not Submitted"})

def DisplayAllDriver(request):
    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from driver"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplayAllDriver.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayAllDriver.html", {'rows': []})

def DisplayDriverbyid(request):

    driverid = request.GET['driverid']

    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from driver where driverid={}".format(driverid)

        cmd.execute(q)
        row = cmd.fetchone()
        db.close()

        return render(request, "DisplayDriverbyid.html", {'row': row})

    except Exception as e:

        print("Error", e)

        return render(request, "DisplayDriverbyid.html", {'row': []})


def EditDeleteDriverRecord(request):
    button = request.GET['button']

    driverid = request.GET['driverid']


    if (button == "EDIT"):

      drivername = request.GET['drivername']
      contactno = request.GET['contactno']
      address = request.GET['address']
      licence = request.GET['licence']
      gender = request.GET['gender']
      salary = request.GET['salary']
      age = request.GET['age']


      try:

        db, cmd = Pool.connectionPolling()

        q = "update driver set drivername='{}', contactno='{}', address='{}', licence='{}', gender='{}', salary='{}', age='{}' where driverid={}".format(drivername,contactno,address,licence,gender,salary,age,driverid)

        cmd.execute(q)
        db.commit()
        db.close()

        return DisplayAllDriver(request)

      except Exception as e:

        print("Error", e)
        return DisplayAllDriver(request)

    elif (button == "DELETE"):


        try:

            db, cmd = Pool.connectionPolling()

            q = "delete from driver where driverid={}".format(driverid)

            cmd.execute(q)
            db.commit()
            db.close()

            return DisplayAllDriver(request)

        except Exception as e:

            print("Error", e)

            return DisplayAllDriver(request)
