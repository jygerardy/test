



var sendData = function () {
    var data = {"myData": [1,2,3,4,5]};
    $.getJSON(getWebAppBackendUrl('/first_api_call'), function(data) {
    console.log(data)
    });
};

sendData(); 