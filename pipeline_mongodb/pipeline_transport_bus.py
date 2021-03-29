[
    """ This pipeline is for cleaning Bus data """
    {
        '$match': {
            'fields.codeinsee': {
                '$gte': 75000, 
                '$lte': 75999
            }
        }
    }, {
        '$project': {
            'fields.codeinsee': 1, 
            'fields.ligne': 1
        }
    }, {
        '$group': {
            '_id': '$fields.codeinsee', 
            'count_bus': {
                '$sum': 1
            }, 
            'list_bus_line': {
                '$addToSet': '$fields.ligne'
            }
        }
    }, {
        '$addFields': {
            'count_bus_line': {
                'count': {
                    '$size': '$list_bus_line'
                }
            }
        }
    }, {
        '$out': 'transport_dataset'
    }
]
