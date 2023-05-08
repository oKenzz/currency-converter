const rateMenu = document.getElementById("rateMenu");
const baseValue = document.getElementById("inputBaseValue");
const baseValueForm = document.getElementById("baseValueForm");
const rateForm = document.getElementById("rateForm");
const displayData = document.getElementById("displayData")
const url = "http://127.0.0.1:5500/data"

let newValue;
let currency;


function getData(){
fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log(data)
    newValue = data.newValue;
    currency = data.currency;
  })
  .catch(error => {
    console.error(error);
  });
}

function submitForm(){
    rateMenu.addEventListener("change", function() {
        rateForm.submit();
        getData();
        console.log(newValue);
        displayData.innerHTML = newValue;
      });
      
    baseValue.addEventListener("change", function() {
        baseValueForm.submit();
        getData();
        displayData.innerHTML = `${newValue} ${currency}`;
    });
}

window.onload = submitForm