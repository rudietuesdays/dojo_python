$(document).ready(function(){
    console.log('working!');
    $.ajax({
        url: "/write",
        method: 'get',
        success: function(serverResponse){
            $('.notes').html(serverResponse)
            console.log("Received this from server: ", serverResponse)
            console.log("Intial notes now loaded")
        }
    })

    $('form').submit(function(e){
        // preventDefault stops the default action of the event (e) from being triggered.
        e.preventDefault();
        console.log("Form submitted but no HTTP request sent to server!");
        $.ajax({
            url: "/write",
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('.notes').html(serverResponse)
                console.log("Received this from server: ", serverResponse)
                console.log("I should probably put that in the DOM...")
            },
        })
    })

    // $('.note_box').on('click', function(){
    //     console.log('clicked');
    //     $.ajax({
    //         url: "/edit/"+id,
    //         method: 'get',
    //     })
    // })

})
