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
        const emailList = document.getElementById('message-list');
        const loadingItem = document.querySelector('.loading');
        if (loadingItem) {
            emailList.removeChild(loadingItem);
        }
        const li = document.createElement('li');
        li.textContent = data.message;
        emailList.appendChild(li);
    };

    socket.onclose = function(e) {
        console.error('WebSocket closed unexpectedly');
        const emailList = document.getElementById('message-list');
        const li = document.createElement('li');
        li.textContent = 'Connection closed. Please refresh the page to reconnect.';
        emailList.appendChild(li);
    };

    socket.onerror = function(error) {
        console.error('WebSocket error:', error);
        const emailList = document.getElementById('message-list');
        const li = document.createElement('li');
        li.textContent = 'Connection error. Please try again later.';
        emailList.appendChild(li);
    };
});