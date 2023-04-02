# Composant CustomDragDrop

## Template

Le template de ce composant Vue est composé d'une seule zone de dépôt où les éléments peuvent être déposés et manipulés. Les éléments sont rendus à l'intérieur de cette zone de dépôt avec une boucle `v-for`.

```
<template>
  <div class="drop-zone" @drop="onDrop($event)" @dragenter.prevent @dragover.prevent>
    <div
      v-for="(element, index) in elements"
      :key="index"
      class="drag-el"
      draggable="true"
      @dragstart="startDrag($event, element, index)"
      v-text="element"
    ></div>
  </div>
</template>
```

### Structure du template

- `<div class="drop-zone">`: La balise `<div>` avec la classe `drop-zone` sert de conteneur pour la zone de dépôt des éléments glissables. Les attributs d'événement suivants sont définis pour cette balise:
  - `@drop="onDrop($event)"`: Gère l'événement de dépôt en appelant la méthode `onDrop` et en passant l'événement en paramètre.
  - `@dragenter.prevent`: Empêche l'événement de survol de la souris par défaut lorsqu'un élément est glissé au-dessus de la zone de dépôt.
  - `@dragover.prevent`: Empêche l'événement de survol de la souris par défaut lorsqu'un élément est glissé sur la zone de dépôt.

- `<div v-for="(element, index) in elements" ...>`: La boucle `v-for` génère une `<div>` pour chaque élément dans le tableau `elements`. Chaque élément est rendu avec l'attribut `v-text`. Les attributs suivants sont définis pour cette balise :
  - `:key="index"`: La clé unique pour chaque élément est définie sur l'index du tableau `elements`.
  - `class="drag-el"`: La classe CSS `drag-el` est appliquée à chaque élément.
  - `draggable="true"`: Rend chaque élément glissable.
  - `@dragstart="startDrag($event, element, index)"`: Gère l'événement de début de glissement en appelant la méthode `startDrag` et en passant l'événement, l'élément glissé et son index en paramètres.
  - `v-text="element"`: Affiche le contenu de l'élément.

## Script

Le script définit la logique associée à la zone de dépôt pour les éléments glissables-déposables.

### Props

- `elements` (type: Array, required: true): Un tableau d'éléments à rendre dans la zone de dépôt.

### Méthodes

- `startDrag(event, element, index)`: Initialise le glissement d'un élément. Cette méthode prend en paramètre l'événement de glissement, l'élément glissé et son index dans le tableau `elements`. Dans cette méthode :
  - `event.dataTransfer.dropEffect = 'move';`: Définit l'effet de dépôt comme "move" (déplacer).
  - `event.dataTransfer.effectAllowed = 'move';`: Autorise l'effet de déplacement uniquement.
  - `event.dataTransfer.setData('element', element);`: Stocke l'élément glissé dans l'objet `dataTransfer` de l'événement.
  - `event.dataTransfer.setData('sourceIndex', index);`: Stocke l'index de l'élément glissé dans l'objet `dataTransfer` de l'événement.

- `onDrop(event)`: Gère l'événement de dépôt. Cette méthode prend en paramètre l'événement de dépôt. Dans cette méthode :
  - `const element = event.dataTransfer.getData('element');`: Récupère l'élément glissé depuis l'objet `dataTransfer` de l'événement.
  - `const sourceIndex = parseInt(event.dataTransfer.getData('sourceIndex'), 10);`: Récupère l'index de l'élément glissé depuis l'objet `dataTransfer` de l'événement et le convertit en nombre entier.
  - `this.$emit('drop', { element, sourceIndex });`: Émet un événement personnalisé `drop` avec les données de l'élément glissé et son index. Ceux-ci peuvent être écoutés et traités par un composant parent.

## Styles

```html
<style>
.custom-drag-drop {
  display: flex;
  flex-direction: column;
}

.drag-el {
  background-color: red;
  color: black;
  border-radius: 3px;
  padding: 3px;
  margin-bottom: 5px;
  cursor: move;
}
</style>
```

## Utilisation

Ce composant peut être utilisé pour créer une interface utilisateur où les éléments peuvent être glissés et déposés. Un composant parent peut écouter l'événement personnalisé `drop` pour traiter les données des éléments déplacés et effectuer des actions en conséquence.
