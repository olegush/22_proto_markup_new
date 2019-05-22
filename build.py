from staticjinja import Site


main_data = {
    'user': 'Леонид Федорович',
    'regions': {'selected_region': 'Новосибирск и область',
                'list_region': [
                    {'url': '#', 'name': 'Новосибирск и область'},
                    {'url': '#', 'name': 'Москва и область'},
                ],
                },
}
order = {
    'publication_datetime': 'Вчера, в 21:30',
    'user_name': 'Алексей',
    'count_views': 12,
    'order_text': '60 шт. ПК от 72-15 до ПК 21-15, '
                 'Криводановка, с доставкой.',
}
comment = {'user_avatar': 'img/avatar_default.png',
           'user_name': 'Кирилл',
           'user_age': 29,
           'user_city': 'Барабинск',
           'comment_text': """Бла, бла, бла! Мне помогло, все супер!
                            Бла, бла, бла! Мне помогло, все супер!
                            Бла, бла, бла! Мне помогло, все супер!""",
           }

index_data = {
    'title': 'Поставщики Новосибирска',
    'orders_list': [order for number in range(4)],
    'list_of_comments': [comment for number in range(3)],
    'need_to_show_notify_message': 1,
}
index_data.update(main_data)

orders_data = {
    'title': 'Заявки',
    'orders_list': [order for number in range(10)]

}

orders_data.update(main_data)


if __name__ == "__main__":
    site = Site.make_site(outpath='static',
                                 contexts=[('index.html', index_data),
                                           ('orders.html', orders_data)]
                                 )
    site.render(use_reloader=True)
