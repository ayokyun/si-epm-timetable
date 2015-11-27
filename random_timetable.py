
year, month = 2015, 12

from calendar import Calendar

def consumed_hours():
    from numpy.random import normal
    return round(normal(10.5, 0.3), 1)

cal = Calendar()
for d in cal.itermonthdates(year, month):
    if d.month != month:
        print '%2d/%2d'%(d.month, d.day),
    else:
        print '%5d'%d.day,

    if d.weekday() >= 6:
        print

        print ' '.join(['%5.1f'%consumed_hours() for _ in range(5)]),
        print ' '.join(['%5s'%'-' for _ in range(2)])

        print '-'*42
