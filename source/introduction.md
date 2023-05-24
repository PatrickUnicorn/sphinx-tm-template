# Introduction

Ce projet est un outil de création et de gestion de quiz en ligne, développé avec Vue.js. Il permet aux utilisateurs de créer leurs propres quiz personnalisés, de les tester localement. J'ai utilisé Vue.js ainsi que HTML/CSS/JavaScript pour créer une interface réactive, modifiable. Le projet est hébergé sur GitHub (en privé).

## Description initiale

Le principal objectif de mon projet est de créer des composants web capables de générer automatiquement, par exemple, des quiz (voire des examens) avec des exercices de type QCM, des textes à trou, des questions-réponses, des exercices de tri entre plusieurs colonnes, des réponses à relier et des frises chronologiques. Bien sûr, ces exercices pourront être imprimés ou alors effectués directement sur l'ordinateur avec une correction disponible pour les professeurs ou une correction automatique disponible pour les élèves en cas de simple questionnaire formatif. Les examens effectués sur ordinateur seraient dotés d'un chronomètre et d'un moyen de revenir aux questions précédentes. Les textes à trou se feraient en englobant la vraie réponse (avec des crochets '[]') parmi d'autres réponses fausses qui sont remplacées par un sélecteur de réponses pour la version sur ordinateur et qui, dans la version imprimée, remplacent juste le mot englobé par une ligne pointillée. Pour les exercices de tri dans plusieurs listes, c'est l'utilisation du Drag&Drop où les seules lignes à écrire seraient une liste de tous les termes à classer avec l'emplacement dans lequel ils doivent être situés à côté de chaque terme. Avec les QCM, écrire la question ainsi que 3 ou 4 réponses possibles en indiquant lesquelles sont justes dans un formulaire à part. Les questions à développement ou les questions à réponses courtes ne sont qu'une zone de texte qui enregistre la réponse pour la correction du professeur. Pour les questions de type chronologique, c'est aussi l'utilisation de Drag&Drop mais chaque élément est aligné avec les autres. Le but est de faire en sorte que la création du quiz avec les différentes questions soit simple et ne nécessite quasiment aucune connaissance poussée en informatique pour permettre à tout le monde de l'utiliser. Je devrais aussi, pour ceux qui font ces quiz sur ordinateur, trouver un moyen d'enregistrer les données pour les corriger et/ou les donner au professeur responsable.

## Difficultés envisagées

Il y a eu beaucoup plus de difficultés que ce que j'aurais pu imaginer - peut-être que c'était de la prétention, qui sait. J’ai commencé la programmation en début du mois d'août et, bien que j'avançasse à bon rythme, ma première difficulté était de savoir comment corriger les diverses erreurs. La deuxième était que je n'étais jamais satisfait de mon travail car il me manquait l'objectif principal : pouvoir créer de A à Z un quiz sans aucune connaissance en informatique directement sur la page web où s'affiche le composant.
Je pense que le pire était quand je réalisais que je ne possédais pas assez de connaissances pour réaliser mes tâches aisément. Ou alors, c'était le fait que je devais réviser pour les cours pour maintenir mes moyennes, car je n'ai pas le droit à l'erreur.
Enfin, pour tout dire, je suis content des deux composants relativement complets qui fonctionnent, bien sûr, et même si les autres composants que j'avais commencé à développer fonctionnent, il leur manque cette interaction avec l'utilisateur qui veut peut-être ajouter ses propres questions.

## Intérêt de l’outil

Mes composants ont pour but d'être éducatifs et divertissants pour les enseignants, les étudiants ou même simplement les personnes qui souhaitent tester leur culture générale. Les résultats sont affichés à la fin des quiz. Cet outil permet de créer facilement des questionnaires avec divers types de questions, dont un simple QCM et un quiz où l'on trie l'emplacement de divers éléments.

## Aperçu des solutions similaires existantes

Il existe de nombreuses solutions similaires pour créer des questionnaires en ligne, comme Kahoot, Google Forms et bien d'autres. Cependant, je pense que mon application de quiz se distingue par sa facilité d'utilisation et sa flexibilité pour personnaliser les questionnaires, car le code est implantable partout.

## Technologies utilisées

Vue.js est un framework JavaScript open source utilisé pour créer des interfaces utilisateur réactives et dynamiques. Il est très facile à apprendre et à utiliser. Les fonctionnalités principales de Vue.js dans mon projet incluent les composants réutilisables, le Data Fetching, la gestion des événements, les méthodes et les lifecycle hooks des composants.

## Configuration matérielle requise

Ce projet est un composant qui peut être implanté sur n'importe quelle page web et ne requiert donc pas d'appareil spécifique. Il peut être utilisé sur n'importe quel ordinateur disposant d'une connexion internet et d'un navigateur web moderne comme Chrome ou Microsoft Edge.

## Connaissances requises pour utiliser l’outil

Il n'est pas nécessaire d'avoir des connaissances techniques spécifiques pour utiliser l'outil. Il suffit de remplir les formulaires qui se présentent aux utilisateurs (administrateurs), et pour répondre au quiz, il suffit de cliquer sur un bouton pour le lancer.

## Connaissances requises pour comprendre le fonctionnement de l’outil

Pour comprendre le fonctionnement des composants, il est recommandé, voire nécessaire, de posséder des connaissances de base en HTML, CSS et JavaScript. C'est particulièrement important pour les utilisateurs qui souhaitent personnaliser l'apparence des questionnaires en codant le style eux-mêmes. Les fonctionnalités de Vue.js sont assez simples en surface, mais elles peuvent devenir complexes lorsqu'on les utilise dans des applications de plus grande envergure. Il faut aussi avoir une connaissance de base de Vue.js, notamment des directives, des computed properties, des event listeners, des méthodes, des composants, des lifecycle hooks, du routage et de la communication entre composants. Cependant, avec des connaissances basiques de JavaScript, Vue.js peut être rapidement maîtrisé pour la mise en route et la construction de quiz interactifs et dynamiques.