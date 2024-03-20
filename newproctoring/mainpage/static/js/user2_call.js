document.addEventListener("DOMContentLoaded", function(event) {
// Получаем доступ к видеокамере
navigator.mediaDevices.getUserMedia({ video: true })
  .then(function(stream) {
    // Камера доступна, начинаем отслеживать состояние
    var video = document.querySelector('video');
    video.srcObject = stream;
    video.oninactive = function() {
      // Камера больше не активна, отправляем сообщение в чат
      var chatInput = document.querySelector('#chat-input');
      var errorMessage = 'Пользователь пропал с камеры!';
      chatInput.value = errorMessage;
      chatInput.dispatchEvent(new KeyboardEvent('keydown', {key: 'Enter'}));
    }
  })
  .catch(function(err) {
    // Обрабатываем ошибку доступа к камере
    console.error('Ошибка доступа к камере', err);
  });
});

const chatWindow = document.querySelector('#chat-window');
const chatHeader = document.querySelector('#chat-header');
const closeChatBtn = document.querySelector('#close-chat');
const chatMessages = document.querySelector('#chat-messages');
const chatForm = document.querySelector('#chat-form');
const chatInput = document.querySelector('#chat-input');

// Показать окно чата
chatHeader.addEventListener('click', () => {
    chatWindow.classList.toggle('chat-open');
});

// Закрыть окно чата
closeChatBtn.addEventListener('click', () => {
    chatWindow.classList.remove('chat-open');
});

// Отправить сообщение
chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const message = chatInput.value.trim();
    if (message) {
        const newMessage = document.createElement('div');
        newMessage.textContent = message;
        chatMessages.appendChild(newMessage);
        chatInput.value = '';
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
