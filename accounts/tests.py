from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AuthenticationFlowTests(TestCase):
    password = "SenhaSegura!2026"

    def register(self, **overrides):
        data = {
            "full_name": "Ana da Silva",
            "email": "ANA@EXAMPLE.COM",
            "password": self.password,
            "password_confirmation": self.password,
        }
        data.update(overrides)
        return self.client.post(reverse("accounts:cadastro"), data)

    def test_valid_registration_normalizes_email_and_hashes_password(self):
        response = self.register()
        user = get_user_model().objects.get(username="ana@example.com")
        self.assertRedirects(response, reverse("accounts:login"))
        self.assertEqual(user.email, "ana@example.com")
        self.assertEqual(user.get_full_name(), "Ana da Silva")
        self.assertNotEqual(user.password, self.password)
        self.assertTrue(user.check_password(self.password))

    def test_registration_rejects_duplicate_email_case_insensitively(self):
        self.register()
        response = self.register(email="ana@example.com")
        self.assertContains(response, "Já existe uma conta cadastrada com este e-mail.")
        self.assertEqual(get_user_model().objects.count(), 1)

    def test_registration_rejects_different_passwords(self):
        response = self.register(password_confirmation="OutraSenha!2026")
        self.assertContains(response, "As senhas não coincidem.")
        self.assertEqual(get_user_model().objects.count(), 0)

    def test_login_and_safe_next_url(self):
        self.register()
        response = self.client.post(reverse("accounts:login"), {
            "email": "ana@example.com", "password": self.password, "next": "/curso/",
        })
        self.assertRedirects(response, reverse("core:curso"))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_rejects_invalid_password_and_external_next_url(self):
        self.register()
        response = self.client.post(reverse("accounts:login"), {
            "email": "ana@example.com", "password": "senha-errada", "next": "https://example.org/",
        })
        self.assertContains(response, "E-mail ou senha inválidos.")
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_private_pages_require_login_and_return_to_the_requested_page(self):
        course = self.client.get(reverse("core:curso"))
        player = self.client.get(reverse("core:player", args=[1, 1]))
        login_url = reverse("accounts:login")
        self.assertRedirects(course, f"{login_url}?next={reverse('core:curso')}")
        self.assertRedirects(player, f"{login_url}?next={reverse('core:player', args=[1, 1])}")

    def test_authenticated_user_sees_own_name_and_can_logout(self):
        user = get_user_model().objects.create_user(
            username="joao@example.com", email="joao@example.com", password=self.password,
            first_name="João", last_name="Souza",
        )
        self.client.force_login(user)
        response = self.client.get(reverse("core:curso"))
        self.assertContains(response, "Olá, João Souza!")
        logout_response = self.client.post(reverse("accounts:logout"))
        self.assertRedirects(logout_response, reverse("core:home"))
        self.assertRedirects(self.client.get(reverse("core:curso")), f"{reverse('accounts:login')}?next={reverse('core:curso')}")

    def test_forms_are_csrf_protected(self):
        client = Client(enforce_csrf_checks=True)
        response = client.post(reverse("accounts:cadastro"), {
            "full_name": "Ana da Silva", "email": "ana@example.com",
            "password": self.password, "password_confirmation": self.password,
        })
        self.assertEqual(response.status_code, 403)
