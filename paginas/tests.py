# paginas/tests.py
from django.test import SimpleTestCase
from django.urls import reverse


class PruebasPaginaInicio(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_correcta(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertTemplateUsed(respuesta, "inicio.html")

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, "<h1>Página de inicio</h1>")


class PruebasPaginaAcercaDe(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/acerca-de/")
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_correcta(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertTemplateUsed(respuesta, "acerca_de.html")

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertContains(respuesta, "Me llamo Ivanna")


class PruebasPaginaSaludo(SimpleTestCase):
    def test_saludo_con_nombre(self):
        respuesta = self.client.get(reverse("saludo", args=["ivanna"]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "¡Hola, Ivanna!")