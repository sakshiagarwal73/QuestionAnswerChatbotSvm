const http = require('http'),
    express = require('express'),
    bodyParser = require('body-parser')
    logger = require('morgan'),
    cors = require('cors'),
    promise = require('promise'),
    {spawn} = require('child_process')
    utf8 = require('utf8'),
    { StringDecoder } = require('string_decoder');

const decoder = new StringDecoder('utf8');

var app = express();
const port = (process.env.PORT || 3000);
const hostname = 'localhost';

app.use(bodyParser.json());
app.use(logger('dev'));
app.use(cors());



app.get("/" , express.static(__dirname + '/frontEnd'));
app.post('/',(req,res,next)=>{
    //console.log(req.body.message)
    const scr = spawn('python3',['./../script.py'])
    a = scr.stdin.write(req.body.message,'utf8')
    console.log('1234')
    scr.on('error',(err)=>{
        console.log(err)
        next(err)
    })
    scr.stdout.on('data',(data)=>{
        console.log(data)
        a = decoder.write(data)
        if(a[0]!=='s'){
            console.log(a)
            res.send(data);
        }
        scr.stdin.end();
        scr.on('exit',(code)=>{
            console.log(code)
        })
    })
    scr.stderr.on('data',(data)=>{
        console.log('Program Error:',data)
        scr.stdin.end();
        res.send(data);
        scr.on('exit',(code)=>{
            console.log(code)
        })
    })
})



app.use('/', function(err, req, res, next) {
    res.locals.message = err.message;
    res.status(err.status || 500);
    res.send('Error: ' + err.message);
});

var server = http.createServer(app);
server.listen(port);