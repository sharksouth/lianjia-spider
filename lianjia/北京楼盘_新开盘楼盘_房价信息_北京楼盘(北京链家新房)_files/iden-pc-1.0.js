(function () {
    function gc(n) {
        var x = n + '=';
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(x) == 0) {
                return c.substring(x.length, c.length);
            }
        }
        return '-';
    }
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/relation/' + md5(window.location.host + window.location.pathname + '/' + gc('lianjia_uuid')));
    xhr.send('');
})()