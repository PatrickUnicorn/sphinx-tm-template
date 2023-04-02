# Composant QuestionManager

Le composant est divisé en trois parties principales :

## 1. Template

Cette partie contient le code HTML qui définit la structure du gestionnaire de questions et ses éléments interactifs.

```{code-block}
<template>
  <div v-if="isAdmin && showQuestionManager">
    <h2>Question Manager</h2>
    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Guesses</th>
          <th>Answer</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="question in questions" :key="question.id">
          <td>{{ question.title }}</td>
          <td>{{ question.guesses.join(", ") }}</td>
          <td>{{ question.answer }}</td>
          <td>
            <button
              @click="
                selectedQuestion = question;
                editingQuestionCopy = JSON.parse(JSON.stringify(question));
              "
            >
              Edit
            </button>
            <button @click="deleteQuestion(question)">
              Delete {{ question.title }}
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <button @click="addQuestion" v-if="!showForm">Add Question</button>

    <div v-if="selectedQuestion" class="edit-form">
      <h3 class="edit-form__title">Edit Question</h3>
      <form class="edit-form__form">
        <label class="edit-form__label">
          Question Title:
          <input
            type="text"
            v-model="editingQuestionCopy.title"
            required
            class="edit-form__input"
          />
        </label>
        <label class="edit-form__label">
          Guesses (separated by commas):
          <input
            type="text"
            v-model="editingQuestionGuesses"
            required
            class="edit-form__input"
          />
        </label>
        <label class="edit-form__label">
          Answer (must be one of the guesses):
          <select
            v-model="editingQuestionCopy.answer"
            required
            class="edit-form__select"
          >
            <option v-for="guess in editingQuestionCopy.guesses" :value="guess">
              {{ guess }}
            </option>
          </select>
        </label>
        <label class="edit-form__label">
          Media Type:
          <select
            v-model="editingQuestionCopy.media.type"
            class="edit-form__select"
          >
            <option value="">None</option>
            <option value="image">Image</option>
            <option value="video">Geogebra</option>
            <option value="video">Video</option>
          </select>
        </label>
        <label
          class="edit-form__label"
          v-if="editingQuestionCopy.media.type === 'video'"
        >
          Media Data (URL):
          <input
            type="text"
            v-model="editingQuestionCopy.media.data"
            required
            class="edit-form__input"
          />
        </label>
        <label
          class="edit-form__label"
          v-if="editingQuestionCopy.media.type === 'image'"
        >
          Media Data (URL):
          <input
            type="text"
            v-model="editingQuestionCopy.media.data"
            required
            class="edit-form__input"
          />
        </label>

        <button
          type="button"
          @click="saveQuestion"
          class="edit-form__button edit-form__button--save"
        >
          Save
        </button>

        <button
          type="button"
          @click="selectedQuestion = null"
          class="edit-form__button edit-form__button--cancel"
        >
          Cancel
        </button>
      </form>
    </div>
  </div>
</template>
```

### Éléments clés du gestionnaire de questions

- Tableau affichant la liste des questions avec leur titre, leurs choix, leur réponse et des boutons pour modifier et supprimer.
- Les formulaires pour ajouter ou modifier une question sont en réalité composés d'un seul formulaire qui change de comportement selon qu'une question est sélectionnée pour modification ou non. Les éléments clés du formulaire sont les suivants :

  - Question Title: Un champ de texte permettant de saisir le titre de la question.
  - Guesses: Un champ de texte permettant de saisir les choix de réponse, séparés par des virgules.
  - Answer: Un menu déroulant contenant les choix de réponse. L'utilisateur doit sélectionner la réponse correcte parmi ces choix.
  - Media Type: Un menu déroulant permettant de choisir le type de média associé à la question : Aucun, Image, Geogebra ou Vidéo.
  - Media Data: Un champ de texte permettant de saisir l'URL du média, visible uniquement si un type de média est sélectionné.
  - Boutons Save et Cancel: Le bouton "Save" enregistre les modifications apportées à la question ou ajoute une nouvelle question si aucune n'est sélectionnée pour modification. Le bouton "Cancel" annule l'édition en cours et réinitialise la variable `selectedQuestion`.

#### Différence entre les deux formulaires

En réalité, il n'y a qu'un seul formulaire qui change de comportement selon qu'une question est sélectionnée pour modification ou non. La différence réside dans la manière dont le formulaire est utilisé et comment les données sont traitées en fonction du contexte :

##### Formulaire d'ajout de question

- Lorsque l'utilisateur clique sur le bouton "Add Question", la méthode `addQuestion()` est appelée et le formulaire est initialisé avec des champs vides.
- La méthode `addQuestion()` émet simplement un événement "add-question" sans passer de paramètre, signalant au composant parent(dans lequel il est importé) qu'une nouvelle question doit être ajoutée.

##### Formulaire de modification de question

- Lorsque l'utilisateur clique sur le bouton "Edit" d'une des questions, le formulaire est prérempli avec les données de la question sélectionnée, et la méthode `saveQuestion()` est appelée, signalant un évènement save-question au composant parent(dans lequel il est importé) qu'il doit utiliser la méthode `saveQuestion`.
- Quande le bouton "Cancel" est appuyé il déselectionne la question (selectedQuestion = null) et le formulaire, nécessitant une question pour ouvrir, se ferme automatiquement.
  
```html
<div v-if="selectedQuestion" class="edit-form">
    ...
</div>
```

## 2. Script

Cette partie contient le code JavaScript qui gère le comportement du composant.

```html
<script>
export default {
  props: {
    isAdmin: {
      type: Boolean,
      default: false,
    },
    questions: {
      type: Array,
      default: () => [],
    },
    showQuestionManager: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      showForm: false,
      selectedQuestion: null,
      editingQuestionCopy: null,
    };
  },
  computed: {
    editingQuestionGuesses: {
      get() {
        if (this.editingQuestionCopy) {
          return this.editingQuestionCopy.guesses.join(", ");
        }
        return "";
      },
      set(newVal) {
        if (this.editingQuestionCopy) {
          this.editingQuestionCopy.guesses = newVal
            .split(",")
            .map((guess) => guess.trim());
        }
      },
    },
  },
  methods: {
    deleteQuestion(question) {
      this.$emit("delete-question", question);
    },
    saveQuestion() {
  this.$emit("save-question", {
    original: this.selectedQuestion,
    edited: this.editingQuestionCopy,
  });
  this.selectedQuestion = null;
},

    addQuestion() {
      this.$emit("add-question");
    },
  },
};
</script>
```

### Propriétés et méthodes importantes

- props: Un tableau contenant les propriétés passées au composant. Ici, 'isAdmin', 'questions' et 'showQuestionManager' sont utilisées pour déterminer si l'utilisateur est un administrateur, pour afficher les questions et pour contrôler la visibilité du composant.

- data(): Une fonction qui retourne un objet contenant les variables de données du composant. Les variables sont "showForm", "selectedQuestion" et "editingQuestionCopy".

- computed: Un objet contenant les propriétés calculées du composant. La propriété calculée est "editingQuestionGuesses".

- methods: Un objet contenant les méthodes qui gèrent le comportement du composant. Les méthodes sont "deleteQuestion", "saveQuestion" et "addQuestion".

#### i. deleteQuestion(question)

Cette méthode est appelée lorsque l'utilisateur clique sur le bouton "Delete". Elle émet un événement "delete-question" au composant parent avec la question à supprimer en paramètre.

#### ii. saveQuestion()

Cette méthode est appelée lorsque l'utilisateur clique sur le bouton "Save". Elle émet un événement "save-question" avec l'objet original et l'objet édité en paramètres, puis réinitialise la variable selectedQuestion.

#### iii. addQuestion()

Cette méthode est appelée lorsque l'utilisateur clique sur le bouton "Add Question". Elle émet simplement un événement "add-question".

## 3. Styles (non présents dans le code fourni)

Cette partie contiendrait les styles CSS qui définissent l'apparence du composant.
