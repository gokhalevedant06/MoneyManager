$(document).ready(function () {
    $("#query_body").hide();
    $('#investment_search').keyup(function () {
        $.ajax({
            url: endpoint,
            data: {
                'query': $('#investment_search').val(),
            },
            success: function (data) {
                if ($('#investment_search').val() != '' || $('#investment_search').val() != null) {
                    $("#query_body").show();
                    $("#query_body").html(data['html']);
                    $("#regular_body").hide();
                }
                else {
                    $("#query_body").hide();
                    $("#regular_body").show();
                }
            }
        })
    })
}) 