[
    """ This pipeline is for cleaning Metro data """
    {
        '$match': {
            'fields.codeinsee': {
                '$gte': 75000, 
                '$lte': 75999
            }
        }
    }, {
        '$project': {
            'fields.codeinsee': 1
        }
    }, {
        '$group': {
            '_id': '$fields.codeinsee', 
            'count_metro': {
                '$sum': 1
            }
        }
    }, {
        '$merge': {
            'into': 'transport_dataset', 
            'on': '_id', 
            'whenMatched': 'merge', 
            'whenNotMatched': 'insert'
        }
    }
]
