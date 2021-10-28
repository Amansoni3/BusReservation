from django.shortcuts import render
from . import Pool
import uuid
from django.http import JsonResponse
import os


def BusInterface(request):
    return render(request, "BusInterface.html")


def SubmitBusRecord(request):
    try:
        busnumber = request.POST['busnumber']
        source = request.POST['source']
        destination = request.POST['destination']
        bustype = request.POST['bustype']
        seats = request.POST['seats']
        busfair = request.POST['busfair']
        picture = request.FILES['picture']

        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]

        db, cmd = Pool.connectionPolling()

        q = "insert into bus(busnumber, source, destination, bustype, seats, busfair, picture)values('{}',{},{},'{}','{}','{}','{}')".format( busnumber, source, destination, bustype, seats, busfair, filename)

        cmd.execute(q)

        f = open("D:/BusReservation/assets/BusImages/" + filename, "wb")

        for chunk in picture.chunks():
            f.write(chunk)
        f.close()

        db.commit()
        db.close()
        return render(request, "BusInterface.html", {'msg': "Record Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "BusInterface.html", {'msg': "Record Not Submitted"})

def DisplayAllBus(request):
    try:
        db, cmd = Pool.connectionPolling()

        q = "select B.*,(select C.cityname from city C where C.cityid=B.source),(select C.cityname from city C where C.cityid=B.destination) from bus B"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplayAllBus.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayAllBus.html", {'rows': []})




def FetchCityJason(request):
    try:

      db,cmd=Pool.connectionPolling()
      q="select * from city"
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def DisplayBusbyid(request):

    busid = request.GET['busid']

    try:
        db, cmd = Pool.connectionPolling()

        # q = "select * from bus where busid={}".format(busid)
        q = "select B.*,(select C.cityname from city C where C.cityid=B.source),(select C.cityname from city C where C.cityid=B.destination) from bus B where busid={}".format(busid)

        cmd.execute(q)
        row = cmd.fetchone()
        db.close()

        return render(request, "DisplayBusById.html", {'row': row})

    except Exception as e:

        print("Error", e)

        return render(request, "DisplayBusById.html", {'row': []})




def EditDeleteBusRecord(request):
    button = request.GET['button']

    busid = request.GET['busid']


    if (button == "EDIT"):

      busnumber = request.GET['busnumber']
      source = request.GET['source']
      destination = request.GET['destination']
      bustype = request.GET['bustype']
      seats = request.GET['seats']
      busfair = request.GET['busfair']



      try:

        db, cmd = Pool.connectionPolling()

        q = "update bus set busnumber='{}', source='{}', destination='{}', bustype='{}', seats='{}', busfair='{}' where busid={}".format(busnumber, source, destination, bustype, seats, busfair,busid)

        cmd.execute(q)
        db.commit()
        db.close()

        return DisplayAllBus(request)

      except Exception as e:

        print("Error", e)
        return DisplayAllBus(request)

    elif (button == "DELETE"):


        try:

            db, cmd = Pool.connectionPolling()

            q = "delete from bus where busid={}".format(busid)

            cmd.execute(q)
            db.commit()
            db.close()

            return DisplayAllBus(request)

        except Exception as e:

            print("Error", e)

            return DisplayAllBus(request)


