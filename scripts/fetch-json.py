import json
from linkedin import server

# Example linkedin-python key and secret
KEY = 'wFNJekVpDCJtRPFX812pQsJee-gt0zO4X5XmG6wcfSOSlLocxodAXNMbl0_hw3Vl'
SECRET = 'daJDa6_8UcnGMw1yuq9TjoO_PMKukXMo8vEMo7Qv5J-G3SPgrAV0FqFCd0TNjQyG'

application = server.quick_api(KEY, SECRET)

profile = application.get_profile(selectors=['educations', 'positions'])

with open('profile.json', 'w') as f:
    f.write(json.dumps(profile))
