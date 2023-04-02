```{code-block}
<template>
  <div class="quiz-container">
    <div v-html="textWithAnswers"></div>
    <form v-if="!submitted">
      <div v-for="(blank, index) in blanks" :key="index">
        <select ref="select" v-model="blank.answer">
          <option v-for="option in blank.options" :key="option">
            {{ option }}
          </option>
        </select>
      </div>
      <button @click.prevent="submitQuiz">Submit</button>
    </form>
    <div v-if="submitted">
      <p>Quiz submitted!</p>
      <button @click.prevent="changeAnswer">Change answer</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      submitted: false,
      text: "This is a fill-in-the-blank quiz. The questions are  ___1___ and ___2___",
      blanks: [
        {
          options: ["difficult", "hard", "tough"],
          answer: "",
        },
        {
          options: ["interesting", "engaging", "fascinating"],
          answer: "",
        },
      ],
    };
  },
  computed: {
    textWithAnswers() {
      let textCopy = this.text;
      this.blanks.forEach((blank, index) => {
        if (blank.answer) {
          textCopy = textCopy.replace(`___${index + 1}___`, blank.answer);
        } else {
          textCopy = textCopy.replace(
            `___${index + 1}___`,
            `<span class="blank" @click="openDropdown(index)">___${
              index + 1
            }___</span>`
          );
        }
      });
      return textCopy;
    },
  },
  methods: {
    submitQuiz() {
      this.submitted = true;
    },
    changeAnswer() {
      this.submitted = false;
    },
    openDropdown(index) {
      this.$refs.select[index].focus();
    },
  },
};
</script>

<style scoped>
.quiz-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #333;
  color: #fff;
  padding: 20px;
}

select {
  margin: 10px 0;
}

button {
  padding: 10px 20px;
  background-color: #fff;
  color: #333;
  border: none;
  cursor: pointer;
}

.blank {
  background-color: #fff;
  color: #333;
  padding: 5px 10px;
}
</style>
```