const crypto = require('crypto-js');
var time = Date.now();
var fin = 'daisydaisy_giveme_your_answer_do' + String(time);
var final = crypto.MD5(fin).toString();
document.cookie = 'key=' + final;
// (
//     function key() {
//         var kkstore = {
//             '1900': 'm',
//             '1901': 'o',
//             '1902': 'i'
//         };
//         console.log(kkstore['1900'] + kkstore['1901'] + kkstore['1902']);
//         return kkstore['1900'] + kkstore['1901'] + kkstore['1902'];
//     }
// )();
// console.log(key())