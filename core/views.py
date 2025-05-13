from django.shortcuts import render

# Create your views here.
def index(request):
    static_url_base = 'static/core/'
    context = {
        'cards': (
            {
                'title':    'Vint',
                'url':      'vint/',
                'img':      static_url_base + "vint-card.jpg",
                'img_alt':  'vint-card',
                'desc':     "Ці самі танки, але запущені нами та інтегровані в цей сайт",
                'hide':     False,
            },
            {
                'title':    'Minecraft',
                'url':      'minecraft/',
                'img':      static_url_base + "minecraft-card.jpg",
                'img_alt':  'minecraft-card',
                'desc':     "Ванільний Minecraft-сервер. Версія 1.21.4",
                'hide':     False,
            },
            {
                'title':    'Файли',
                'url':      'files/',
                'img':      static_url_base + "files-card.webp",
                'img_alt':  'files-card',
                'desc':     "Типу FTP-сервер. Завантажуйте файли, які вам потрібні",
                'hide':     False,
            },
            {
                'title':    'Портфоліо',
                'url':      'portfolio/',
                'img':      static_url_base + "portfolio-card-2.webp",
                'img_alt':  'portfolio-card',
                'desc':     "Моє портфоліо",
                'hide':     False,
            },
        ),
    }
    return render(request, "core/index.html", context=context)
