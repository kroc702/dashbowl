---
layout: default
title: Règles de base
subtitle: les règles présenté ici suffisent à jouer votre première partie
---
* TOC
{:toc}

## Introduction

#### Matériel
Pour jouer une partie de Dash Bowl vous aurrez besoin d'un terrain pavé d’hexagone (12 x 19), avec un gabarit de rebond sur 12 cases.
Vous pouvez tenter sur un terrain de blood bowl seven voir blitz bowl, dans ce cas utilisez un D8 ou D16 pour les rebonds.

Un D12.
Vous pouvez tenter avec un D6 x2 pour les jets et un D6 pour les rebonds.

Un ballon et deux équipes (figurines, fiche d’équipe et éventuellement un deck d’action si vous testez cette règle)

#### Les équipes
La fiche d’équipe est la description de l’équipe donnant le nombre de joueur à chaque poste ainsi que leur caractéristique.
 Chaque joueur à les caractéristiques suivante :
- **Poste** : le type de joueur, la figurine doit permettre de distinguer le poste du joueur. Le poste peut avoir un impact sur certaine cartes ou talent d’équipe.
- **Mouvement** (M [3-9]) : plus que le nombre de case de déplacement, cela correspond au nombre d’action possible lors d’une activation. Certaines actions demandes plusieurs points de mouvement.
- **Lancer** (L [4-10+]) : la capacité du joueur à effectuer une passe.
- **Blocage** (B [4-10+]) : la capacité du joueur à bloquer ou tacler un joueur adverse.
- **Armure** (A [4-10+]) : représente aussi sa masse et son agilité. La capacité du joueur à rester debout suite à un blocage.

#### Début de partie
L’équipe qui joue à domicile débute le jeu en défense, celle qui joue à l’extérieur engage et donc joue en premier. On peut tirer à pile ou face pour les matches amicaux.

Ensuite chaque équipe/coach jouent à tour de role en activant leur joueur un par un. L'ordre est important car en cas d'échec le tour de l'équipe prend fin imédiatement, c'est un turnover.

## Glossaire
- **Joueur** : une figurine sur le terrain
- **Coach** : la personne qui déplace les figurines
- **Joueur debout** : un joueur qui n’est pas à terre
- **Joueur libre** : un joueur debout qui n'a aucun joueur debout de l’équipe adverse adjacent
- **Joueur marqué** : un joueur debout qui a au moins un joueur debout de l’équipe adverse adjacent
- **Joueur multi-marqué** : un joueur marqué qui a au moins deux joueurs debout de l’équipe adverse adjacent
- **Joueur à terre** : Un joueur à terre ne peut que se relever lors de son activation.
Un joueur mis à terre doit immédiatement lâcher le ballon (cf rebondit)
- **Joueur ko** : retiré du plateau jusqu’au prochain touchdown
- **Rebond** : le ballon est déplacé sur une case déterminée aléatoirement sur l’une des 12 cases autour du point de rebond (les 6 cases adjacentes et 6 autres à 2 cases de distance). Si le ballon arrive sur un joueur libre, celui-ci s’en empare.
Si le ballon arrive sur un joueur marqué ou à terre, le ballon rebondi une nouvelle fois.
Si le ballon doit atterrir en dehors du plateau ou sur un obstacle, le ballon doit atterrir sur la case opposée.
- **Jet de passe, Jet de blocage, Jet d’armure** : le coach du joueur concerné doit lancer un dé 12 et y ajouter un éventuel modificateur. Si le résultat est supérieur ou égal à la compétence correspondante du joueur c’est une réussite. Sinon c’est un échec et l’activation du joueur actif prend fin.
Les effets sont détaillé dans les sections concernés.
- **Maladresse** : si lors d’un jet de dé le coach fait <=2 naturel ou après modificateur, alors le joueur fait une maladresse.
- **Turn over** : après une maladresse du joueur actif, le tour de son coach s’arrête immédiatement même si tous les joueurs n’ont pas été activé.


## Tour d’engagement
L’équipe en défense place ses joueurs à 5 cases ou moins de sa ligne de touchdown.

L’équipe attaquante place ses joueurs dans sa ligne de touchdown, donne le ballon à l’un d’eux, puis les actives normalement.

## Les autres tours se déroule tous de la même façon
L’équipe en défense joue en activant ses joueurs un par un, puis l’équipe attaquante fait de même.

L’activation d’un joueur lui permet de réaliser les actions suivantes dans la limite de sa caractéristique de mouvement :

#### Courir (joueur libre - 1M)
Déplacer le joueur libre d'une case, ce joueur doit être encore libre après ce mouvement.

#### Marquer (joueur libre - 2M)
Déplacer le joueur libre d'une case.

#### Passe (joueur libre - Une seule par tour par équipe, 1M + jet de lancer)
Un joueur libre peu utiliser 1M pour tenter une action de passe sur un coéquipier receveur.
- 1 case & receveur libre : réussite automatique
- <= 4 cases : jet de lancer
- <= 8 cases : jet de lancer -1
- Receveur marqué : -1 par marquage

Résultat:
-	Maladresse : Le ballon rebondi autour du lanceur. Turnover.
-	Echec : Le ballon rebondi autour de la cible. Le joueur actif et le receveur ne peuvent plus être activé ce tour ci
-	Réussite : Le ballon arrive dans les mains du receveur

#### Ramasser le ballon (joueur libre/marqué - 1M)
Si pendant son activation, un joueur libre ou marqué ce trouve sur la même case que le ballon, il peut utiliser un point de mouvement pour s’emparer de celui-ci.

S’il ne le fait pas, le ballon rebondi.

Si le joueur est marqué, il doit faire un jet d’armure (-1 par joueur supplémentaire le marquant)
-	Maladresse : le joueur actif est à terre. Le ballon rebondit. Turnover.
-	Echec : Le ballon rebondit. Fin de l’activation.
-	Réussite : Le ballon est dans les mains du joueur actif.

#### Esquiver (joueur marqué - 2M)
Déplacer le joueur marqué d'une case.

A moins qu’il ne soit marqué uniquement par des joueurs multi-marqué, le joueur doit faire un jet d’armure avec -1 par joueur supplémentaire le marquant.
-	Maladresse : Le joueur est à terre. Turnover.
-	Echec : Le joueur est à terre.
-	Réussite : Le joueur est debout et peut continuer sont activation normalement.

#### Blocage (joueur marqué - 2M + jet de blocage)
Un joueur marqué peu utiliser 2 points de mouvements pour tenter de bloquer un joueur adverse qu’il marque.
Le coach du joueur actif doit faire un jet de blocage avec les modificateurs suivants :
- +1 pour chaque joueur marquant le défenseur.
- -1 pour chaque joueur marquant le joueur actif.

Resultat:
-	Maladresse : le joueur actif est à terre. Turnover.
-	Échec : rien ne se passe. L’activation du joueur actif prend fin.
-	Réussite, le joueur défenseur doit faire un jet d’armure, s’il avait le ballon, celui-ci rebondi :
    - -1 pour chaque joueur marquant le défenseur.
    - +1 pour chaque joueur marquant le joueur actif.

    Resutat:
    -	Maladresse, le défenseur est KO
    -	Échec, le défenseur est à terre
    -	Réussite, le coach du joueur actif choisi de déplacer le joueur défenseur sur l’une des 3 cases vide opposé. Si ce n’est pas   possible, le défenseur est à terre.
    Le joueur actif peut se déplacer gratuitement sur la case précédemment occupé par le joueur défenseur.

#### Se relever (joueur à terre - action unique)
Un joueur à terre (pas ko) au début du tour peut se relever. Il ne peut faire aucune autre action pendant son activation.
S’il est marqué, il doit faire un jet d’armure.
-	Maladresse : le joueur est KO. Turnover.
-	Echec : Le joueur reste à terre.
-	Réussite : Le joueur est debout.

## Touchdown
Dès qu’un joueur en possession du ballon se trouve dans la zone de touchdown adverse, le tour prend fin et son équipe marque un point.
Un nouvel engagement a lieu comme au tour 0. L’équipe venant de marquer est désormais l’équipe en défense.

## Fin de partie
Les conditions de fin de partie doivent être précisé. Deux options possibles :
- la partie peut s’arrêter après 12 tours complet.
- la partie peut s’arrêter dès qu’une équipe marque 3 touchdown.
