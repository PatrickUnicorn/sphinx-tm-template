# Composant Drag and Drop

Ce composant Vue.js permet de créer une zone de déplacement de glisser-déposer. Il contient deux zones de dépôt, chacune contenant une liste d'éléments qui peuvent être déplacés entre les zones en utilisant la fonctionnalité de glisser-déposer. Les éléments sont stockés dans une propriété de référence "items" et sont filtrés pour s'afficher dans chaque zone de dépôt en utilisant la fonction "getList".

## Propriétés

- `items`: cette propriété de référence contient la liste des éléments qui peuvent être déplacés entre les zones de dépôt. Chaque élément a un ID unique, un titre et une propriété "list" qui indique à quelle zone de dépôt il appartient.

## Fonctions

- `getList(list)`: cette fonction filtre les éléments en fonction de la propriété "list" pour afficher uniquement les éléments qui appartiennent à la zone de dépôt spécifiée.

- `startDrag(event, items)`: cette fonction est appelée lorsque l'utilisateur commence à déplacer un élément. Elle définit les propriétés de l'événement de déplacement pour indiquer qu'il s'agit d'un déplacement et stocke l'ID de l'élément en cours de déplacement dans l'événement.

- `onDrop(event, list)`: cette fonction est appelée lorsque l'utilisateur dépose un élément dans une zone de dépôt. Elle récupère l'ID de l'élément déposé à partir de l'événement, trouve l'élément correspondant dans la liste d'éléments et met à jour sa propriété "list" pour qu'il appartienne à la nouvelle zone de dépôt.

## Utilisation

Pour utiliser ce script, vous devez l'importer dans votre projet Vue.js et utiliser les propriétés et les fonctions décrites ci-dessus pour gérer l'interaction utilisateur et mettre à jour l'état de l'application.
