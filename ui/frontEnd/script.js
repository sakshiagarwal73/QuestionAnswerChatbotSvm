var messages = document.getElementById('messages');
var inp = document.getElementById('inp');
var btn = document.getElementById('btn');

btn.addEventListener('click', (event) => {
    event.preventDefault();
    var greeting = ['hi','hello','hey']
    var bye = ['bye','bi']
    var message = inp.value;
    var mes = document.createElement('li');
    var tex = document.createTextNode(message);
    mes.appendChild(tex)
    mes.className = 'userMessage';
    messages.appendChild(mes);
    inp.value=''
    message.toLowerCase()
    console.log(message)
    if(message===''){
        console.log('wer')
        return;
    }
    if(greeting.includes(message)){
        addMessage('Hello!!');
        return;
    }
    if(bye.includes(message)){
        addMessage('Biee!!');
        return;
    }

    console.log('23',message)
    
    var data = { 'message': message }
    console.log(data)
    var rep = ''
    var req = new XMLHttpRequest();
    req.open('POST', "/", true);
    req.setRequestHeader("Content-Type", "application/json");
    req.responseType = 'text/plain';
    req.onreadystatechange = () => {
        if (req.status === 200 && req.readyState === 4) {
            rep = req.response;
            addMessage(rep);
            //console.log(rep)
        }
    }
    req.send(JSON.stringify(data));
    
})

function addMessage(reply) {
    if(reply=='error'){
        reply = 'Sorry! We couldn\'t find anything suitable. Contact Developer.'
    }
    var repl = document.createElement('li');
    repl.className = 'systemReply';
    var text = document.createTextNode(reply);
    repl.appendChild(text);
    messages.appendChild(repl)
}