/* CONSTANTS */
const UPLOAD_BTN = document.getElementById("upload-btn"),
    BASE_URL = "http://0.0.0.0:8000/";

/* EVENT_LISTENERS */
window.addEventListener("load", loadFiles);
UPLOAD_BTN.addEventListener("click", uploadFile)

/* MAIN */



function loadFiles(e){


    let query = `${BASE_URL}files/`;

    let init = {
        "method":"GET",
        "headers": { "accept": "application/json"},
        "Access-Control-Allow-Origin": "http://localhost:8000"
    };

    fetch(`${query}`,init)
    .then((response)=> {
        return response.json();
    })
    .then((result)=> {

        console.log(result);
        
    });

}

const filetoBase64 = function(file) { 
    return new Promise(
        (resolve, reject) => {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => resolve(reader.result);
            reader.onerror = error => reject(error);
        }
    );
}

function uploadFile(e){
    e.preventDefault();
    

    let formData = new FormData();
    let fileField = document.querySelector("input[type='file']").files[0];

    let uploadedBy = document.getElementById("uploaded-by").value;
    let description = document.getElementById("description").value;
    let fileName = fileField.name;
    let fileType = fileField.type.split("/")[1]

    formData.append("file_name", fileName);
    formData.append("uploaded_by", uploadedBy);
    formData.append("description", description);
    formData.append("file_type", fileType);
    formData.append('file', fileField);

    let query = `${BASE_URL}file/${fileName}/${uploadedBy}/${description}/${fileType}`;

    let init = {
        "method":'POST',
        //"headers": {"Content-type": "multipart/form-data"},
        "body": formData,
        "Access-Control-Allow-Origin": "http://localhost:8000"
    };

    fetch(`${query}`,init)
    .then((response)=> {
        return response.json();
    })
    .then((result)=> {

    });
    
}

