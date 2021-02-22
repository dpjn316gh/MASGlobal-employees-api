/**
 * Small JQuery to controls the view
 */
$(function () {
    var $employees = $('#employees');
    var $employee_id = $('#employee_id');

    /**
     * handles a click event on 'get employees'
     */
    $("#get-employee").click(function () {

        if (!$employee_id.val()) {
            $.ajax({
                url: 'http://localhost:5000/employees',
                type: 'GET',
                dataType: 'json',
                data: 'json',
                contentType: 'application/json; charset=utf-8',
                success: function (data) {
                    $("#datatable tbody tr").remove();
                    $.each(data, function (key, value) {
                        var html = '<tr>' +
                            '<td>' + value.employee_id + '</td>' +
                            '<td>' + value.name + '</td>' +
                            '<td>' + value.role_id + '</td>' +
                            '<td>' + value.role_name + '</td>' +
                            '<td>' + value.role_description + '</td>' +
                            '<td>' + value.monthly_salary + '</td>' +
                            '<td>' + value.hourly_salary + '</td>' +
                            '<td>' + value.contract_type_name + '</td>' +
                            '<td>' + value.annual_salary + '</td>' +
                            '</tr>';

                        $('#datatable tbody').append(html);
                    });
                },
                error: function (xhr, status, error) {
                    console.log(xhr.status)
                    alert("Connection error");
                }
            });
        } else {
            $.ajax({
                url: 'http://localhost:5000/employees/' + $employee_id.val(),
                type: 'GET',
                dataType: 'json',
                data: 'json',
                contentType: 'application/json; charset=utf-8',
                success: function (data) {

                    $("#datatable tbody tr").remove();

                    if (Object.keys(data).length !== 0) {
                        var html = '<tr>' +
                            '<td>' + data.employee_id + '</td>' +
                            '<td>' + data.name + '</td>' +
                            '<td>' + data.role_id + '</td>' +
                            '<td>' + data.role_name + '</td>' +
                            '<td>' + data.role_description + '</td>' +
                            '<td>' + data.monthly_salary + '</td>' +
                            '<td>' + data.hourly_salary + '</td>' +
                            '<td>' + data.contract_type_name + '</td>' +
                            '<td>' + data.annual_salary + '</td>' +
                            '</tr>';

                        $('#datatable tbody').append(html);
                    }

                },
                error: function (xhr, status, error) {
                    console.log(xhr.status)
                    alert("Connection error");
                }
            });
        }
    });

    /**
     * Avoid entering non numeric values on a textbox
     */
    $(".allow-numeric").bind("keypress", function (e) {
        var keyCode = e.which ? e.which : e.keyCode
        if (!(keyCode >= 48 && keyCode <= 57)) {
            $(".error").css("display", "inline");
            return false;
        } else {
            $(".error").css("display", "none");
        }
    });
});

