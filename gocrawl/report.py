import json


def output_json(data):
    print '\nDone:\n%s' % json.dumps(data, indent=2)
