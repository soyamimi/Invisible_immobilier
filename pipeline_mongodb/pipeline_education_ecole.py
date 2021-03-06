[
    {
        '$match': {
            'fields.libelle_academie': 'Paris'
        }
    }, {
        '$group': {
            '_id': '$fields.code_commune', 
            'total_count_ecole': {
                '$sum': 1
            }, 
            'private_ecole': {
                '$sum': {
                    '$cond': [
                        {
                            '$eq': [
                                '$fields.secteur_public_prive_libe', 'Privé'
                            ]
                        }, 1, 0
                    ]
                }
            }, 
            'public_ecole': {
                '$sum': {
                    '$cond': [
                        {
                            '$eq': [
                                '$fields.secteur_public_prive_libe', 'Public'
                            ]
                        }, 1, 0
                    ]
                }
            }
        }
    }, {
        '$out': 'education_dataset'
    }
]