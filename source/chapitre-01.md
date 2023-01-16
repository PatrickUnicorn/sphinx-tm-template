# Quiz Application

Ce script configure une application de quiz en utilisant Vue.js. L'application a une liste de questions, chacune avec plusieurs options et une réponse correcte. L'utilisateur peut sélectionner une option pour chaque question, et l'application suivra si l'option sélectionnée par l'utilisateur est correcte.

## Gestion de l'état

L'application utilise le système de réactivité intégré de Vue pour gérer l'état de l'application. Les variables d'état suivantes sont utilisées:

- `questions`: un tableau d'objets représentant les questions dans le quiz. Chaque objet de question a les propriétés suivantes:
  - `question`: une chaîne représentant le texte de la question.
  - `answer`: un entier représentant l'index de la réponse correcte dans le tableau `options`.
  - `options`: un tableau de chaînes représentant les options pour la question.
  - `selected`: un entier représentant l'index de l'option sélectionnée par l'utilisateur, ou `null` si l'utilisateur n'a pas encore sélectionné d'option.
- `quizCompleted`: un booléen indiquant si le quiz a été terminé par l'utilisateur.
- `currentQuestion`: un entier représentant l'index de la question actuelle dans le tableau `questions`.
- `timer`: un entier représentant le nombre de secondes restantes pour le quiz.

Les propriétés calculées suivantes sont utilisées:
- `score`: une propriété calculée qui retourne le nombre de questions que l'utilisateur a répondu correctement.
- `getCurrentQuestion`: une propriété calculée qui retourne l'objet de question actuel, avec une propriété supplémentaire `index` représentant l'index de la question dans le tableau `questions`.

## Interaction utilisateur

Les fonctions suivantes sont utilisées pour gérer l'interaction utilisateur:
- `SetAnswer(e)`: Cette fonction est utilisée pour définir la réponse de l'utilisateur pour la question actuelle.
- `startTimer()`: Cette fonction est utilisée pour démarrer le minuteur dès que la première question est chargée.
- `NextQuestion()`: Cette fonction est utilisée pour passer à la question suivante. Si la question actuelle est la dernière question, la variable `quizCompleted` est définie sur `true`.
- `resetQuiz()`: Cette fonction est utilisée pour réinitialiser le quiz à son état initial.
- `saveProgress()`:Cette fonction est utilisée pour enregistrer l'état actuel du quiz dans le stockage local.
- `loadProgress()`: Cette fonction est utilisée pour charger l'état sauvegardé du quiz depuis le stockage local.

## Mise en page

Le script utilise CSS pour mettre en forme le quiz. Les classes CSS suivantes sont utilisées:
- `quiz-info`: pour mettre en forme le conteneur pour le texte de la question
- `options`: pour mettre en forme le conteneur pour les options
- `option`: pour mettre en forme une option individuelle
- `correct`: pour indiquer une réponse correcte
- `wrong`: pour indiquer une réponse incorrecte
- `disabled`: pour indiquer une option qui n'a pas été sélectionnée par l'utilisateur.

## Utilisation

Pour utiliser ce script, vous devez l'importer dans votre projet Vue.js et appeler les fonctions nécessaires pour gérer l'interaction utilisateur et mettre à jour l'état de l'application.

## Conclusion

Ce script configure une application de quiz de base en utilisant Vue.js, qui permet aux utilisateurs de répondre à des questions et de suivre leur progression et leur score. Il a également un minuteur, et la progression de l'utilisateur peut être sauvegardée et chargée à partir du stockage local.