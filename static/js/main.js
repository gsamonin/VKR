function Search() {
    var formData = {
        'search': $("#SearchVacancy").val()
    }
    $.ajax({
        type: 'POST',
        url: '/search',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(formData),
        success: function (response) {
            // location.reload();
            console.log(response);
            $("#vacancyName").text("Вакансия: " + response['vacancy_name']);
        }
    });
}