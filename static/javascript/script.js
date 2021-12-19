/* jshint esversion: 6 */
/*jslint browser:true */

// Create constants for html input.
const dropButton = document.getElementById("dropdownMenuLink");
const dropDown = document.getElementById("myDropdown");
const dropdowns = document.getElementsByClassName("dropdown-menu");
const navBar = document.getElementsByClassName("navbar");
var i;
const openDropdown = dropdowns[i];

//https://www.w3schools.com/bootstrap/bootstrap_ref_js_dropdown.asp
// referenced and edited for dropdownMenu

/**
 * @function dropdownMenu When the user clicks on the button,
* toggle between hiding and showing the dropdown content.
 */

function dropdownMenu() {
  dropDown.classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
navBar.onclick = function (event) {
  if (!event.target.matches(".steps-button")) {
      for (i = 0; i < dropdowns.length; i++) {
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};

dropButton.addEventListener("click", dropdownMenu);

// https://getbootstrap.com/docs/5.0/components/tooltips/
// referenced and edited for
// tooltips

const tooltipTriggerList = [].slice.call(document
                                         .querySelectorAll(
                                         "[data-bs-toggle='tooltip']"));
const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});

// the below code is from:
// https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_autocomplete
// and edited for purpose

const steps = ["Getting Started", "Empathy", "Define", "Ideate",
               "Prototype", "Test", "Finishing Off"];
const input = document.getElementById("myInput");
var currentFocus;

function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/

  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function (e) {
    var a, b, c, val = this.value;
    /*close any already open lists of autocompleted values*/
    closeAllLists();
    if (!val) {
      return false;
    }
    currentFocus = -1;
    /*create a DIV element that will contain the items (values):*/
    a = document.createElement("DIV");
    a.setAttribute("id", this.id + "autocomplete-list");
    a.setAttribute("class", "autocomplete-items");
    /*append the DIV element as a child of the autocomplete container:*/
    this.parentNode.appendChild(a);
    /*for each item in the array...*/
    for (c = 0; c < arr.length; c++) {
      /*check if the item starts with the same letters
       as the text field value:*/
      if (arr[c].substr(0, val.length).toUpperCase() === val.toUpperCase()) {
        /*create a DIV element for each matching element:*/
        b = document.createElement("DIV");
        /*make the matching letters bold:*/
        b.innerHTML = "<strong>" + arr[c].substr(0, val.length) + "</strong>";
        b.innerHTML += arr[c].substr(val.length);
        /*insert a input field that will hold the current array item's value:*/
        b.innerHTML += "<input type='hidden' value='" + arr[c] + "'>";
        /*execute a function when someone clicks on
        the item value (DIV element):*/
        b.addEventListener("click", function (e) {
          /*insert the value for the autocomplete text field:*/
          inp.value = this.getElementsByTagName("input")[0].value;
          /*close the list of autocompleted values,
          (or any other open lists of autocompleted values:*/
          closeAllLists();
        });
        a.appendChild(b);
      }
    }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function (e) {
    var x = document.getElementById(this.id + "autocomplete-list");
    if (x){ x = x.getElementsByTagName("div")}
    if (e.keyCode === 40) {
      /*If the arrow DOWN key is pressed,
      increase the currentFocus variable:*/
      currentFocus++;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode === 38) { //up
      /*If the arrow UP key is pressed,
      decrease the currentFocus variable:*/
      currentFocus--;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode === 13) {
      /*If the ENTER key is pressed, prevent the
       form from being submitted,*/
      e.preventDefault();
      if (currentFocus > -1) {
        /*and simulate a click on the "active" item:*/
        if (x) {x[currentFocus].click()
               }
      }
    }
  });

  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) { return false;
            }
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) { currentFocus = 0
                                    }
    if (currentFocus < 0) { currentFocus = (x.length - 1)
                            }
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }

  function removeActive(x) {
    /*a function to remove the "active" class from all
     autocomplete items:*/
    for ( i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }

  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for ( i = 0; i < x.length; i++) {
      if (elmnt !== x[i] && elmnt !== inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
    closeAllLists(e.target);
  });
}

/*initiate the autocomplete function on the "myInput" element,
and pass along the steps array as possible autocomplete values:*/
autocomplete(document.getElementById("myInput"), steps);

//added the below code to allow the submission of the autokey
// search with the enter key
input.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("submitButton").click();
  }
});

//Account sidebar https://bootstrapious.com/p/bootstrap-sidebar

$(document).ready(function () {

  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
  });

});

// set timeout function for messages as per
// the code institute example project.
setTimeout(function () {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close(messages);}
           , 2000);