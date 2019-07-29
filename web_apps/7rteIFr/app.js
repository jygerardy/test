


$(document).ready(function () {
    let modifiedData = {"myData":[1,2,3,4]};
    $.getJSON(getWebAppBackendUrl('/first_api_call'), modifiedData,  function(data) {
        console.log(data.status)
});
    };

