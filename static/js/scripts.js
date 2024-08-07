$(document).ready(function() {
    const socket = new WebSocket('ws://' + window.location.host + '/ws/email/');

    socket.onopen = function() {
        const loadingItem = document.querySelector('.loading');
        if (loadingItem) {
            loadingItem.textContent = 'Connected. Waiting for messages...';
        }
    };

    socket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const messageList = document.getElementById('message-list');
        const loadingItem = document.querySelector('.loading');
        if (loadingItem) {
            messageList.removeChild(loadingItem);
        }
        const li = document.createElement('li');
        li.textContent = data.message;
        messageList.appendChild(li);
    };

    socket.onclose = function(e) {
        console.error('WebSocket closed unexpectedly');
        const messageList = document.getElementById('message-list');
        const li = document.createElement('li');
        li.textContent = 'Connection closed. Please refresh the page to reconnect.';
        messageList.appendChild(li);
    };

    socket.onerror = function(error) {
        console.error('WebSocket error:', error);
        const messageList = document.getElementById('message-list');
        const li = document.createElement('li');
        li.textContent = 'Connection error. Please try again later.';
        messageList.appendChild(li);
    };
});