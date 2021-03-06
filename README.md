# QCM application

## Overview

This project is a QCM application and the last project of a formation.


## Pré-requis 

Il est nécessaire d'avoir installer les outils ci-dessous 
- Docker
- Jenkins

Dans un second temps il vous faudra récupérer le dossier git qui se trouve à l'adresse suivante : https://github.com/NicolasWattiez/projet_formation_ajc

Pour le cloner sur votre machine, ouvrir un terminal et effectuer la commande suivante :
```
git clone git@github.com:NicolasWattiez/projet_formation_ajc.git
```
## Nettoyer son espace de travail si besoin (facultatif) 

Si vous avez des conteneurs qui tournent pour rien ou qui peuvent interférer avec ceux que nous allons installer il peut être utile de tous les arrêter et les supprimer 
``` 
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

## Se placer dans le dossier de travail

Se déplacer dans le dossier de travail 
```
cd projet_formation_ajc
```

## Création des hôtes

Nous allons utiliser le fichier docker-compose.yml pour créer le master, 2 hôtes ubuntu (1 pour l'application python et 1 pour la base de donnée) 

```
docker-compose up -d
```

## Copier les fichier utiles dans les conteneurs master et jenkins

Copiet le contenu du dossier ansible, src et bdd dans le conteneur master : 
```
docker cp ansible/. master:/etc/ansible/
docker cp bdd/. master:/etc/ansible/bdd/
docker cp src/. master:/etc/ansible/src/
```
Copier le Jenkinsfile dans le conteneur jenkins
```
docker cp Jenkinsfile jenkins:/home
```

## Configuration des hôtes

__1) Connexion au master__

```
docker exec -it master sh
```
Vous êtes désormais connecté dans le master, nous allons maintenant connecter le master aux 2 hôtes via ssh 

__2) Connexion en SSH :__ effectuer les commandes ci-dessous dans le master, une par une : (les deux dernières étapes sont là pour s'assurer que la clé ssh ait bien été ajoutée)

```
ssh-keygen
eval "$(ssh-agent)"
ssh-add /root/.ssh/id_rsa
```
*NB: penser à modifier /root/.ssh/id_rsa si vous avez enregistré votre clé ailleurs que dans le chemin par défaut*

__3) Copie de la clé sur les machines hôtes :__  il vous faudra effectuer les commandes suivantes (le mot de passe du root est *toor*)

```
ssh-copy-id root@dbubuntu 
ssh-copy-id root@appubuntu
```

__4) Connexion aux hôtes :__ nous allons nous connecter aux hôtes pour vérfier que la clé ssh est bien été copiée sur chacun des hôtes (une fois connecté, il faut penser à faire "exit" pour revenir dans le master et lancer une nouvelle connexion ssh )

```
ssh root@dbubuntu
exit
ssh root@appubuntu
exit
```
On se déconnecte maintenant du conteneur master
```
exit
```

## Connexion au conteneur master depuis le conteneur jenkins
Nous allons nous connecter au conteneur master depuis le conteneur jenkins pour pouvoir par la suite lancer nos playbook via le Jenkinsfile

``` 
docker exec -it jenkins sh
ssh-keygen
eval "$(ssh-agent)"
ssh-add /root/.ssh/id_rsa
ssh-copy-id root@master
ssh root@master
exit
```

## Connexion a Jenkins
Ouvre jenkins dans un onglet de votre navigateur en tapant localhost:8098
COnfigurez le si nécessaire en respectant les étapes indiqués sur Jenkins. 

Une fois sur Jenkins :

1) Se rendre sur Manage Jenkins
2) Se rendre dans Global Tool Configuration 
3) Ajouter un Gradle en lui donnant le nom 'gradle'
4) Save
5) Retourner dans Manage jenkis puis dans Manage Plug-in
6) Cliquer sur Available puis chercher SSH Pipeline Steps, le sélectionner et l'installer
7) Créer un projet pipeline et donné lui un nom 
8) Dans Pipeline définition choisir Pipeline Script from SCM
9) Choisir git
10) Copier l'url suivant dans la case correspondante :https://github.com/NicolasWattiez/projet_formation_ajc
11) Dans branch to build saisir : */main
12) Save 
13) Lancer le Build Now
