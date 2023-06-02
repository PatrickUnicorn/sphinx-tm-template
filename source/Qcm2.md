## Deuxième Qcm à voir le jour 

- Ce composant est un peu plus flexible, même si l'on ne peut pas créer ses propres questions sans les modifier directement dans le code. Il permet toutefois de revenir à la question précédente.

```{code-block}
<template>
  <div class="qcm2">
    <h1 class="titre-qcm">Quiz</h1>
    <span class="question">{{ currentQuestion.question }}</span>
    <ul class="answers-list">
      <li
        class="answers"
        v-for="(answer, index) in currentQuestion.answers"
        :key="index"
      >
        <label class="checkbox">
          <input
            type="checkbox"
            v-model="selected"
            :value="answer"
            :disabled="completed"
            @change="selectAnswer"
          />
          {{ answer }}
          <span class="checkmark"></span>
        </label>
      </li>
    </ul>
    <button class="btn" v-if="!completed" @click="submit">Submit</button>
    <button
      class="btn"
      v-if="currentQuestionNumber > 0 && !completed"
      @click="previousQuestion"
    >
      Previous
    </button>
    <p v-if="completed">
      You got {{ correctAnswers }} out of {{ questions.length }} questions
      correct.
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      completed: false,
      questions: [
        {
          question: "Which of the following are fruits?",
          answers: ["Apple", "Carrot", "Banana", "Tomato"],
          correct: ["Apple", "Banana"],
        },
        {
          question: "Which of the following are vegetables?",
          answers: ["Pepper", "Lettuce", "Onion", "Strawberry"],
          correct: ["Pepper", "Lettuce", "Onion"],
        },
      ],
      currentQuestionNumber: 0,
      currentQuestion: null,
      selected: [],
      correctAnswers: 0,
    };
  },
  computed: {
    isLastQuestion() {
      return this.currentQuestionNumber === this.questions.length - 1;
    },
  },
  created() {
    this.questions.forEach((question) => {
      question.answers = this.shuffleAnswers(question.answers);
    });
    this.currentQuestion = this.questions[this.currentQuestionNumber];
  },
  methods: {
    previousQuestion() {
      if (this.currentQuestionNumber > 0) {
        this.currentQuestionNumber--;
        this.currentQuestion = this.questions[this.currentQuestionNumber];
      }
    },
    selectAnswer() {
      this.selected = this.selected.filter(
        (answer) => answer !== this.currentAnswer
      );
      this.selected.push(this.currentAnswer);
    },
    submit() {
      const correct = this.currentQuestion.correct;
      const selected = this.selected;
      if (correct.every((answer) => selected.includes(answer))) {
        this.correctAnswers++;
      }
      if (this.isLastQuestion) {
        this.completed = true;
      } else {
        this.nextQuestion();
      }
    },
    nextQuestion() {
      this.selected = [];
      this.currentQuestionNumber++;
      this.currentQuestion = this.questions[this.currentQuestionNumber];
    },

    shuffleAnswers(answers) {
      return answers.sort(() => Math.random() - 0.5);
    },
  },
};
</script>
```