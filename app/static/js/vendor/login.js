import { initializeApp } from "https://www.gstatic.com/firebasejs/11.3.1/firebase-app.js";
import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/11.3.1/firebase-auth.js";


// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAp5eKM8TFL_j4wgEPoHURQmkRvrORABCk",
  authDomain: "login-1ee91.firebaseapp.com",
  projectId: "login-1ee91",
  storageBucket: "login-1ee91.firebasestorage.app",
  messagingSenderId: "472988569628",
  appId: "1:472988569628:web:a7f676a86a387cb8fb8fd9"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);




// Submit

const submit = document.getElementById('submit');

submit.addEventListener("click",function(event){
    event.preventDefault();
    

    // Inputs

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    signInWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed up 
    const user = userCredential.user;
    alert("Loging In...");
    window.location.href='/home/';
     
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    alert(errorMessage);

  });

})