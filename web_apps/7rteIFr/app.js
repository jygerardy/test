


$(document).ready(function () {
    let modifieData = {"myData":[1,2,3,4]};
    $.getJSON(getWebAppBackendUrl('/first_api_call'), function(data) {
        console.log(data.status)
});
    };

