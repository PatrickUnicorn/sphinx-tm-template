## Premier Qcm 

— C'était mon premier composant lié aux types de questions et, bien qu'il fonctionnait, il était trop restrictif, étant donné qu'il s'agissait d'un composant fixe sans possibilité de modifier les questions depuis la page web.

```{code-block}
<script setup>
import { ref, computed } from "vue";

const questions = ref([
  {
    question: "Dans quel pays se trouve-t'on ?",
    answer: 0,
    options: ["Suisse", "France", "Allemagne"],
    selected: null,
  },
  {
    question: "Quel pays comporte le plus d'habitants",
    answer: 0,
    options: ["Inde", "USA", "Chine"],
    selected: null,
  },
  {
    question: "Quel est le plus grand pays au monde ?",
    answer: 1,
    options: ["USA", "Russie", "Canada"],
    selected: null,
  },
]);

const quizCompleted = ref(false);
const currentQuestion = ref(0);
const timer = ref(60);

const score = computed(() => {
  let value = 0;
  questions.value.map((q) => {
    if (q.selected != null && q.answer == q.selected) {
      value++;
    }
  });
  return value;
});

const getCurrentQuestion = computed(() => {
  let question = questions.value[currentQuestion.value];
  question.index = currentQuestion.value;
  return question;
});

const SetAnswer = (e) => {
  questions.value[currentQuestion.value].selected = e.target.value;
  e.target.value = null;
};

const startTimer = () => {
  setInterval(() => {
    timer.value--;
    if (timer.value === 0) {
      quizCompleted.value = true;
    }
  }, 1000);
};

const NextQuestion = () => {
  if (currentQuestion.value === 0) {
    startTimer();
  }
  if (currentQuestion.value < questions.value.length - 1) {
    currentQuestion.value++;
    saveProgress();
    return;
  }
  quizCompleted.value = true;
};

const resetQuiz = () => {
  currentQuestion.value = 0;
  timer.value = 60;
  quizCompleted.value = false;
  questions.value = questions.value.map((question) => {
    question.selected = null;
    return question;
  });
  localStorage.removeItem("quizProgress");
};

const saveProgress = () => {
  localStorage.setItem(
    "quizProgress",
    JSON.stringify({
      currentQuestion: currentQuestion.value,
      timer: timer.value,
      questions: questions.value,
    })
  );
};

const loadProgress = () => {
  const quizProgress = JSON.parse(localStorage.getItem("quizProgress"));
  if (quizProgress) {
    currentQuestion.value = quizProgress.currentQuestion;
    timer.value = quizProgress.timer;
    questions.value = quizProgress.questions;
    startTimer();
  }
};
</script>

<template>
  <main class="qcm">
    <h2>Question 1</h2>

    <section class="quiz" v-if="!quizCompleted">
      <div class="quiz-info">
        <span class="question-qcm">{{ getCurrentQuestion.question }}</span>
      </div>

      <div class="options">
        <label
          v-for="(option, index) in getCurrentQuestion.options"
          :key="index"
          :for="'option' + index"
          :class="`option ${
            getCurrentQuestion.selected == index
              ? index == getCurrentQuestion.answer
                ? 'correct'
                : 'wrong'
              : ''
          } ${
            getCurrentQuestion.selected != null &&
            index != getCurrentQuestion.selected
              ? 'disabled'
              : ''
          }`"
        >
          <input
            type="radio"
            :id="'option' + index"
            :name="getCurrentQuestion.index"
            :value="index"
            v-model="getCurrentQuestion.selected"
            :disabled="getCurrentQuestion.selected"
            @change="SetAnswer"
          />
          <span>{{ option }}</span>
        </label>
      </div>

      <button
        class="buttonQcm"
        @click="NextQuestion"
        :disabled="!getCurrentQuestion.selected"
      >
        {{
          getCurrentQuestion.index == questions.length - 1
            ? "Finish"
            : getCurrentQuestion.selected == null
            ? "Select an option"
            : "Next question"
        }}
      </button>
    </section>

    <section v-else>
      <h2>You have finished the quiz!</h2>
      <p class="question-qcm">
        Your score is {{ score }}/{{ questions.length }}
      </p>
    </section>
  </main>
</template>
```