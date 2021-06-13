$(document).ready(function () {
    $.ajax({
        url: endpoint,
        data: {
            "user_response": "hi" // put actual user response here
        },
        success: function(data) {
            console.log(data)
        }
    })
})