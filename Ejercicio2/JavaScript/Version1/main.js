var start = 1;
var rows = 3;
var ans = "";

function russianPeasant(n, m) {
  var an = 0;
  while(m) {
    if(m % 2) 
      an = an + n;
    n = n << 1;
    m = m >> 1;
  }
  ans += "<h1>" + an + "</h1>";
}

function multiply(left, right) {
    var answer, expected;
    answer = 0;

    expected = left * right;
    do {
        if (left & 1) // If it's an odd number
        {
            answer += right;
        }
        left = left / 2;
        right = right + right;
    } while (left >= 1);

    if (answer != expected) {
        alert('FAILURE! Expected ' + expected + ', but got ' + answer);
    }
    ans += "<br><h1>" + answer + "</h1>";
}

function generate() {
  start = parseInt(document.getElementById("start").value);
  rows = parseInt(document.getElementById("rows").value);
  ans += "<br><h1>Forma original:</h1>"; 
  var a = +new Date();
  russianPeasant(start, rows);
  var b = +new Date();
  ans += "<br><h1> El tiempo de ejecucion fue: " + (b - a) + " ms";
  ans += "<br><h1>Forma alternativa:</h1>"; 
  var c = +new Date();
  multiply(start, rows);
  var d = +new Date();
  ans += "<br><h1> El tiempo de ejecucion fue: " + (d - c) + " ms";
  document.getElementById("bod").innerHTML = ans;
}
