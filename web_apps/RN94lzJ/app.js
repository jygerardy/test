

var data = {"myData": [1,2,3,4,5]};

var sendData = function () {
    $.getJSON(getWebAppBackendUrl('/first_api_call'), function(data) {
    console.log('sent to backend')
    });
};

sendData(); 