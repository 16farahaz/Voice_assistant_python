$(document).ready(function () {
    //display speak message
eel.expose(DisplayMessage)
function DisplayMessage(message){
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate('start');
    


    eel.expose(ShowHood)
    function ShowHood(){
        $("#oval").attr("hidden",false);
        $("#Siriwave").attr("hidden",true);

    }
}
});