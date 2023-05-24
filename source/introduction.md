# Introduction :

Ce projet est un outil de création et de gestion de quiz en ligne, développé avec Vue.js. Il permet aux utilisateurs de créer leurs propres quiz personnalisés, de les essayer en local. J’ai utilisé Vue.js et le HTML/CSS/JavaScript pour créer une interface réactive dont l'on peut modifier. Le projet est hébergé sur GitHub (en Privé).

## Description initiale

Le principal but de mon projet est de créer un composants web capable de générer automatiquement, par exemple, des quiz (voire des examens) avec des exercices de type QCM mais aussi des textes à trou, des question-réponse, des exercices de triages entre plusieurs colonnes, des réponses à relier et des frises chronologiques. Bien sur ces exercices pourront être imprimer ou alors être directement effectué sur ordinateur avec une correction disponible pour les professeurs ou une correction automatique disponible pour les élèves en cas de simple questionnaire formatif. Les examens effectués sur ordinateur serait doté d’un chronomètre et d’un moyen de revenir aux questions précédentes. Les textes à trou se feraient en englobant la vraie réponse (avec des crochets ‘’ []’’) avec d’autre réponses fausses qui sont remplacé par un sélecteur de réponses pour la version ordinateur et qui, dans la version imprimée, remplace juste le mot englobé par une ligne pointillée. Pour les exercices de triages dans plusieurs listes, c’est l’utilisation du Drag&Drop où les seules lignes à écrire seraient une liste de tous les termes à classer avec l’emplacement dans lesquels ils doivent être situé à côté de chaque terme. Avec les QCM, écrire la question ainsi que 3 ou 4 réponses possibles en indiquant lesquelles sont justes dans un formulaire à part. Les questions à développement ou les questions à réponses courtes ne sont qu’une zone de texte qui enregistre la réponse pour la correction du professeur. Pour les questions de type chronologique, c’est aussi l’utilisation de Drag&Drop mais chaque élément est aligné avec les autres. Le but est de faire en sorte que la création du quiz avec les différentes questions soit simple et nécessite quasiment aucunes connaissances poussées en informatique pour permettre à tout le monde de l’utiliser. Je devrais aussi, pour ceux faisant ces quiz sur ordinateur, trouver un moyen d’enregistrer les données pour les corriger et/ou les donner au professeur responsable.

## Difficultés envisagées

Il y a eu beaucoup plus de difficultés que ce que j'aurais pu imaginer - peut-être que c'était de la prétention, qui sait. J’ai commencé la programmation en début du mois d'août et, bien que j'avançais à bon rythme, ma première difficulté était de savoir comment corriger les diverses erreurs. La deuxième était que je n'étais jamais satisfait de mon travail car il me manquait l'objectif principal : pouvoir créer de A à Z un quiz sans aucune connaissance en informatique directement sur la page web où s'affichait le composant.
Je pense que le pire était quand je réalisais que je ne possédais pas de loin assez de connaissances pour réaliser mes tâches aisément. Ou alors, c'était le fait que je devais réviser pour les cours pour maintenir mes moyennes car je n'ai pas le droit à l'erreur.
Enfin, pour tout dire, je suis content des deux composants relativement complets qui fonctionnent, bien sûr, et même si les autres composants que j'avais commencé à développer fonctionnent, il leur manque cette interaction avec l'utilisateur qui veut peut-être ajouter ses propres questions.

## Intérêt de l’outil :

Mes composants ont pour but d'être éducatifs et amusants pour les enseignants, les étudiants ou même simplement les personnes qui souhaitent tester leur culture générale, et les résultats sont montrés à la fin des quiz. Cet outil permet de créer facilement des questionnaires avec divers types de questions, dont un simple QCM et un quiz où l'on trie l'emplacement de divers éléments.
## Aperçu des solutions similaires existantes :

Il existe de nombreuses solutions similaires pour créer des questionnaires en ligne, comme Kahoot, Google Forms et tant d'autres. Cependant, je pense que mon application de quiz se distingue par sa facilité d'utilisation et sa flexibilité pour personnaliser les questionnaires, car le code est implantable partout.

## Technologies utilisées :

Vue.js est un framework JavaScript open source utilisé pour créer des interfaces utilisateur réactives et dynamiques. Il est très facile à apprendre et à utiliser. Quant aux fonctionnalités principales de Vue.js dans mon projet, ce sont les composants réutilisables, le Data Fetching, la gestion des événements, les méthodes et les lifecycle hooks des composants.

## Configuration matérielle requise :

C’est un composant implantable sur n'importe quelle page web et donc ne requiert pas d'appareil spécifique. Il peut être utilisé sur n'importe quel ordinateur qui possède une connexion internet et un navigateur web moderne comme Chrome ou Microsoft Edge.
## Connaissances requises pour utiliser l’outil :

Il n'y a rien à savoir pour utiliser l'outil car il suffit juste de remplir les formulaires qui se présentent aux utilisateurs (administrateurs) et pour répondre au quiz, il suffit d'appuyer sur un bouton pour le lancer.

## Connaissances requises pour comprendre le fonctionnement de l’outil :

Pour comprendre le fonctionnement des composants, il est recommandé, voire nécessaire, de posséder des connaissances de base en HTML, CSS et JavaScript, surtout pour les utilisateurs qui veulent personnaliser l'apparence des questionnaires en codant le style par eux-mêmes. Les fonctionnalités de Vue.js sont assez simples, mais elles peuvent très vite devenir complexes lorsqu'on les utilise dans des applications de plus en plus complexes. Il faut aussi quelques connaissances de base de Vue.js notamment les directives, les computed properties, les event listeners, les méthodes, les composants, les lifecycle hooks, le routage et la communication entre composants. Cependant, avec des connaissances basiques de JavaScript, Vue.js est rapidement appréciable pour la mise en route et pour construire des quiz interactifs et dynamiques.
