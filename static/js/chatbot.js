function ajaxCall(message) {
  console.log(message);
  $.ajax({
    url: chatbot_endpoint,
    data: {
      user_response: message,
    },
    success: function (data) {
      $("#chatlogs").append(
        ` <div class="chat friend">
                <div class="user-photo">
                  <img src="/static/img/user.png" />
                </div>
                <p class="chat-message">${data.bot_response}</p>
              </div>`
      );
    },
  });
}

function message() {
  $("#chatlogs").append(
    `<div class="chat self" ><p class="chat-message">${
      document.getElementById("message").value
    }</p></div>`
  );
  ajaxCall($("#message").val());
  $("#message").clear()
}
