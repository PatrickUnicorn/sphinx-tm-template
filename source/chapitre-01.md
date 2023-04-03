# Composant Quiz

Ce composant gère l'affichage et la logique de l'ensemble du quiz, y compris l'affichage des questions, des médias, des réponses possibles, des résultats et des fonctionnalités d'administration. Il est composé, en plus de lui-même, de deux autres composants séparés qui rajoutent des fonctionnalités au composant parent.

## Template

```{code-block}
<template>
  <div>
    <login-form
      v-if="!isAdmin && !isUser"
      @login="handleLogin"
      :isAdmin="isAdmin"
      :isUser="isUser"
    ></login-form>
    <div
      v-if="quizActive && questions.length > 0 && !quizComplete"
      class="quiz"
    >
      <h3 class="quiz__question">Questions:</h3>
      <div v-for="question in questions" :key="question.id">
        <h2>{{ question.title }}</h2>
        <div v-if="question.media.type === 'image'">
          <img
            v-if="question.media.data"
            :src="question.media.data"
            alt="Question Image"
            class="quiz__media quiz__media--image"
            width="560"
          />
        </div>

        <div v-else-if="question.media.type === 'video'"
          class="quiz__media quiz__media--video"
        >
          <iframe
            :src="embedUrl(question.media.data)"
            width="560"
            height="315"
            allowfullscreen
            style="border: 1px solid #e4e4e4; border-radius: 4px"
            frameborder="0"
          ></iframe>
        </div>
        <div v-if="!question.answerSelected" class="guesses-column">
          <label v-for="(guess, index) in question.guesses" :key="index">
            <input
              type="radio"
              :value="guess"
              v-model="question.selectedAnswer"
              :disabled="question.submitted"
            />
            {{ guess }}
          </label>
        </div>
        <div v-else>
          <div
            :class="{
              quiz__answer: true,
              'quiz__answer--selected': question.submitted,
            }"
          >
            You selected: {{ question.selectedAnswer }}
          </div>
        </div>
      </div>
      <button @click="submitQuiz">Submit Quiz</button>
    </div>
    <div v-if="isUser">
      <button @click="createQuiz" v-if="!quizComplete && !quizActive && questions.length > 0">
        Start Quiz
      </button>
    </div>

    <div v-if="isAdmin">
      <button v-if="!quizActive" @click="toggleQuestionManager">
        Question Manager
      </button>
      <button @click="createQuiz" v-if="!quizComplete && !quizActive && questions.length > 0">
        Start Quiz
      </button>

      <div v-if="showForm">
  <form @submit.prevent="addQuestion" class="question-form">
    <label class="question-form__label">
      Question Title:
      <input type="text" v-model="title" required class="question-form__input" />
    </label>
    <label class="question-form__label">
      Guesses (separated by commas):
      <input type="text" v-model="guesses" required class="question-form__input" />
    </label>
    <label class="question-form__label">
      Answer (must be one of the guesses):
      <select class="question-form__input" v-model="answer" required>
        <option v-for="guess in guessList" :value="guess">{{ guess }}</option>
      </select>
    </label>
    <label class="question-form__label">
      Media Type:
      <select class="question-form__input" v-model="selectedMediaType">
        <option value="">None</option>
        <option value="image">Image</option>
        <option value="video">Video</option>
        <option value="video">Geogebra classic</option>
      </select>
    </label>
    <label v-if="selectedMediaType === 'image'" class="question-form__label">
      Media Data (URL):
      <input type="text" v-model="mediaData" required />
    </label>
    <label v-if="selectedMediaType === 'video'" class="question-form__label">
      Media Data (URL):
      <input type="text" v-model="mediaData" required />
    </label>

    <button type="submit" class="question-form__button question-form__button--save">
      Submit
    </button>
    <button
      type="button"
      @click="showForm = false"
      class="question-form__button question-form__button--cancel"
    >
      Cancel
    </button>
  </form>
</div>

      <question-manager
        :isAdmin="isAdmin && !quizActive && !quizComplete"
        :questions="questions"
        :showQuestionManager="showQuestionManager"
        @add-question="showAddQuestionForm"
        @delete-question="deleteQuestion"
        @save-question="saveQuestion($event)"
      ></question-manager>
    </div>
    <div v-if="quizComplete" class="quiz-results">
      <button v-if="isAdmin" @click="resetQuiz" class="quiz-results__reset-btn">
        Reset Quiz
      </button>
      <h3 class="quiz-results__title">Quiz Results:</h3>
      <p class="quiz-results__score">
        You scored {{ score }} out of {{ questions.length }}.
      </p>
      <h4 class="quiz-results__question-title">Questions:</h4>
      <ul class="quiz-results__question-list">
        <li
          v-for="question in questions"
          :key="question.id"
          class="quiz-results__question-item"
        >
          <h2 class="quiz-results__question-heading">{{ question.title }}</h2>
          <ul class="quiz-results__guesses-list">
            <li
              v-for="(guess, index) in question.guesses"
              :key="index"
              class="quiz-results__guesses-item"
            >
              {{ guess }}
            </li>
          </ul>
          <p class="quiz-results__answer">Answer: {{ question.answer }}</p>
          <p class="quiz-results__your-answer">
            Your answer: {{ question.selectedAnswer }}
          </p>
          <p
            v-if="question.answer === question.selectedAnswer"
            class="quiz-results__result-correct">
            Correct!
          </p>
          <p v-else class="quiz-results__result-incorrect">Incorrect</p>
        </li>
      </ul>
    </div>
  </div>
</template>
```

### Structure du template

- `<login-form>`: Composant pour gérer la connexion en tant qu'utilisateur ou administrateur.
- `<div class="quiz">`: Conteneur pour l'affichage des questions du quiz, visible uniquement lorsque le quiz est actif et n'est pas terminé.
  - `<div v-for="question in questions" :key="question.id">`: crée une boucle pour chaque question et crée un conteneur pour l'affichage de la question, des médias associés et des réponses possibles.
    - `<div v-if="question.media.type === 'image'">`ou `<div v-else-if="question.media.type === 'video'"`: Conteneurs pour les médias associés à la question (image ou vidéo).
    - `<div class="guesses-column">`: Conteneur pour les réponses possibles de la question.
- `<div v-if="isUser">`: Conteneur pour les actions de l'utilisateur (commencer le quiz).
- `<div v-if="isAdmin">`: Conteneur pour les actions de l'administrateur (gérer les questions, commencer le quiz).
  - `<button v-if="!quizActive" @click="toggleQuestionManager">`: Bouton pour afficher le gestionnaire de questions.
  - `<button @click="createQuiz" v-if="!quizComplete && !quizActive && questions.length > 0">`: Bouton pour créer un nouveau quiz.
  - `<div v-if="showForm">`: Conteneur pour le formulaire d'ajout de question.
  - `<question-manager>`: Composant pour gérer les questions du quiz (ajouter, modifier, supprimer des questions).
- `<div v-if="quizComplete" class="quiz-results">`: Conteneur pour afficher les résultats du quiz lorsque le quiz est terminé.
  - `<button v-if="isAdmin" @click="resetQuiz">`: Bouton pour réinitialiser le quiz (visible uniquement pour les administrateurs).
  - `<ul class="quiz-results__question-list">`: Liste des questions avec les réponses possibles, la réponse correcte et la réponse sélectionnée par l'utilisateur.

## Script

```html
<script>
import LoginForm from "./LoginForm.vue";
import QuestionManager from "./QuestionManager.vue";

export default {
  components: {
    LoginForm,
    QuestionManager,
  },
  data() {
    return {
      showForm: false,
      quizActive: false,
      quizComplete: false,
      questions: [],
      selectedAnswers: {},
      score: 0,
      title: "",
      guesses: "",
      answer: "",
      isAdmin: false,
      loginError: false,
      editingQuestion: null,
      addingQuestion: false,
      showQuestionManager: false,
      selectedQuestion: null,
      editingQuestionCopy: null,
      mediaData: "",
      selectedMediaType: "",
      isUser: false,
    };
  },

  methods: {
    resetQuiz() {
      this.quizComplete = false;
      this.score = 0;
      this.questions.forEach((question) => {
        question.selectedAnswer = null;
        question.answerSelected = false;
      });
      this.selectedAnswers = {};
    },

    handleLogin(userType) {
      if (userType === "admin") {
        this.isAdmin = true;
      } else if (userType === "user") {
        this.isUser = true;
      }
    },
    addQuestion() {
      const guessesList = this.guesses.split(",").map((guess) => guess.trim());
      this.questions.push({
        id: this.questions.length + 1,
        title: this.title,
        guesses: guessesList,
        answer: this.answer,
        media: {
          type: this.selectedMediaType,
          data: this.mediaData,
        },
      });

      this.clearFormData();
      localStorage.setItem("questions", JSON.stringify(this.questions));
    },

    clearFormData() {
      this.title = "";
      this.guesses = "";
      this.answer = "";
      this.selectedMediaType = "";
      this.mediaData = "";
      this.showForm = false;
    },

    embedUrl(url) {
      let embedUrl;

      if (url.includes("youtube.com") || url.includes("youtu.be")) {
        const videoId = url.split(/(vi\/|v=|\/v\/|youtu\.be\/|\/embed\/)/)[2];
        embedUrl = `https://www.youtube.com/embed/${videoId}`;
      } else if (url.includes("vimeo.com")) {
        const videoId = url.split(/(vimeo\.com\/|video\/)/)[2];
        embedUrl = `https://player.vimeo.com/video/${videoId}`;
      } else if (url.includes("dailymotion.com")) {
        const videoId = url.split(/(dailymotion\.com\/video\/|dai\.ly\/)/)[2];
        embedUrl = `https://www.dailymotion.com/embed/video/${videoId}`;
      } else if (url.includes("geogebra.org")) {
        embedUrl = `${url}?embed&showToolBar=false`;
      } else {
        embedUrl = url;
      }

      return embedUrl;
    },

    createQuiz() {
      this.questions.forEach((question) => {
        if (!question.hasOwnProperty("media")) {
          question.media = {
            type: "",
            data: "",
          };
        } else {
          question.media.type = question.media.type || "";
          question.media.data = question.media.data || "";
        }
        question.selectedAnswer = null;
        question.answerSelected = false;
      });
      this.quizActive = true;
    },

    submitQuiz() {
      let numCorrect = 0;
      this.questions.forEach((question) => {
        if (question.selectedAnswer === question.answer) {
          numCorrect++;
        }
      });
      this.score = numCorrect;
      this.quizComplete = true;
      this.quizActive = false;
    },

    selectAnswer(question, guess) {
      this.$set(this.selectedAnswers, question.id, guess);
    },

    logout() {
      this.isAdmin = false;
      this.isUser = false;
    },

    deleteQuestion(question) {
      const index = this.questions.findIndex((q) => q.id === question.id);
      this.questions.splice(index, 1);
      localStorage.setItem("questions", JSON.stringify(this.questions));
    },
    saveQuestion(payload) {
      const { original, edited } = payload;

      if (this.addingQuestion) {
        this.addQuestion();
      } else if (original !== null) {
        const index = this.questions.findIndex((q) => q.id === original.id);
        this.questions.splice(index, 1, edited);
        localStorage.setItem("questions", JSON.stringify(this.questions));
      }
      this.selectedQuestion = null;
    },

    toggleQuestionManager() {
      this.showQuestionManager = !this.showQuestionManager;
    },
    showAddQuestionForm() {
      this.showForm = true;
      this.addingQuestion = true;
      this.selectedQuestion = null;
    },
  },
  mounted() {
    const questions = JSON.parse(localStorage.getItem("questions"));
    if (questions) {
      this.questions = questions;
    }
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
    guessList() {
      if (!this.guesses) {
        return [];
      }
      return this.guesses.split(",").map((guess) => guess.trim());
    },
    selectedQuestionGuesses() {
      if (this.selectedQuestion) {
        return this.selectedQuestion.guesses.join(", ");
      }
      return "";
    },
    selectedQuestionData() {
      if (this.selectedQuestion) {
        return {
          title: this.selectedQuestion.title,
          guesses: this.selectedQuestion.guesses.join(", "),
          answer: this.selectedQuestion.answer,
          media: {
            type: this.selectedQuestion.media.type,
            data: this.selectedQuestion.media.data,
          },
        };
      }
      return null;
    },
  },
  watch: {
    selectedQuestionGuesses(newVal) {
      if (this.selectedQuestion) {
        this.selectedQuestion.guesses = newVal
          .split(",")
          .map((guess) => guess.trim());
      }
    },
    showQuizQuestions() {
      return this.quizActive && this.questions.length > 0 && !this.quizComplete;
    },
  },
};
</script>
```

### Importations

- LoginForm : composant pour le formulaire de connexion.
- QuestionManager : composant pour gérer les questions du quiz.

### Propriétés de l'objet 'data'

- showForm : 
  - booléen pour afficher ou masquer le formulaire d'ajout de question.
- quizActive : 
  - booléen pour déterminer si le quiz est actif ou non.
- quizComplete : 
  - booléen pour déterminer si le quiz est terminé ou non.
- questions : 
  - tableau pour stocker les questions du quiz.
- selectedAnswers : 
  - objet pour stocker les réponses sélectionnées par l'utilisateur.
- editingQuestion : 
  - objet pour stocker la question en cours de modification.
- addingQuestion : 
  - booléen pour déterminer si une question est en cours d'ajout.
- showQuestionManager : 
  - booléen pour afficher ou masquer le gestionnaire de questions.
- selectedQuestion : 
  - objet pour stocker la question sélectionnée.
- editingQuestionCopy : 
  - objet pour stocker une copie de la question en cours de modification.
- mediaData : 
  - chaîne pour stocker les données de média (URL) de la question en cours de création.
- selectedMediaType : 
  - chaîne pour stocker le type de média de la question en cours de création.

### Méthodes

- resetQuiz : 
  - réinitialise le quiz.
- handleLogin(userType) : 
  - gère la connexion de l'utilisateur en fonction du type d'utilisateur.
- addQuestion : 
  - ajoute une nouvelle question au tableau des questions.
- clearFormData : 
  - réinitialise les données du formulaire.
- embedUrl(url) : 
  - génère une URL intégrée en fonction de l'URL du média.
- createQuiz : 
  - crée un quiz à partir des questions.
- submitQuiz : 
  - soumet le quiz et calcule le score.
- selectAnswer(question, guess) : 
  - sélectionne une réponse pour une question.
- deleteQuestion(question) : 
  - supprime une question du tableau des questions.
- saveQuestion(payload) :
  - enregistre les modifications apportées à une question.
- toggleQuestionManager :
  - bascule l'affichage du gestionnaire de questions.
- showAddQuestionForm : 
  - affiche le formulaire d'ajout de question.

### Cycle de vie

- mounted : récupère les questions stockées localement à l'initialisation du composant.

### Propriétés calculées

- editingQuestionGuesses : obtient et définit les propositions de réponse pour la question en cours de modification.
- guessList : retourne la liste des propositions pour la question en cours de création.
- selectedQuestionGuesses : obtient et définit les propositions de réponse pour la question sélectionnée.
- selectedQuestionData : retourne les données de la question sélectionnée.

### Surveillance

- selectedQuestionGuesses : met à jour les propositions de réponse pour la question sélectionnée.
- showQuizQuestions : retourne un booléen pour afficher les questions du quiz lorsque le quiz est actif, a des questions et n'est pas terminé.

### Explication des méthodes

- resetQuiz()
  - Réinitialise les propriétés quizComplete et score.
  - Réinitialise les propriétés selectedAnswer et answerSelected pour chaque question.
  - Réinitialise l'objet selectedAnswers.
  
- handleLogin(userType)
  - Si userType est "admin", définit isAdmin sur true.
  - Si userType est "user", définit isUser sur true.

- addQuestion()
  - Crée un tableau guessesList en séparant les chaînes de caractères de la propriété guesses.
  - Ajoute une nouvelle question au tableau questions avec les propriétés fournies.
  - Appelle clearFormData() pour réinitialiser le formulaire.
  - Stocke les questions dans le localStorage.
  
- clearFormData()
  - Réinitialise les propriétés title, guesses, answer, selectedMediaType, mediaData et showForm.

- embedUrl(url)
  - Génère une URL intégrée pour YouTube, Vimeo, Dailymotion et Geogebra en fonction de l'URL du média fournie.

- createQuiz()
  - Initialise les propriétés media, selectedAnswer et answerSelected pour chaque question.
  - Définit quizActive sur true
  .
- submitQuiz()
  - Calcule le nombre de réponses correctes.
  - Met à jour le score.
  - Définit quizComplete sur true et quizActive sur false.
  - selectAnswer(question, guess)
  - Met à jour l'objet selectedAnswers avec l'ID de la question et la réponse sélectionnée.

- logout()
  - Définit isAdmin et isUser sur false.

- deleteQuestion(question)
  - Trouve l'index de la question à supprimer dans le tableau questions.
  - Supprime la question à l'index trouvé.
  - Met à jour le localStorage avec les nouvelles questions.

- saveQuestion(payload)
  - Si addingQuestion est true, appelle addQuestion().
  - Sinon, trouve l'index de la question originale dans le tableau des questions, remplace la question par la version modifiée et met à jour le localStorage.
  - Réinitialise selectedQuestion.

- toggleQuestionManager()
  - Bascule la valeur de showQuestionManager.

- showAddQuestionForm()
  - Affiche le formulaire d'ajout de question en définissant showForm et addingQuestion sur true.
  - Réinitialise selectedQuestion.

### Computed properties

- editingQuestionGuesses
  - Getter : Si editingQuestionCopy existe, retourne les éléments du tableau guesses de editingQuestionCopy sous forme de chaîne de caractères séparés par des virgules.
  - Setter : Si editingQuestionCopy existe, met à jour le tableau guesses de editingQuestionCopy avec les éléments de la chaîne de caractères newVal, en les séparant par des virgules.
- guessList()
  - Si la propriété guesses est vide, retourne un tableau vide.
  - Sinon, retourne un tableau contenant les éléments de la chaîne de caractères guesses, en les séparant par des virgules.
- selectedQuestionGuesses()
  - Si selectedQuestion existe, retourne les éléments du tableau guesses de selectedQuestion sous forme de chaîne de caractères séparés par des virgules.
  - Sinon, retourne une chaîne vide.
- selectedQuestionData()
  - Si selectedQuestion existe, retourne un objet contenant les propriétés de la question sélectionnée.
  - Sinon, retourne null.

### Watchers

- selectedQuestionGuesses(newVal)
  - Si selectedQuestion existe, met à jour le tableau guesses de selectedQuestion avec les éléments de la chaîne de caractères newVal, en les séparant par des virgules.
- showQuizQuestions()
  - Retourne un booléen pour afficher les questions du quiz lorsque le quiz est actif, a des questions et n'est pas terminé.
  - Ainsi, le script permet de gérer les fonctionnalités du quiz, y compris la création, la soumission, la réinitialisation, la gestion des questions, l'ajout de questions et la connexion/déconnexion des utilisateurs et administrateurs.
