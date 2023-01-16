# Composant de Texte à trou

Ce composant Vue.js permet de créer un texte dont l'on doit remplir les blancs. Il contient un texte avec des espaces vides remplaçables par l'utilisateur, et une liste de champs de saisie pour chaque espace vide. Lorsque l'utilisateur soumet le quiz en cliquant sur le bouton "Submit", le texte est mis à jour pour remplacer les espaces vides par les réponses de l'utilisateur.

## Propriétés

`text`: cette propriété contient le texte du quiz avec des espaces vides marqués par des chaînes de caractères comme ___1___, ___2___, etc.
`blanks`: cette propriété contient une liste d'objets qui décrivent les espaces vides dans le texte. Chaque objet contient une propriété "label" pour l'étiquette du champ de saisie correspondant, et une propriété "answer" pour stocker la réponse de l'utilisateur.

## Computed properties

`textWithBlanks()`: cette propriété calculée remplace les espaces vides dans le texte par des balises span pour les mettre en surbrillance et les différencier des autres parties
