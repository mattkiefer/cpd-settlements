import json

def prep_officer_data():
    with open('data/casecops.json', 'r') as f:
        casecops = json.loads(f.read())

    with open('data/officers_full.json', 'r') as f:
        officers = json.loads(f.read())

    for cop in casecops:
        officer_data = filter(lambda x: x.get('id', None) == cop.get('cop', None), officers)[0]

        """
        Unset some keys we're going to replace with data from the officers sheet
        """
        delete_these = [
            'cop_first_name',
            'cop_middle_initial',
            'cop_last_name'
        ]

        for key in delete_these:
            del cop[key]

        """
        Use identifying info from officers sheet:
        - First name
        - Middle initial
        - Last name
        - Gender
        - Race
        - Dates of service
        - Rank
        - Unit
        """
        use_these = [
            'first_name',
            'last_name',
            'middle_init',
            'sex',
            'race',
            'appointed_date',
            'resignation_date',
            'position_desc',
            'notes'
        ]

        for key in use_these:
            cop[key] = officer_data[key]

    with open('data/officers.json', 'w+') as f:
        f.write(json.dumps(casecops))