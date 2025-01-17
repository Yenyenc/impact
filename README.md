[![test](https://github.com/betagouv/impact/actions/workflows/test.yml/badge.svg)](https://github.com/betagouv/impact/actions/workflows/test.yml)

# Plateforme Impact

https://beta.gouv.fr/startups/plateforme.impact.html


## développement local

### installation

Installer [`pipenv`](https://pypi.org/project/pipenv/) puis le projet avec

```
make install
```

Il est nécessaire d'installer le paquet système `libpq-dev` pour avoir `pg_config`.

### lancement


Créer le fichier de variable d'environnement `.env` à partir du fichier d'exemple `.env.example`
Pour activer l'intégration avec Sentry, il est nécessaire de renseigner la variable d'environnement SENTRY_DSN


```
make migrate
make run
```

Le service est disponible sur http://127.0.0.1:8000

### migration

Pour générer les nouvelles migrations éventuelles et les appliquer :

```
make migrations
make migrate
```

### test

Exécuter les tests avec :

```
make test
```

### pre-commit

Le projet utilise [pre-commit](https://pre-commit.com/) pour vérifier le formattage du code automatiquement à chaque commit.
La cible `make install` l'installe directement.


## migration en recette


```
scalingo --app ${PROJET} run python3 impact/manage.py migrate
```

Cette commande est jouée automatiquement lors de tout déploiement.

Pour lister les migrations jouées en recette :

```
scalingo --app ${PROJET} run python3 impact/manage.py showmigrations
```

Pour défaire des migrations déjà appliquées en recette **avant** de déployer une branche où l'historique des migrations est différent/a changé (et ainsi éviter les exceptions de type InconsistentMigrationHistory au déploiement et d'avoir à supprimer toutes les données) :
https://docs.djangoproject.com/fr/4.1/ref/django-admin/#django-admin-migrate

```
scalingo --app ${PROJET} run python3 impact/manage.py migrate NOM_DE_L_APP_DJANGO NOM_DE_LA_DERNIERE_MIGRATION_A_LAQUELLE_ON_SOUHAITE_REVENIR
```


### suppression des données

Pour supprimer toutes les données en recette :

```
scalingo --app ${PROJET} pgsql-console
drop owned by ${PROJET}_3273;
```

Penser à créer à nouveau le super utilisateur une fois l'application redéployée/les migrations rejouées avec :

```
scalingo --app ${PROJET} run python3 impact/manage.py createsuperuser
```
