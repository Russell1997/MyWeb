var exec = require('child_process').exec;
// var arg1 = 'https://mp.weixin.qq.com/s/wNmK6L7nEWRSJKHWiDUrtQ';
var arg1;


exec('python wechatcrawler.py  '+ arg1+' ', function(error, stdout, stderr){
    if(stdout){
        console.log(stdout);
    } else {
        console.log(stderr);
    }
    if(error) {
        console.info('caib');
    }
});
