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
<style>
.checkbox {
  display: inline-block;
  position: relative;
  padding-left: 35px;
  margin-right: 10px;
  cursor: pointer;
  font-size: 22px;
}

.checkbox input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create a custom checkmark */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  width: 25px;
  height: 25px;
  background-color: #ddd;
  border: 2px solid #ccc;
}

/* On mouse-over, add a hover effect */
.checkbox:hover input ~ .checkmark {
  background-color: #bbb;
}

/* When the checkbox is checked, add a custom symbol */
.checkbox input:checked ~ .checkmark {
  background-color: #2196f3;
  border: none;
}

/* Create the checkmark symbol */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the checkmark symbol when the checkbox is checked */
.checkbox input:checked ~ .checkmark:after {
  display: block;
}

/* Style the checkmark symbol */
.checkbox .checkmark:after {
  left: 8px;
  top: 3px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
/* center everything */

.quiz-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.btn {
  padding: 0.5rem 1rem;
  margin: 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
}

.btn.previous {
  background-color: #f44336;
}

.titre-qcm {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 1rem;
}

/* add a background color and padding to the question container */
.question {
  background-color: #e6e6e6;
  padding: 1rem;
  border-radius: 0.5rem;
  text-align: center;
  margin-bottom: 1rem;
}

/* style the list of answers */
.answers-list {
  list-style-type: none;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 60%;
}

/* style the individual answers */
.answers {
  display: flex;
  align-items: center;
  padding: 0.5rem;
  margin: 0.5rem;
  border-radius: 0.5rem;
  background-color: #f2f2f2;
  text-align: center;
}

/* style the checkboxes */
input[type="checkbox"] {
  margin-right: 0.5rem;
}

/* style the results */
.question.result {
  margin-top: 1rem;
  text-align: center;
}
.qcm2 {
  display: flex;
  flex-direction: column;
  align-items: center; /* horizontally center all child elements */
  justify-content: center; /* vertically center all child elements */
  background-color: white;
  align-self: center;
  border-radius: 15px;
  padding: 20px 0px;
}
</style>
```