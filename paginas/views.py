from django.shortcuts import render
from django.views.generic import TemplateView 

class VistaAcercaDe(TemplateView):  
    template_name = "acerca_de.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nombre"] = "Ivanna"
        contexto["edad"] = 22
        return contexto

def vista_inicio(request):
    contexto = {
        "habilidades": ["Python", "Django", "Git"],
        "mensaje": "GRACIAS por VISITAR mi sitio.",
    }
    return render(request, "inicio.html", contexto)


class VistaProyectos(TemplateView):  
    template_name = "proyectos.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["proyectos"] = [
            "Aplicación de monitoreo ergonómico",
            "Plataforma de rutas y turismo local",
            "Videojuego de plataformas 2D",
        ]
        return contexto

def vista_saludo(request, nombre):  
    return render(request, "saludo.html", {"nombre": nombre})

def vista_cuadrado(request, numero):  
    cuadrado = numero**2
    contexto = {
        "numero": numero,
        "cuadrado": cuadrado,
    }
    return render(request, "cuadrado.html", contexto)
