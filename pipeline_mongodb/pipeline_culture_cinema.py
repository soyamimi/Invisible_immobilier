[
    {
        '$match': {
            'fields.code_insee': {
                '$gte': 75000, 
                '$lte': 75999
            }
        }
    }, {
        '$group': {
            '_id': '$fields.code_insee', 
            'count_cinema': {
                '$sum': 1
            }
        }
    }, {
        '$out': 'culture_dataset'
    }
]