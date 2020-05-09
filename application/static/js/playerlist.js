document.addEventListener('DOMContentLoaded', () => {

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

    socket.on('remove player', data => {
        document.querySelector(`#${ data }`).remove();
    });
});
