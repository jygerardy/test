
var modifiedData = {"myData":[1,2,3,4]};
var sendData =  function (){
   
    $.getJSON(getWebAppBackendUrl('/first_api_call'), modifiedData,  function(data) {
        console.log(data.status)
});
    };


sendData()

