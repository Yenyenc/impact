import pytest
from django.urls import reverse

from entreprises.models import Entreprise, Habilitation
from users.models import User


def test_page_creation(client):
    response = client.get("/creation")

    assert response.status_code == 200
    content = response.content.decode("utf-8")
    assert "<!-- page creation compte -->" in content


@pytest.mark.parametrize("reception_actualites", ["checked", ""])
def test_create_user_with_real_siren(reception_actualites, client, db):
    data = {
        "prenom": "Alice",
        "nom": "User",
        "email": "user@example.com",
        "password1": "Passw0rd!123",
        "password2": "Passw0rd!123",
        "siren": "130025265",  #  Dinum
        "acceptation_cgu": "checked",
        "reception_actualites": reception_actualites,
        "fonctions": "Présidente",
    }

    response = client.post("/creation", data=data, follow=True)

    assert response.status_code == 200
    assert response.redirect_chain == [(reverse("reglementations"), 302)]

    assert (
        "Votre compte a bien été créé. Vous êtes maintenant connecté."
        in response.content.decode("utf-8")
    )

    user = User.objects.get(email="user@example.com")
    entreprise = Entreprise.objects.get(siren="130025265")
    assert user.created_at
    assert user.updated_at
    assert user.email == "user@example.com"
    assert user.prenom == "Alice"
    assert user.nom == "User"
    assert user.acceptation_cgu == True
    assert user.reception_actualites == (reception_actualites == "checked")
    assert user in entreprise.users.all()
    assert (
        Habilitation.objects.get(user=user, entreprise=entreprise).fonctions
        == "Présidente"
    )
    assert user.check_password("Passw0rd!123")


def test_account_page_is_not_public(client):
    response = client.get("/mon-compte")

    assert response.status_code == 302


def test_account_page_when_logged_in(client, alice):
    client.force_login(alice)

    response = client.get("/mon-compte")

    assert response.status_code == 200
    content = response.content.decode("utf-8")
    assert "<!-- page mon compte -->" in content, content


@pytest.fixture
def alice(django_user_model):
    alice = django_user_model.objects.create(
        prenom="Alice",
        nom="Cooper",
        email="alice@example.com",
        reception_actualites=False,
    )
    alice.set_password("Passw0rd!123")
    alice.save()  # il faut save après set_password
    return alice


def test_edit_account_info(client, alice):
    client.force_login(alice)

    data = {
        "prenom": "Bob",
        "nom": "Dylan",
        "email": "bob@example.com",
        "reception_actualites": "checked",
    }

    response = client.post("/mon-compte", data=data, follow=True)

    assert response.status_code == 200
    assert response.redirect_chain == [(reverse("account"), 302)]

    content = response.content.decode("utf-8")
    assert "Votre compte a bien été modifié." in content

    alice.refresh_from_db()
    assert alice.prenom == "Bob"
    assert alice.nom == "Dylan"
    assert alice.email == "bob@example.com"
    assert alice.reception_actualites
    assert alice.check_password("Passw0rd!123")


def test_edit_account_info_and_password(client, alice):
    client.force_login(alice)

    response = client.get("/mon-compte")

    assert response.status_code == 200

    data = {
        "prenom": "Bob",
        "nom": "Dylan",
        "email": "bob@example.com",
        "reception_actualites": "checked",
        "password1": "Yol0!1234567",
        "password2": "Yol0!1234567",
    }

    response = client.post("/mon-compte", data=data, follow=True)

    assert response.status_code == 200
    assert response.redirect_chain == [
        (reverse("account"), 302),
        (
            f"{reverse('login')}?next=/mon-compte",
            302,
        ),  # l'utilisateur doit se reconnecter
    ]

    content = response.content.decode("utf-8")
    assert (
        "Votre mot de passe a bien été modifié. Veuillez vous reconnecter." in content
    )

    user = User.objects.get(email="bob@example.com")
    alice.refresh_from_db()
    assert alice.prenom == "Bob"
    assert alice.nom == "Dylan"
    assert alice.email == "bob@example.com"
    assert alice.reception_actualites
    assert alice.check_password("Yol0!1234567")