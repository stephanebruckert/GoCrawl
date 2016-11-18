import json


def output_json(queuer):
    '''
    Output the final result data and stats in JSON format
    '''

    print '\nDone:\n%s' % json.dumps(
        {
            'success':
                {
                    'total': len(queuer.results),
                    'data': queuer.results
                },
            'failures':
                {
                    'total': len(queuer.invalid),
                    'data': queuer.invalid
                }
        }, indent=2)
