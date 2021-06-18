$(document).ready(function () {
    $.ajax({
        url: chatbot_endpoint,
        data: {
            "user_response": "hi" // put actual user response here
        },
        success: function(data) {
            console.log(data)
        }
    })
})