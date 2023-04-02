# Composant DragDropQuiz

Ce composant permet de créer un quiz de glisser-déposer avec des colonnes et des éléments à réorganiser.

## Template

```
<template>
  <div class="drag-drop-quiz">
    <h1>{{ question }}</h1>

    <div v-for="(title, index) in columnTitles" :key="index" class="column">
      <h2>{{ title }}</h2>
      <CustomDragDrop
        class="column-content"
        :elements="columns[index]"
        @drop="onDrop(index, $event)"
      />
    </div>
  </div>
</template>
```

### Structure du template

- `<h1>{{ question }}</h1>` : Affiche le titre de la question.
- `<div v-for="(title, index) in columnTitles" :key="index" class="column">` : Crée une colonne pour chaque titre de colonne, avec une clé unique.
  - `<CustomDragDrop>` : Utilise le composant CustomDragDrop pour gérer les éléments glissables.
    - `:elements="columns[index]"` : Passe les éléments de la colonne correspondante au composant CustomDragDrop.
    - `@drop="onDrop(index, $event)"` : Gère l'événement "drop" avec la méthode "onDrop" et passe l'index de la colonne cible et l'événement.

## Script

```html
<script>
import CustomDragDrop from './CustomDragDrop.vue';

export default {
  components: {
    CustomDragDrop,
  },
  props: {
    question: String,
    columnTitles: Array,
    initialElements: Array,
  },
  data() {
    return {
      columns: [],
    };
  },
  created() {
    this.initializeColumns();
  },
  methods: {
    initializeColumns() {
      this.columns = this.columnTitles.map(() => []);
      const elements = this.initialElements.slice();

      while (elements.length) {
        const index = Math.floor(Math.random() * this.columns.length);
        this.columns[index].push(elements.pop());
      }
    },
    onDrop(targetColumnIndex, event) {
      const { element, sourceIndex } = event;
      const sourceColumnIndex = this.columns.findIndex((column) =>
        column.includes(element)
      );

      if (sourceColumnIndex !== -1) {
        this.columns[sourceColumnIndex].splice(sourceIndex, 1);
        this.columns[targetColumnIndex].push(element);
      }
    },
  },
};
</script>
```

### Importation du composant

- `import CustomDragDrop from './CustomDragDrop.vue';` : Importe le composant CustomDragDrop.

### Composant

- `components: { CustomDragDrop }`: Enregistre le composant CustomDragDrop pour une utilisation dans ce composant.

### Props

- `question`: Chaîne de caractères représentant la question du quiz.
- `columnTitles`: Tableau contenant les titres des colonnes.
- `initialElements`: Tableau contenant les éléments initiaux à placer dans les colonnes.

### Données

- `columns`: Tableau vide qui contiendra les éléments de chaque colonne après l'initialisation.

### Hooks

- `created()`: Appelle la méthode `initializeColumns()` pour initialiser les colonnes avec les éléments.

### Méthodes

- `initializeColumns()`: Initialise les colonnes avec les éléments.
  - Crée un tableau de colonnes vide pour chaque titre de colonne.
  - Mélange les éléments initiaux et les répartit de manière aléatoire dans les colonnes.
- `onDrop(targetColumnIndex, event)`: Gère l'événement de dépôt en mettant à jour les colonnes.
  - `const { element, sourceIndex } = event;`: Extrait l'élément et l'index source de l'événement.
  - `const sourceColumnIndex = this.columns.findIndex((column) => column.includes(element));`: Trouve l'index de la colonne source en recherchant l'élément.
  - Si `sourceColumnIndex` est différent de -1, supprime l'élément de la colonne source et l'ajoute à la colonne cible.

## Styles

Les styles CSS pour ce composant ne sont pas inclus dans le code fourni. Vous pouvez les ajouter en fonction de vos besoins pour personnaliser l'apparence des colonnes et des éléments glissables.
