# Python client/server example

Dit voorbeeld maakt gebruik van [Flask](http://flask.pocoo.org/) voor het server-gedeelte, de client gebruikt alleen Python standard library bibliotheken.

Je kan Flask installeren met `./setup.sh`. Dit gaat er van uit dat [virtualenv](https://virtualenv.pypa.io/en/stable/) beschikbaar is.

Start nu de server met `./run_server.sh`. Dit start de server op poort 5000. De server verstaat volgende HTTP commandos:

```
GET /
POST /roerder_aan
POST /roerder_uit
```

Je kan dit test van op de command line met `curl`

```
curl localhost:5000

curl -X POST localhost:5000/roerder_aan

curl -X POST localhost:5000/roerder_uit
```

Het programma `client.py` toont hoe je dit kan aanroepen vanuit Python. Gebruik opnieuw `run_python.sh` zodat je zeker bent dat de virtualenv geactiveerd wordt.

```
$ run_python.sh
{u'verwarming': False, u'temperatuur': 25.88, u'roerder': True, u'bierpomp': False}
roerder wordt omgeschakeld
{u'verwarming': False, u'temperatuur': 25.88, u'roerder': False, u'bierpomp': False}
```
