import httplib
import json

conn = httplib.HTTPConnection("localhost:5000")

def GET(path):
    conn.request("GET", path)
    res = conn.getresponse()
    conn.close
    return res

def POST(path):
    conn.request("POST", path)
    return conn.getresponse()

def status():
    res = GET("/")
    if res.status == 200:
        return json.loads(res.read())
    else:
        print "Getting status failed: ", res.status, res.reason
        return {}

def toggle_roerder():
    roerder = status()['roerder']
    if roerder:
       POST("/roerder_uit")
    else:
       POST("/roerder_aan")

############################################################

print status()

print "roerder wordt omgeschakeld"
toggle_roerder()

print status()
