from django.test import TestCase
from django.urls import reverse

from .models import Producto


class ProductoModelTest(TestCase):
    def test_str_producto(self):
        producto = Producto.objects.create(
            nombre='Mouse',
            descripcion='Mouse inalámbrico',
            precio=399.99,
            stock=5,
            categoria='Accesorios',
        )
        self.assertEqual(str(producto), 'Mouse')


class ProductoViewsTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre='Teclado',
            descripcion='Teclado mecánico',
            precio=999.99,
            stock=10,
            categoria='Accesorios',
        )

    def test_lista_productos_responde_200(self):
        response = self.client.get(reverse('lista_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teclado')

    def test_crear_producto(self):
        response = self.client.post(reverse('crear_producto'), {
            'nombre': 'Monitor',
            'descripcion': 'Monitor 24 pulgadas',
            'precio': '2999.99',
            'stock': '3',
            'categoria': 'Pantallas',
            'activo': True,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Producto.objects.count(), 2)
