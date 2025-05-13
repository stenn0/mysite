# навігаційне меню
def menu_items(request):
    return {
        'menu_items': [
            # ('vint',        'Головна'),
            ('game',        'Гра'),
            ('player_list', 'Гравці'),
            ('forum',       'Форум'),
            ('media',       'Медіа'),
            ('login',       'Увійти'),
        ]
    }
