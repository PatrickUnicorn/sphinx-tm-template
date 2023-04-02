# Formulaire de connexion Admin ou simple utilisateur

Le composant est divisé en trois parties principales :

## 1. Template

Cette partie contient le code HTML qui définit la structure du formulaire de connexion et ses éléments interactifs.

```{code-block}
<template>
      <div class="login-form" v-if="!isAdmin && !isUser">
        <h2>Please Login</h2>
        <form @submit.prevent="login">
          <label>
            Username:
            <input type="text" v-model="loginUsername" />
          </label>
          <label>
            Password:
            <input type="password" v-model="loginPassword" />
          </label>
          <button id="loginAsAdmin" @click="login">Login as Admin</button>
          <p v-show="loginError">Invalid username or password.</p>
          <button id="loginAsUser" @click="loginAsUser">Login as User</button>
        </form>
      </div>
  </template>
```

## Structure du template

### div.login-form

- S'affiche uniquement lorsque les variables "isAdmin" et "isUser" sont fausses.
- Contient le formulaire de connexion.

### h2

- Affiche "Please Login" comme titre du formulaire de connexion.

### form

- Présente un écouteur d'événement "submit" qui empêche le comportement par défaut et appelle la méthode "login".
- Contient des champs pour le nom d'utilisateur et le mot de passe, ainsi que des boutons pour se connecter en tant qu'administrateur ou utilisateur.

#### label (Nom d'utilisateur)

- Un label pour le champ de saisie du nom d'utilisateur.
- Contient un champ de saisie pour entrer le nom d'utilisateur avec une liaison bidirectionnelle à la propriété de données "loginUsername".

#### label (Mot de passe)

- Un label pour le champ de saisie du mot de passe.
- Contient un champ de saisie pour entrer le mot de passe avec une liaison bidirectionnelle à la propriété de données "loginPassword".

#### button#loginAsAdmin

- Un bouton pour se connecter en tant qu'administrateur.
- Possède un écouteur d'événement "click" qui appelle la méthode "login".

#### p (Message d'erreur)

- Affiche un message d'erreur lorsque la variable "loginError" est vraie.
- Le message est "Invalid username or password."

#### button#loginAsUser

- Un bouton pour se connecter en tant qu'utilisateur.
- Possède un écouteur d'événement "click" qui appelle la méthode "loginAsUser".

## Propriétés de données

### loginUsername

- Stocke la valeur d'entrée pour le champ nom d'utilisateur.
- Réinitialisée après une tentative de connexion.

### loginPassword

- Stocke la valeur d'entrée pour le champ mot de passe.
- Réinitialisée après une tentative de connexion.

### loginError

- Indique si une erreur de connexion s'est produite (faux par défaut).
- Devient vrai si la tentative de connexion échoue.

## Méthodes

### login()

- Vérifie si le nom d'utilisateur et le mot de passe correspondent à ceux de l'administrateur (dans cet exemple, "admin" et "admin123").
- Si les informations d'identification sont correctes :
  - Émet l'événement "login" avec la valeur "admin".
  - Réinitialise la variable "loginError" à faux.
- Si les informations d'identification sont incorrectes :
  - Définit la variable "loginError" à vrai.
- Réinitialise les variables "loginUsername" et "loginPassword".

### loginAsUser()

- Émet l'événement "login" avec la valeur "user".
- Ne nécessite pas de vérification des informations d'identification.

### Éléments clés du formulaire de connexion:

- Le formulaire lui-même, qui utilise l'événement @submit.prevent pour appeler la méthode login lors de la soumission.
- Les champs de saisie Username et Password, liés aux variables de données loginUsername et loginPassword via v-model.
- Les boutons pour se connecter en tant qu'administrateur et utilisateur, avec des gestionnaires d'événements associés.
- Un message d'erreur qui apparaît si les identifiants sont invalides.

## 2. Script

Cette partie contient le code JavaScript qui gère le comportement du composant.

```html
  <script>
  export default {
    props: ['isAdmin', 'isUser'],
    data() {
      return {
        loginUsername: "",
        loginPassword: "",
        loginError: false
      };
    },
    methods: {
      login() {
        if (this.loginUsername === "admin" && this.loginPassword === "admin123") {
          this.$emit("login", "admin");
          this.loginError = false;
        } else {
          this.loginError = true;
        }
        this.loginUsername = "";
        this.loginPassword = "";
      },
      loginAsUser() {
        this.$emit("login", "user");
      }
    }
  };
  </script>
```

### Propriétés et méthodes importantes :

a. props: Un tableau contenant les propriétés passées au composant. Ici, 'isAdmin' et 'isUser' sont utilisés pour déterminer si l'utilisateur est déjà connecté en tant qu'administrateur ou utilisateur.

b. data(): Une fonction qui retourne un objet contenant les variables de données du composant. Les variables sont loginUsername, loginPassword et loginError.

c. methods: Un objet contenant les méthodes qui gèrent le comportement du composant. Les méthodes sont login et loginAsUser.

#### i. login()

Cette méthode est appelée lorsque le formulaire est soumis. Elle vérifie si les identifiants sont corrects et émet un événement 'login' avec la valeur 'admin' si c'est le cas. Sinon, elle affiche un message d'erreur et réinitialise les champs de saisie.

#### ii. loginAsUser()

Cette méthode est appelée lorsque l'utilisateur clique sur le bouton 'Login as User'. Elle émet simplement un événement 'login' avec la valeur 'user'.

## 3. Styles

### (non présents dans le code fourni)

Cette partie contiendrait les styles CSS qui définissent l'apparence du composant mais ces styles sont simples et personnels et donc pas très important pour le faire fonctionner.
