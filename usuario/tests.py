# -*- coding: utf-8 -*-

from django.test import TestCase
from usuario.models import UsuarioPendente

#view test
class CadastroViewsTests(TestCase):
    def valida_envio_sem_usuario(self):
        """
        Valida envio sem usuario
        """
        #import ipdb; ipdb.set_trace()
        self.client.login(username='user', password='test')
        response = self.client.post('/cadastro/cadastrar/', {'usuario': '', 'senha': 'smith', 'confirmacao_senha': '', 'email':'','confirmacao_email':'','dia':'','mes':'','ano':'','sexo':'','cidade':''})
        self.assertEqual(response.content, 'sem_usuario')
        self.assertEqual(response.status_code, 200)

    def valida_usuario_existente(self):
        """
        Valida usuario existente
        """
        #response.status_code - 200
        response = u.post('/cadastro/cadastrar/', {'usuario': 'allan', 'senha': 'smith', 'confirmacao_senha': '', 'email':'','confirmacao_email':'','dia':'','mes':'','ano':'','sexo':'','cidade':''})
        self.assertEqual(response.content, 'sem_usuario')



    #def testar_nada(self):
        #self.assertEqual(1,1)
        #w = self.create_whatever()
        #url = reverse("whatever.views.whatever")
        #resp = self.client.get(url)

        #self.assertEqual(resp.status_code, 200)
        #self.assertIn(w.title, resp.content)
