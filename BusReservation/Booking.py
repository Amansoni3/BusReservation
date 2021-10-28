from django.shortcuts import render
from . import Pool

def BookingTicket(request):
    return render(request, "Booking.html")


def BookTicket(request):
    try:
        busid = request.GET['busid']
        busnumber = request.GET['busnumber']
        source = request.GET['source']
        destination = request.GET['destination']
        bustype = request.GET['bustype']
        busfair = request.GET['busfair']

        row = [busid,busnumber,source,destination,bustype,busfair]

        return render(request, "Booking.html", {'row': row})

    except Exception as e:

        return render(request, "Booking.html", {'row': []})

def SubmitBookingRecord(request):
    try:
        # busid = request.GET['busid']
        username = request.GET['username']
        age = request.GET['age']
        email = request.GET['email']
        mobilenumber = request.GET['mobilenumber']
        addhar = request.GET['addhar']
        address = request.GET['address']
        totalseats = request.GET['totalseats']
        gender = request.GET['gender']
        busnumber = request.GET['busnumber']
        source = request.GET['source']
        destination = request.GET['destination']
        bustype = request.GET['bustype']
        busfair = request.GET['busfair']

        totalamount=int(busfair)*int(totalseats)

        db, cmd = Pool.connectionPolling()

        q = "insert into booking(username, age, email, mobilenumber, addhar, address, totalseats, gender, busnumber, source, destination, bustype, busfair,totalamount)values('{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}',{},{})".format(username, age, email, mobilenumber, addhar, address, totalseats, gender, busnumber, source, destination, bustype, busfair,totalamount)

        cmd.execute(q)

        # q="update booking set busfair={}*{} where busnumber={}".format(busfair,totalseats,busnumber)
        #
        # cmd.execute(q)

        db.commit()
        db.close()
        return render(request, "Booking.html", {'msg': "Booking Succesfull"})

    except Exception as e:

        print(e)
        return render(request, "Booking.html", {'msg': "Failed"})

def DisplayAllBooking(request):
    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from booking "

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplayAllBooking.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayAllBooking.html", {'rows': []})


def ViewTicket(request):
    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from booking "

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "ShowMyTicket.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "ShowMyTicket.html", {'rows': []})




