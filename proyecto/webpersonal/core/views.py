from django.shortcuts import render, HttpResponse


# html_base = """
#     <h1>Mi web personal</h1>
#     <ul>
#         <li><a href="/">Portada</a></li>
#         <li><a href="/about-me">acerca de</a></li>
#         <li><a href="/portafolio">portafolio</a></li>
#         <li><a href="/contact">contacto</a></li>
#     </ul>
# """


def home(request):
    return render(request, "core/home.html")
    # return HttpResponse(f"{html_base}<h2>Portada</h2><p>Este es el contenido de la portada de mi p.web</p>")


def about(request):
    return render(request, "core/about_me.html")
    # return HttpResponse(f"{html_base}<h2>Acerca de</h2><p>Mi nombre es francisco y soy programador</p>")


def contact(request):
    return render(request, "core/contact.html")
    # return HttpResponse(f"{html_base}<h2>Contacto</h2><p>Formulario de contacto</p>")
