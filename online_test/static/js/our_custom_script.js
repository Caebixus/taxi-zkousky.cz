var ul = document.querySelector('ul');
for (var i = ul.children.length; i >= 0; i--) {
  ul.appendChild(ul.children[Math.random() * i | 0]);
}


function showDiv(elem){
  if(elem.name == 10){
    document.getElementById('spravne').style.display = "block";
    document.getElementById('testicek').style.display = "none";
  } else{
    document.getElementById('spatne').style.display = "block";
    document.getElementById('testicek').style.display = "none";
  }
}
