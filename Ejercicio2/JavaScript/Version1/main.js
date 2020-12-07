var start = 1;
var rows = 3;
var ans = "";

function russianPeasant(n, m) {
  var an = 0;
  while(m) {
    if(m % 2) 
      an = an + n;
    n = parseInt(n * 2);
    m = parseInt(m / 2);
  }
  ans = "<h1>" + an + "</h1>";
}

function generate() {
  start = parseInt(document.getElementById("start").value);
  rows = parseInt(document.getElementById("rows").value);
  var d = new Date();
  var a = +new Date();
  russianPeasant(start, rows);
  var b = +new Date();
  console.log(b - a);
  ans += "<br><h1> El tiempo de ejecucion fue: " + (b - a) + " ms";
  document.getElementById("bod").innerHTML = ans;
}
