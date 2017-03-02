function getBey(res){
    var images = "";

    for(var i = 0; i < res.images.length; i++) {
        images+="<img src='"+res.images[i].url+"' alt=>";
        }

    $('h2').html(
        `<p>${images}</p>`
    )
}

function beyMood(){
    var mood = $('#mood').val()
    song = ''
    if (mood == 'happy'){
        song = '3axkNosdVQLZiq1HakuGhc'
    }
    if (mood == 'dancey'){
        song = '02M6vucOvmRfMxTXDUwRXu'
    }
    if (mood == 'sad'){
        song = '31acMiV67UgKn1ScFChFxo'
    }
    if (mood == 'vengeful'){
        song = '2ZBNclC5wm4GtiWaeh0DMx'
    }
    if (mood == 'loving'){
        song = '5IVuqXILoxVWvWEPm82Jxr'
    }
    $('.player').html(
        `<iframe src="https://embed.spotify.com/?uri=spotify:track:${song}" frameborder="0" allowtransparency="true"></iframe>`
    )

}

$(document).ready(function(){
    console.log('working');

    // $('.building_blocks').submit(function(e){
    //     e.preventDefault();
        // $.ajax({
        //     url: "/",
        //     method: 'post',
        //     data: $(this).serialize(),
        //     success: function(serverResponse){
        //         $('.notes').html(serverResponse)
        //         console.log("Received this from server: ", serverResponse)
        //     },
        // })
    // })

    $('h2').on('click', function(){
        $.get('https://api.spotify.com/v1/artists/6vWDO969PvNqNYHIOW5v0m', function(res){
            console.log(res);
            getBey(res);
        })
    })

    $('.bey_moods').submit(function(e){
        e.preventDefault();
        console.log('Mood selection is: '+$('#mood').val());
        beyMood()
    })

})
