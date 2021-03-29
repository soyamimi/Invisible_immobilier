[
    """ This pipeline is for cleaning University data """
    {
        '$group': {
            '_id': '$fields.com_code', 
            'total_count_enseignement_sup': {
                '$sum': 1
            }, 
            'private_enseignement_sup': {
                '$sum': {
                    '$cond': [
                        {
                            '$eq': [
                                '$fields.secteur_d_etablissement', 'Privé'
                            ]
                        }, 1, 0
                    ]
                }
            }, 
            'public_enseignement_sup': {
                '$sum': {
                    '$cond': [
                        {
                            '$eq': [
                                '$fields.secteur_d_etablissement', 'Public'
                            ]
                        }, 1, 0
                    ]
                }
            }
        }
    }, {
        '$match': {
            '_id': re.compile(r"75")
        }
    }, {
        '$addFields': {
            '_id': {
                '$convert': {
                    'input': '$_id', 
                    'to': 'int'
                }
            }
        }
    }, {
        '$merge': {
            'into': 'education_dataset', 
            'on': '_id', 
            'whenMatched': 'merge', 
            'whenNotMatched': 'insert'
        }
    }
]
