function ajaxCall(message) {
	$.ajax({
		url: chatbot_endpoint,
		data: {
			user_response: message,
		},
		success: function (data) {
			$("#chatlogs").append(` 
				<div class="chat friend">
					<div class="user-photo">
						<img src="/static/img/user.png" />
					</div>
					<p class="chat-message">${data.bot_response}</p>
				</div>
			`);
			if (data.url != null) {
				$(this)
					.delay(3000)
					.queue(function () {
						$("#chatbotModal").modal("hide");
						$("#redirectingModal").modal("show");
						setTimeout(function () {
							window.location.replace(data.url);
							$("#chatbotModal").modal("hide");
						}, 2000);
						$(this).dequeue();
					});
			}
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
	$("#message").val("");
}

$(document).ready(function () {
	$("#message").keyup(function (e) {
		if (e.key === "Enter") {
			message();
		}
	});
});
