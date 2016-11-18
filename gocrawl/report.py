import json


def output_json(data):
    '''
    Output the final result in JSON format
    '''
    print '\nDone:\n%s' % json.dumps(data, indent=2)
