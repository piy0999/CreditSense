window.onload = function()
            {
               var x = document.getElementById('submit');
               x.onclick = function()
               {
                var xhttp = new XMLHttpRequest();
                xhttp.open("POST","http://52.187.163.79:9685",true);
                xhttp.setRequestHeader("Content-type", "application/json");
                var val = document.getElementById('hkid_val').value;
                console.log(val)
                var data = {};
                data['id'] = val;
                console.log(data);
                var lamda = JSON.stringify(data);
                xhttp.send(lamda);
                
                xhttp.onload = function(){
                  window.location.href = "scoredash/index.html";
                };
               };

            };