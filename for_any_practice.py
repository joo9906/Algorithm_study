data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for i in data:
    i.setdefault('company', 'unknown')
    print(f'name은/는 {i.get('name')}입니다.\ncompany은/는 {i.get('company')}입니다.\nis_collapsible은/는 {i.get('is_collapsible')}입니다.')
    print('')