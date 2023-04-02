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

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.qcm {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-self: center;
  border-radius: 15px;
  padding: 20px 0px;
  background-color: var(--dark-alt);
}
h2 {
  color: var(--light);
  font-size: 2rem;
  margin-bottom: 2rem;
}
.quiz {
  background-color: var(--dark);
  padding: 1rem;
  width: 100%;
  max-width: 640px;
  border-radius: 0.5rem;
  flex-direction: column;
}
.quiz-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
}
.quiz-info .question {
  color: var(--light);
  font-size: 1.25rem;
}
.quiz-info .score {
  color: var(--light);
  font-size: 1.25rem;
}
.options {
  margin-bottom: 1rem;
}
.option {
  padding: 1rem;
  display: block;
  background-color: white;
  margin-bottom: 0.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
}
.option:hover {
  background-color: var(--grey);
}
.option.correct {
  background-color: #00ff37;
}
.option.wrong {
  background-color: #ff0008;
}
.option:last-of-type {
  margin-bottom: 0;
}
.option.disabled {
  opacity: 0.5;
}
.option input {
  display: none;
}
.buttonQcm {
  appearance: none;
  outline: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem 1rem;
  background-color: var(--primary);
  color: var(--dark);
  font-weight: 700;
  text-transform: uppercase;
  font-size: 1.2rem;
  border-radius: 0.5rem;
}
button:disabled {
  background-color: var(--grey);
}
h2 {
  font-size: 2rem;
  margin-bottom: 2rem;
  text-align: center;
}
.question-qcm {
  color: var(--light);
  font-size: 1.5rem;
  text-align: center;
}
</style>
```