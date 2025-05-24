from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ProdutoNome, Fornecedor, Lote

# Create your tests here.

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    # ====================
    # Teste Login
    # ====================
    def test_login_success(self):
        response = self.client.post(reverse('login_submit'), {
            'usuario': 'testuser',
            'senha': 'testpass'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    # ====================
    # Teste Registro
    # ====================
    def test_register_user_success(self):
        response = self.client.post(reverse('create_usuario'), {
            'usuario': 'newuser',
            'email': 'newuser@test.com',
            'senha1': 'testpassword',
            'senha2': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertTrue(User.objects.filter(username='newuser').exists())
        response = self.client.get(reverse('home'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    # ====================
    # Teste Produto
    # ====================
    def test_create_produto(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('produtossubmit'), {
            'Nomeproduto': 'ProdutoTeste',
            'Formail1produto': 'email1@test.com',
            'Formail2produto': 'email2@test.com',
            'Formail3produto': '',
            'Formail4produto': '',
            'Formail5produto': '',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/produtos/')
        self.assertTrue(ProdutoNome.objects.filter(Nome='ProdutoTeste').exists())

    # ====================
    # Teste Fornecedor
    # ====================
    def test_create_forn(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('fornsubmit'), {
            'Nomefornecedor': 'FornecedorTeste',
            'Emailfornecedor': 'forn@test.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/forn/')
        self.assertTrue(Fornecedor.objects.filter(Nome='FornecedorTeste').exists())

    # ====================
    # Teste Lote
    # ====================
    def test_create_lote(self):
        self.client.login(username='testuser', password='testpass')
        produto = ProdutoNome.objects.create(Nome='ProdutoTeste')
        response = self.client.post(reverse('lotessubmit'), {
            'Nomelote': 'ProdutoTeste',
            'Quantlote': 10,
            'Nlotelote': '123ABC',
            'Valilote': '2030-12-31',
            'Usurlote': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertTrue(Lote.objects.filter(Nlote='123ABC').exists())

    # ====================
    # Teste Deletar Produto
    # ====================
    def test_delete_produto(self):
        self.client.login(username='testuser', password='testpass')
        ProdutoNome.objects.create(Nome='ProdutoDeletar')
        response = self.client.get(reverse('proddelet', args=['ProdutoDeletar']))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/produtos/')
        self.assertFalse(ProdutoNome.objects.filter(Nome='ProdutoDeletar').exists())

    # ====================
    # Teste Gráfico de Quantidade
    # ====================
    def test_quantidade_graf(self):
        self.client.login(username='testuser', password='testpass')
        ProdutoNome.objects.create(Nome='ProdutoGraf')
        Lote.objects.create(Nome='ProdutoGraf', Quantidade=5, Nlote='NL1', Validade='2030-01-01', Usuario=self.user)

        response = self.client.get(reverse('graf'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grafico.html')
        self.assertContains(response, 'ProdutoGraf')
