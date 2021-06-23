$(document).ready(function () {
  $.ajax({
    url: endpoint,
    data: {
      user_response: document.getElementById("message").value,
    },
    success: function (data) {
      $("#chatlogs").append(
        ` <div class="chat friend">
                <div class="user-photo">
                  <img src="{% static 'img/user.png' %}" />
                </div>
                <p class="chat-message">${data.bot_response}</p>
              </div>`
      );
      console.log(data);
    },
  });
});

function message() {
  $("#chatlogs").append(
    `<div class="chat self" ><p class="chat-message">${
      document.getElementById("message").value
    }</p></div>`
  );
  $("#message").clear()
}
