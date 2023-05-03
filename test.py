import json
from datetime import datetime as datetime
test_string = """
            [{"accuracy":0.20877023166690792,"associated":false,"crs":"local","elevation_ref":"floor","floor":0,"position":{"coordinates":[-0.1275302513532863,4.40840793730435,0.31335037755167705],"type":"Point"},"properties":{"uncert":{"x":0.15649741092070282,"y":0.1381794847485367,"z":0.12177930446306706},"uwb_time":"712810851"},"provider_id":"70B3:D50F:7030:1E37","provider_type":"uwb","source":"{2ba8cf8e-09ca-4b52-bbbf-8d6118fabc28}","timestamp_generated":"2023-03-15T11:05:42.889Z","timestamp_sent":"2023-03-15T11:05:45.265Z"}]
             """
test_string = test_string.strip()

json_obj = json.loads(test_string)

print(json_obj[0]["position"]["coordinates"])
print(json_obj[0]["provider_id"])

ts_generated = json_obj[0]["timestamp_generated"]

_format = "%Y-%m-%dT%H:%M:%S.%fZ"

time_generated = datetime.strptime(ts_generated, _format)

ts_sent = json_obj[0]["timestamp_sent"]

time_sent = datetime.strptime(ts_sent, _format)

print(time_generated)
print(time_sent)
time_diff = time_sent - time_generated
print(time_diff.total_seconds())
