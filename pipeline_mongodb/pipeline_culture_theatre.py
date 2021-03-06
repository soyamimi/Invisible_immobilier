[
    {
        '$addFields': {
            'fields.code_postal': {
                '$add': [
                    '$fields.code_postal', 100
                ]
            }
        }
    }, {
        '$match': {
            'fields.code_postal': {
                '$gte': 75000, 
                '$lte': 75121
            }
        }
    }, {
        '$group': {
            '_id': '$fields.code_postal', 
            'count_theatre': {
                '$sum': 1
            }
        }
    }, {
        '$merge': {
            'into': 'culture_dataset', 
            'on': '_id', 
            'whenMatched': 'merge', 
            'whenNotMatched': 'insert'
        }
    }
]