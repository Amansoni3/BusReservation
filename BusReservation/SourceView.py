from django.shortcuts import render
from . import Pool

def SourceDestination(request):
    return render(request, "Source.html")


def DisplaySearchBus(request):

    source = request.GET['source']
    destination = request.GET['destination']

    try:
        db, cmd = Pool.connectionPolling()

        q = "select B.*,(select C.cityname from city C where C.cityid=B.source),(select C.cityname from city C where C.cityid=B.destination) from bus B where source='{}' and destination='{}'" .format(source,destination)

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplaySearchBus.html", {'rows': rows})

    except Exception as e:

        print("Error", e)

        return render(request, "DisplaySearchBus.html", {'row': []})


