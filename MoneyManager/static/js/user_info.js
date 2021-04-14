$(document).ready(function () {
    $.ajax({
        method: 'get',
        url: endpoint,
        success: function (data) {
            gen = []
            prf = []

            d = JSON.parse(data);
            for (i = 0; i < d.length; i++) {
                if (d[i].fields.field === "gender") {
                    gen.push(d[i].fields.value);
                }
                else if (d[i].fields.field === "profession") {
                    prf.push(d[i].fields.value);
                }
            }

            $('#gender').append(new Option("-------", null, true))
            for (i = 0; i < gen.length; i++) {
                $('#gender').append(
                    new Option(gen[i], gen[i])
                );
            }
            $('#profession').append(new Option("-------", null, true))
            for (i = 0; i < prf.length; i++) {
                $('#profession').append(
                    new Option(prf[i], prf[i])
                );
            }
        },
    })
})