

const api_url = "http://192.168.31.82:1234/users"

function loadData(records = []) {
    var table_data = "";
        for(let i=0; i<records.length; i++) {
                table_data += `<tr>`;
                table_data += `<td>${records[i]['ID']}</td>`;
                table_data += `<td>${records[i]['Name']}</td>`;
                table_data += `<td>${records[i]['Age']}</td>`;
                table_data += `<td>${records[i]['City']}</td>`;
                table_data += `<td>`;
                table_data += `<a href="edit.html?id=${records[i]['ID']}"><button class="btn btn-primary">Edit</button></a>`;
                table_data += '&nbsp;&nbsp;';
                table_data += `<button class="btn btn-danger" onclick=deleteData('${records[i]['ID']}')>Delete</button>`;
                table_data += `</td>`;
                table_data += `</tr>`;
        }
        console.log(table_data);
        document.getElementById("tbody").innerHTML = table_data;
}



function getData() {
        fetch(api_url)
        .then((response) => response.json())
        .then((data) => {
                //console.table(data);
                loadData(data);
        });
}

function getDataById(ID) {
        fetch(`${api_url}edit?ID=${ID}`)
        .then((response) => response.json())
        .then((data) => {

                console.log(data);
                document.getElementById("ID").value = data[0]['ID'];
                document.getElementById("Name").value = data[0]['Name'];
                document.getElementById("Age").value = data[0]['Age'];
                document.getElementById("City").value = data[0]['City'];
        })
}

function postData() {
        var Name = document.getElementById("Name").value;
        var Age = document.getElementById("Age").value;
        var City = document.getElementById("City").value;


        data = {Name: Name, Age: Age, City: City};

        fetch(api_url, {
                method: "POST",
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
        })
        .then((response) => response.json())
        .then((data) => {
                console.log(data);
                window.location.href = "index.html";
        })
}



function putData() {

        var ID = document.getElementById("ID").value;
        var Name = document.getElementById("Name").value;
        var Age = document.getElementById("Age").value;
        var City = document.getElementById("City").value;

        data = {ID: ID, Name: Name, Age: Age, City: City};
        console.log(data)
        fetch(api_url, {
                method: "PUT",
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
        })
        .then((response) => response.json())
        .then((data) => {
                console.table(data);
                window.location.href = "index.html";
        })
}



function deleteData(ID) {
        console.log(ID);
        user_input = confirm("Are you sure you want to delete this record?");
        if(user_input) {
                fetch(api_url+"?ID="+ID, {
                        method: "DELETE",
                        headers: {
                          'Accept': 'application/json',
                          'Content-Type': 'application/json'
                        },
                        //body: JSON.stringify({"id": id})
                })
                .then((response) => response.json())
                .then((data) => {
                        console.log(data);
                        window.location.reload();
                })
        }
}
