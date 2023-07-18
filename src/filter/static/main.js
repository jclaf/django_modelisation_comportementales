function add_date(){
    var elem = document.getElementById('add');
    
    var divElem = document.getElementById('myDIV2'); 
    if(elem.checked == true){
        divElem.style.display = 'block'  ; 
    }else{
        divElem.style.display = 'none'  ;
    }
}


document.getElementById("YOURFORMNAMEHERE").addEventListener = function(e) {
    var key = e.charCode || e.keyCode || 0;     
    if (key == 13) {
      e.preventDefault();
    }
  }