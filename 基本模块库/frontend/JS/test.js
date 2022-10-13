// function fac(n) {
//     var i, product=1;
//     for (i=2;i<=n;i++)
//         product*=i
//     return product
//
// }
// var x=fac(5)
//
// document.write(x)


// cookie

// function setcookie(name, value, daysToLive) {
//     var cookie = name + "=" + encodeURIComponent(value);
//     if(typeof daysToLive === "number");
//         cookie +="; max-age=" + (daysToLive*60*60*24)+ ";path=/";
//     document.cookie=cookie;
// }
//
// setcookie("test","testvalue","2020");
// document.write(document.cookie);


// document.write(document.cookie);



// function getcookie() {
//     var cookie = {};
//     var all = document.cookie;
//     // return all;
//     if (all == '') return cookie;
//
//     var list = all.split(';');
//     // return list;
//
//     for (var i = 0; i < list.length; i++) {
//         var cookie = list[i];
//         var p = cookie.indexOf("=");
//         var name = cookie.substring(0, p);
//         var value = cookie.substring(p + 1);
//         value = decodeURIComponent(value);
//         cookie.name = value;
//     }
//     return cookie;
// }
//
// res=getcookie();
//
//
// var keys=[];
// for (var key in res) keys.push(key);
//
//
// document.write(keys);






































