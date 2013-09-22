import json


def as_year(date):
    return date['year']


with open('profile.json', 'r') as f:
    profile = json.loads(f.read())

with open('education.tex', 'w') as f:
    for education in profile['educations']['values']:
        print >> f, '%-------------------------------'
        print >> f, '\entry'
        print >> f, "{%d--%d}" % (
            as_year(education['startDate']),
            as_year(education['endDate']))
        print >> f, "{%s}" % education['degree']
        print >> f, "{%s}" % education['schoolName']
        print >> f, "{%s}" % education['fieldOfStudy']

with open('experience.tex', 'w') as f:
    for position in profile['positions']['values']:
        print >> f, '%-------------------------------'
        print >> f, '\entry'
        print >> f, "{%s--%s}" % (
            as_year(position['startDate']),
            as_year(position['endDate']) if position.get('endDate', None) else 'Now')
        print >> f, "{%s}" % position['company']['name']
        print >> f, "{Mexico City, Mexico}"
        print >> f, "{\emph{%s} \\\\" % position['title'],
        print >> f, position.get('summary', ""),
        print >> f, "}"
