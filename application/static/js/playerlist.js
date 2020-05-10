/*document.addEventListener('DOMContentLoaded', () => {

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    // When a new vote is announced, add to the unordered list
    socket.on('add player', data => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="{{ url_for('main_bp.dashboard') }}" class="list-group-item list-group-item-action h5-responsive font-sharetech min-w-min-cont" id="${ data }">
                        ${ data }: Alive
                       </a>`;
        li.id = data;
        document.querySelector('#playerList').append(li);
    });



    socket.on('connect', () => {
        console.log('sent join room request')
        socket.emit('join room');
    })

});*/

document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect', () => {
        socket.emit('join room');

        document.querySelector("#leaveBattle").onclick = () => {
            console.log('leaving room');
            socket.emit('leave room');
        };

        socket.on('add player', data => {
            console.log(data);

            const a = document.createElement('a');
            a.href = "{{ url_for('main_bp.dashboard') }}";
            a.classList.add("list-group-item", "list-group-item-action", "h5-responsive", "font-sharetech", "min-w-min-cont");
            a.id = data;
            a.innerHTML = `${ data } : Alive`;
            document.querySelector('#playerList').append(a);
        });

        socket.on('remove player', data => {
            console.log(data)
            document.querySelector(`#${ data }`).remove();
        });


    });




});
