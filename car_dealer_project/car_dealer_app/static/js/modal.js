
function rent(id){



// Get the modal
var modal = document.getElementById('myModal-' + id);

// Get the button that opens the modal
var btn = document.getElementById("btn-"+ id);

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close-"+ id)[0];

// When the user clicks the button, open the modal 

modal.style.display = "block";


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

}

function del(id){



    // Get the modal
    var modal = document.getElementById('myModal_del-' + id);
    
    // Get the button that opens the modal
    var btn = document.getElementById("btn_del-"+ id);
    
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close_del-"+ id)[0];
    
    // When the user clicks the button, open the modal 
    
    modal.style.display = "block";
    
    
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
    
    }
    