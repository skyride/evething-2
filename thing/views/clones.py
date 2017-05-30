from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum

from thing.models import *
from thing.stuff import *


@login_required
def clones_home(request):
    stations = Station.objects.annotate(
        clone_count=Count('clones')
    ).filter(
        clones__character__esitoken__user=request.user,
        clone_count__gt=0
    ).order_by(
        'name'
    ).all()

    out = render_page(
        'thing/clones.html',
        {
            'stations': stations
        },
        request
    )

    return out
