const signInBtn = document.querySelector('.signin-btn');
const signUpBtn = document.querySelector('.signup-btn');
const formBox = document.querySelector('.form-box');
const body = document.body;

signUpBtn.addEventListener('click', function () {
    formBox.classList.add('active');
    body.classList.add('active');
});

signInBtn.addEventListener('click', function () {
    formBox.classList.remove('active');
    body.classList.remove('active');
});

signInButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "web_dev") {
        alert("Добро пожаловать!");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})