
function getSeatsValue() {
    console.log("seat"); 
    var uiSeats = document.getElementsByName("uiSeats");
    for(var i in uiSeats) {
      if(uiSeats[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
           
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var Km_driven = document.getElementById("uiKm");
    var Mileage = document.getElementById("uiMl");
    var Engine = document.getElementById("uiEg");
    var Seats = getSeatsValue();
    var No_years = document.getElementById("uiNoy");
    var Fuel = document.getElementById("uiFuels");
    var estPrice = document.getElementById("uiEstimatedPrice");
    var url = "http://127.0.0.1:5000/predict_cardekho_price";  //Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards  
    $.post(url, {
        km_driven: parseInt(Km_driven.value),
        mileage: parseInt(Mileage.value),
        engine: parseInt(Engine.value),
        seats: Seats,
        no_years: parseInt(No_years.value),
        fuel: Fuel.value
    },function(data, status) {
        console.log("Estimate price button clicked");
        console.log(data.estimated_Price);
        estPrice.innerHTML = "<h2>" + data.estimated_Price.toString() + " Rupees</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
     var url = "http://127.0.0.1:5000/get_fuel_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_fuel_names request");
        if(data) {
            var fuels= data.fuels;
            var uiFuels = document.getElementById("uiFuels");
            $('#uiFuels').empty();
            for(var i in fuels) {
                var opt = new Option(fuels[i]);
                $('#uiFuels').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;