var prevArr = [1];
var curArr = [1, 1];
var start = 1;
var rows = 3;
var ans = "";

function Pascal() {
  prevArr = [start];
  curArr = [start, start];
  ans = "<h1>"
  for (var i = 0; i <= rows; i++) {
    if (rows > 2) {
      prevArr = curArr;
      curArr = new Array(i);
      CreateRows();
    } else if(rows < 2){
      ans = "<h1>¡Un triángulo necesita al menos dos niveles!</h1>";
    }
    else{
      ans = "<h1>" + prevArr + "<br>" + curArr[0] + " " + curArr[1] + "</h1>";
    }
  }
  ans += "</h1>";
}

function CreateRows() {
  for (var i = 0; i < curArr.length; i++) {
    if (i == 0 || i == curArr.length - 1) {
      curArr[i] = start;
    } else {
      curArr[i] = prevArr[i - 1] + prevArr[i];
    }
    ans += (curArr[i] + " ");
  }
  ans += ("<br>");
}

function generate() {
  start = parseInt(document.getElementById("start").value);
  rows = parseInt(document.getElementById("rows").value);
  var d = new Date();
  var a = +new Date();
  Pascal();
  var b = +new Date();
  ans += "<br><h1> El tiempo de ejecucion fue: " + (b - a) + " ms";
  document.getElementById("bod").innerHTML = ans;
}
