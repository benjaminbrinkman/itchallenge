from django.shortcuts import render_to_response
from visitorcounter.models import VisitorLog

import random

# Create your views here.
def index(request):
    visitor = VisitorLog()
    visitor.save()

    return render_to_response("index.html",
                              {
                                  "visitor_count": len(list(VisitorLog.objects.all())),
                                  "random_num": random.randint(0,1000)
                              })
