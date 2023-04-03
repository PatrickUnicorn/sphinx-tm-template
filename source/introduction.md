# Introduction:

Ce projet est un outil de création et de gestion de quiz en ligne, développé avec Vue.js. Il permet aux utilisateurs de créer leurs propres quiz personnalisés, de les essayer en local. j'ai utilisé Vue.js et le HTML/CSS/JavaScript pour créer une interface réactive dont l'on peut modifié. Le projet est hébergé sur GitHub(en Privé).

## Description initiale

Le principal but de mon projet est de créer un composants web capable de générer automatiquement, par exemple, des quiz (voire des examens) avec des exercices de type QCM mais aussi des textes à trou, des question-réponse, des exercices de triages entre plusieurs colonnes, des réponses à relier et des frises chronologiques. Bien sur ces exercices pourront être imprimer ou alors être directement effectué sur ordinateur avec une correction disponible pour les professeurs ou une correction automatique disponible pour les élèves en cas de simple questionnaire formatif. Les examens effectués sur ordinateur serait doté d’un chronomètre et d’un moyen de revenir aux questions précédentes. Les textes à trou se feraient en englobant la vraie réponse (avec des crochets ‘’[]’’) avec d’autre réponses fausses qui sont remplacé par un sélecteur de réponses pour la version ordinateur et qui, dans la version imprimée, remplace juste le mot englobé par une ligne pointillée. Pour les exercices de triages dans plusieurs listes, c’est l’utilisation du Drag&Drop où les seules lignes à écrire seraient une liste de tous les termes à classer avec l’emplacement dans lesquels ils doivent être situé à côté de chaque terme. Avec les QCM, écrire la question ainsi que 3 ou 4 réponses possibles en indiquant lesquelles sont justes dans un formulaire à part. Les questions à développement ou les questions à réponses courtes ne sont qu’une zone de texte qui enregistre la réponse pour la correction du professeur. Pour les questions de type chronologique, c’est aussi l’utilisation de Drag&Drop mais chaque élément est aligné avec les autres. Le but est de faire en sorte que la création du quiz avec les différentes questions soit simple et nécessite quasiment aucunes connaissances poussées en informatique pour permettre à tout le monde de l’utiliser. Je devrais aussi, pour ceux faisant ces quiz sur ordinateur, trouver un moyen d’enregistrer les données pour les corriger et/ou les donner au professeur responsable.

## Difficultés envisagées

Il y a eu beaucoup plus de difficultés que ce que j'aurais pu m'imaginer peut-être que c'était de la prétention qui sait. j'ai commencé la programmation en début de mois août et bien que j'avançait à bon rythme  ma première difficulté était de savoir comment corrigeait-t-on les divers erreur. le deuxième était que je n'était jamais satisfait de mon travail car il me manquait le principal des mes objectifs pouvoir créer de A à Z un quiz sans aucune connaissance de l'informatique directement sur la page web où s'affichait le composant.
je pense que le pire était quand je réalisait que je ne possédait de loin pas assez de connaissance pour réaliser mes tâches aisément. Ou alors c'était le fait que je me devais de réviser pour les cours pour maintenir mes moyennes car je n'ai pas le droit à l'erreur. 
Enfin, pour tout dire, je suis content des deux composants relativement complet et qui fonctionne, bien sûr, et même si les autres composants que j'avais commencé fonctionnent, il leur manque cette intéraction avec l'utilisateur qui veut peut-être ajouter ces propres questions.

## Intérêt de l'outil:

Mes composants sont des outils à but éducatif et amusant pour les enseignants, les étudiants ou même les personnes qui souhaitent tester leurs connaissances dans un domaine en particulier. cet outil permet de créer facilement des questionnaires avec une variété de types de questions dont un simple Qcm et un quiz ou l'on trie l'emplacement de divers éléments. Les résultats sont montrés à la fin des quiz.

## Aperçu des solutions similaires existantes:

Il existe de nombreuses solutions similaires pour créer des questionnaires en ligne, comme Kahoot, Google Forms et tant d'autres. Cependant, je pense que mon application de quiz se distingue par sa facilité d'utilisation et sa flexibilité pour personnaliser les questionnaires car le code est implémentable partout.

## Technologies utilisées:

Vue.js est un framework JavaScript open source utilisé pour créer des interfaces utilisateur réactives et dynamiques. Il est très facile de l'apprendre et de l'utiliser, quant aux fonctionnalités principales de Vue.js, dans mon projet, ce sont les composants réutilisables, le Data Fetching, la gestion des événements, les méthodes et les lifecycle hooks des composants.

## Configuration matérielle requise:

c'est un composant implementable sur n'importe quelle page web et donc ne requiert pas d'appareil spécifique. il peut être utilisé sur n'importe quel ordinateur qui possède une connexion internet et un navigateur web moderne comme Chrome ou Microsoft Edge.

## Connaissances requises pour utiliser l'outil:

Il n'y a rien à savoir pour utiliser l'outil car il suffit juste de remplir les formulaires qui se présente au utilisateurs (administrateurs) et pour répondre au quiz il suffit d'appuyer sur un bouton pour le lancer

## Connaissances requises pour comprendre le fonctionnement de l'outil:

Pour comprendre le fonctionnement des composants, il est recommandé, voire nécessaire de posséder des connaissances de base en HTML, CSS et JavaScript, surtout pour les utilisateurs qui veulent personnaliser l'apparence des questionnaires en codant le style par eux-même. Les spécialités de Vue.js sont assez simples, mais elles peuvent très vite devenir complexes lorsqu'on les utilise dans des applications de plus en plus complexes. Il faut aussi quelques connaissances de base de Vue.js notamment les directives, les computed properties, les event listeners, les méthodes, les composants, les lifecycle hooks, le routage et la communication entre composants. Cependant, avec des connaissances basiques de JavaScript, Vue.js est rapidement apprenable comme la mise en route et de l'utiliser pour construire des quiz interactifs et dynamiques.