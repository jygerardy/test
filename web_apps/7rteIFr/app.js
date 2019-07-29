


$(document).ready(function () {
    var modifiedData = {"myData":[1,2,3,4]};
    sendData();
})
                  
var sendData =  function (modifiedData){     
    $.getJSON(getWebAppBackendUrl('/first_api_call'), modifiedData,  function(data) {
    console.log(data.status)
});
    };