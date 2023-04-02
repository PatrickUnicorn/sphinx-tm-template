# Composant QuizForm

Ce composant permet de créer un formulaire pour ajouter ou modifier un quiz de glisser-déposer.

## Template

```{code-block}
<template>
  <div>
    <form class="form-wrapper" @submit.prevent="submitQuizForm">
      <div class="form-group">
        <label for="question">Question:</label>
        <input id="question" v-model="form.question" type="text" required />
      </div>

      <div
        class="form-group"
        v-for="(title, index) in form.columnTitles"
        :key="index"
      >
        <label :for="`column-title-${index}`"
          >Column Title {{ index + 1 }}:</label
        >
        <input
          :id="`column-title-${index}`"
          v-model="form.columnTitles[index]"
          type="text"
          required
        />
      </div>

      <button class="form-group" type="button" @click="addColumn">
        Add Column
      </button>

      <div
        class="form-group"
        v-for="(element, index) in form.initialElements"
        :key="index"
      >
        <label :for="`element-${index}`">Element {{ index + 1 }}:</label>
        <input
          :id="`element-${index}`"
          v-model="form.initialElements[index]"
          type="text"
          required
        />
      </div>

      <button class="form-group" type="button" @click="addElement">
        Add Element
      </button>

      <button class="form-group" type="submit">Create Quiz</button>
    </form>
  </div>
</template>
```

### Structure du template

- `<form class="form-wrapper" @submit.prevent="submitQuizForm">` : Le formulaire avec la classe "form-wrapper" et la méthode "submitQuizForm" pour gérer la soumission du formulaire.
  - `<div class="form-group">` : Conteneur pour chaque champ du formulaire avec la classe "form-group".
    - `Question:` : Label pour le champ de la question.
    - `<input id="question" v-model="form.question" type="text" required />`: Champ pour saisir la question du quiz.
  - `<div class="form-group" v-for="(title, index) in form.columnTitles" :key="index">` : Boucle sur les titres de colonnes et crée un conteneur pour chaque champ avec une clé unique.
    - `Column Title {{ index + 1 }}:` : Label pour le champ du titre de la colonne.
    - `<input :id="column-title-${index}" v-model="form.columnTitles[index]" type="text" required />`: Champ pour saisir le titre de chaque colonne.
  - `<button class="form-group" type="button" @click="addColumn">`: Bouton pour ajouter une nouvelle colonne.
  - `<div class="form-group" v-for="(element, index) in form.initialElements" :key="index">` : Boucle sur les éléments initiaux et crée un conteneur pour chaque champ avec une clé unique.
    - `Element {{ index + 1 }}:` : Label pour le champ de l'élément.
    - `<input :id="element-${index}" v-model="form.initialElements[index]" type="text" required />`: Champ pour saisir chaque élément.
  - `<button class="form-group" type="button" @click="addElement">`: Bouton pour ajouter un nouvel élément.
  - `<button class="form-group" type="submit">`: Bouton pour soumettre le formulaire.

## Script

```html
<script>
export default {
  data() {
    return {
      form: {
        question: "",
        columnTitles: ["", ""],
        initialElements: ["", "", "", ""],
      },
    };
  },
  methods: {
    addColumn() {
      this.form.columnTitles.push("");
    },
    addElement() {
      this.form.initialElements.push("");
    },
    submitQuizForm() {
      const form = {
        question: this.form.question,
        columnTitles: this.form.columnTitles,
        initialElements: this.form.initialElements,
      };
      this.$emit("create-quiz", form);
      this.resetForm();
    },

    resetForm() {
      this.form.question = "";
      this.form.columnTitles = ["", ""];
      this.form.initialElements = ["", "", "", ""];
    },
  },
};
</script>
```

### Données

- `form`: Objet représentant le formulaire avec les propriétés :
  - `question`: Chaîne de caractères pour la question du quiz.
  - `columnTitles`: Tableau pour les titres des colonnes.
  - `initialElements`: Tableau pour les éléments initiaux.

### Méthodes

- `addColumn()`: Ajoute une nouvelle colonne vide au tableau des titres de colonnes.
- `addElement()`: Ajoute un nouvel élément vide au tableau des éléments initiaux.
- `submitQuizForm()`: Gère la soumission du formulaire en émettant un événement "create-quiz" avec les données du formulaire, puis réinitialise le formulaire.
- `resetForm()`: Réinitialise le formulaire en remettant les champs à leur état initial.

## Styles

Les styles CSS pour ce composant ne sont pas inclus dans le code fourni. Vous pouvez les ajouter en fonction de vos besoins pour personnaliser l'apparence du formulaire et des champs.
