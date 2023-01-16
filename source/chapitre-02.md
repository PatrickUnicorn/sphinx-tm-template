# Composant Qcm type 2

Ce script configure une application de quiz en utilisant Vue.js. L'application a une liste de questions, chacune avec plusieurs options de réponse et une ou plusieurs réponses correctes. L'utilisateur peut sélectionner une ou plusieurs options pour chaque question, et l'application suivra si les options sélectionnées par l'utilisateur sont correctes.

## Gestion de l'état

L'application utilise le système de réactivité intégré de Vue pour gérer l'état de l'application. Les variables d'état suivantes sont utilisées:

- `questions`: un tableau d'objets représentant les questions dans le quiz. Chaque objet de question a les propriétés suivantes:
  - `question`: une chaîne représentant le texte de la question.
  - `answers`: un tableau de chaînes représentant les options de réponse pour la question.
  - `correct`: un tableau de chaînes représentant les réponses correctes pour la question.
- `completed`: un booléen indiquant si le quiz a été terminé par l'utilisateur.
- `currentQuestionNumber`: un entier représentant l'index de la question actuelle dans le tableau `questions`.
- `currentQuestion`: un objet représentant la question actuelle.
- `selected`: un tableau de chaînes représentant les options de réponse sélectionnées par l'utilisateur.
- `correctAnswers`: un entier représentant le nombre de réponses correctes données par l'utilisateur.

Les propriétés calculées suivantes sont utilisées:
- `isLastQuestion`: une propriété calculée qui retourne vrai si la question actuelle est la dernière question dans le tableau `questions`.

## Interaction utilisateur

Les fonctions suivantes sont utilisées pour gérer l'interaction utilisateur:
- `selectAnswer()`: Cette fonction est utilisée pour définir les réponses sélectionnées par l'utilisateur pour la question actuelle.
- `submit()`: Cette fonction est utilisée pour soumettre les réponses de l'utilisateur pour la question actuelle. Si c'est la dernière question, la variable `completed` est définie sur `true`. Sinon, elle passe à la question suivante.
- `nextQuestion()`: Cette fonction est utilisée pour passer à la question suivante.
- `previousQuestion()`: Cette fonction est utilisée pour retourner à la question précédente.
- shuffleAnswers(answers)`: Cette fonction est utilisée pour mélanger les options de réponse pour chaque question.

## Mise en page

Le script utilise CSS pour mettre en forme le quiz. Les classes CSS suivantes sont utilisées:
- `titre-qcm`: pour mettre en forme le titre du quiz
- `question`: pour mettre en forme le texte de la question
- `answers-list`: pour mettre en forme le conteneur pour les options de réponse
- `answers`: pour mettre en forme une option de réponse individuelle
- `checkbox`: pour mettre en forme la case à cocher pour chaque option de réponse
- `checkmark`: pour mettre en forme la coche pour une option de réponse sélectionnée
- `btn`: pour mettre en forme les boutons de soumission et de question précédente

## Utilisation

Pour utiliser ce script, vous devez l'importer dans votre projet Vue.js et utiliser les propriétés et les fonctions décrites ci-dessus pour gérer l'interaction utilisateur et mettre à jour l'état de l'application.

## Conclusion

Ce script configure une application de quiz de base en utilisant Vue.js, qui permet aux utilisateurs de répondre à des questions à choix multiple et de suivre leur score. Il permet également de naviguer entre les questions précédentes et suivantes.

