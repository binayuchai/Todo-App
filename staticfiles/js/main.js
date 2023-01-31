


// Function for POST and UPDATE


function operation_data(url,formData,method_type)
{
 
  fetch(url,{
    method:method_type,
    credentials: "same-origin",
    headers: {
      "X-Requested-With":"XMLHttpRequest",
      "X-CSRFToken":getCookie("csrftoken"),
    },
    body: JSON.stringify({payload: formData })
  })
  .then(response => response.json())
  .then(data=>{
    console.log(data);
  });

}




