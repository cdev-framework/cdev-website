TYPER = null
RESETER = null
NEXT_MESSAGE = 0
MESSAGES = []

$( document ).ready(function() {
    console.log( "ready!" );

    //$(".dynamic-text").text("HelloWorlds")
    console.log($(".dynamic-text").data()["info"])
    console.log($(".dynamic-text").text())
    MESSAGES = $(".dynamic-text").data()["info"].split(",")

    dynamic_typer(MESSAGES)
});

function dynamic_typer(){
    start_typer(MESSAGES[NEXT_MESSAGE])

    NEXT_MESSAGE++

    if(NEXT_MESSAGE == MESSAGES.length){
        NEXT_MESSAGE = 0
    }

}

function start_typer(message){
    TYPER = setInterval(function(){type(message)}, 50)
}

function start_reseter(){
    RESETER = setInterval(function(){erase()}, 40)
}

function stop_typer(){
    clearInterval(TYPER)
}

function stop_reseter(){
    clearInterval(RESETER)
}


function type(message){
    final_message = message
    current_message = $(".dynamic-text").text()

    if (current_message.length == final_message.length){
        stop_typer()
        setTimeout(start_reseter, 3000);

    }
    else{
        next_message = current_message.concat(final_message.charAt(current_message.length))
        $(".dynamic-text").text(next_message)
    }
}

function erase(){
    current_message = $(".dynamic-text").text()

    if (current_message.length == 0){
        stop_reseter()
        dynamic_typer()
    }
    else{
        next_message = current_message.slice(0,-1)
        $(".dynamic-text").text(next_message)
    }
} 
