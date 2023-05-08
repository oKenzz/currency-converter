const rateMenu = document.getElementById("rateMenu");
const baseValue = document.getElementById('inputBaseValue');
const baseValueForm = document.getElementById("baseValueForm");
const rateForm = document.getElementById("rateForm");

function submitForm(){
    rateMenu.addEventListener("change", function() {
        rateForm.submit();
      });
      
    baseValue.addEventListener("change", function() {
        baseValueForm.submit();
    })   
}

window.onload = submitForm