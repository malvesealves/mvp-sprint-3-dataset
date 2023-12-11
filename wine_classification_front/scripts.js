/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
    let url = 'http://127.0.0.1:5000/vinhos';
    fetch(url, {
        method: 'get',
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.vinhos) {
                data.vinhos.forEach(item => insertList(
                    item.name,
                    item.fixedAcidity,
                    item.volatileAcidity,
                    item.citricAcid,
                    item.residualSugar,
                    item.chlorides,
                    item.freeSulfurDioxide,
                    item.totalSulfurDioxide,
                    item.density,
                    item.ph,
                    item.sulphates,
                    item.alcohol,
                    item.quality
                ))
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()

/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputName, inputFixedAcitidy, inputVolatileAcitidy, inputCitricAcid,
    inputResidualSugar, inputChlorides, inputFreeSulfurDioxide,
    inputTotalSulfurDioxide, inputDensity, inputPh,
    inputSulphates, inputAlcohol) => {

    const formData = new FormData();
    formData.append('name', inputName);
    formData.append('fixedAcidity', inputFixedAcitidy);
    formData.append('volatileAcidity', inputVolatileAcitidy);
    formData.append('citricAcid', inputCitricAcid);
    formData.append('residualSugar', inputResidualSugar);
    formData.append('chlorides', inputChlorides);
    formData.append('freeSulfurDioxide', inputFreeSulfurDioxide);
    formData.append('totalSulfurDioxide', inputTotalSulfurDioxide);
    formData.append('density', inputDensity);
    formData.append('ph', inputPh);
    formData.append('sulphates', inputSulphates);
    formData.append('alcohol', inputAlcohol);
    console.log(formData);

    let url = 'http://127.0.0.1:5000/vinho';
    fetch(url, {
        method: 'post',
        body: formData
    })
        .then((response) => response.json())
        .catch((error) => {
            console.error('Error:', error);
        });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
    let span = document.createElement("span");
    let txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
    let close = document.getElementsByClassName("close");
    let i;
    for (i = 0; i < close.length; i++) {
        close[i].onclick = function () {
            let div = this.parentElement.parentElement;
            const nomeItem = div.getElementsByTagName('td')[0].innerHTML
            if (confirm("Você tem certeza?")) {
                div.remove()
                deleteItem(nomeItem)
                alert("Removido!")
            }
        }
    }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (name) => {
    console.log(name);
    let url = 'http://127.0.0.1:5000/vinho?name=' + name;
    fetch(url, {
        method: 'delete'
    })
        .then((response) => response.json())
        .catch((error) => {
            console.error('Error:', error);
        });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item  
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
    let inputName = document.getElementById("newName").value;
    let inputFixedAcitidy = document.getElementById("newFixedAcidity").value;
    let inputVolatileAcidity = document.getElementById("newVolatileAcidity").value;
    let inputCitricAcid = document.getElementById("newCitricAcid").value;
    let inputResidualSugar = document.getElementById("newResidualSugar").value;
    let inputChlorides = document.getElementById("newChlorides").value;
    let inputFreeSulfurDioxide = document.getElementById("newFreeSulfurDioxide").value;
    let inputTotalSulfurDioxide = document.getElementById("newTotalSulfurDioxide").value;
    let inputDensity = document.getElementById("newDensity").value;
    let inputPh = document.getElementById("newPh").value;
    let inputSulphates = document.getElementById("newSulphates").value;
    let inputAlcohol = document.getElementById("newAlcohol").value;

    const checkUrl = `http://127.0.0.1:5000/vinhos?name=${inputName}`;
    fetch(checkUrl, {
        method: 'get'
    })
        .then((response) => response.json())
        .then((data) => {
            if (inputFixedAcitidy === '' || inputVolatileAcidity === '' || inputCitricAcid === '' || inputResidualSugar === '' || inputChlorides === '' ||
                inputFreeSulfurDioxide === '' || inputTotalSulfurDioxide === '' || inputDensity === '' || inputPh === '' || inputSulphates === '' || inputAlcohol === '') {
                alert("Os campos devem ser preenchidos.");
            } else if (isNaN(inputFixedAcitidy) || isNaN(inputVolatileAcidity) || isNaN(inputCitricAcid) || isNaN(inputResidualSugar) || isNaN(inputChlorides) ||
                isNaN(inputFreeSulfurDioxide) || isNaN(inputTotalSulfurDioxide) || isNaN(inputDensity) || isNaN(inputPh) || isNaN(inputSulphates) || isNaN(inputAlcohol)) {
                alert("Todos os campos precisam ser numéricos!");
            } else if (inputName === '') {
                    alert("O nome da amostra do vinho não pode ser vazio!");
            } else {
                insertList(inputName, inputFixedAcitidy, inputVolatileAcidity, inputCitricAcid, inputResidualSugar, inputChlorides, inputFreeSulfurDioxide, inputTotalSulfurDioxide, inputDensity, inputPh, inputSulphates, inputAlcohol);
                postItem(inputName, inputFixedAcitidy, inputVolatileAcidity, inputCitricAcid, inputResidualSugar, inputChlorides, inputFreeSulfurDioxide, inputTotalSulfurDioxide, inputDensity, inputPh, inputSulphates, inputAlcohol);
                alert("Vinho adicionado!");
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (name, fixedAcitidy, volatileAcidity, citricAcid, residualSugar, chlorides, freeSulfurDioxide, totalSulfurDioxide, density, ph, sulphates, alcohol, quality) => {
    var item = [name, fixedAcitidy, volatileAcidity, citricAcid, residualSugar, chlorides, freeSulfurDioxide, totalSulfurDioxide, density, ph, sulphates, alcohol, quality];
    var table = document.getElementById('myTable');
    var row = table.insertRow();

    for (var i = 0; i < item.length; i++) {
        var cell = row.insertCell(i);
        cell.textContent = item[i];
    }

    var deleteCell = row.insertCell(-1);
    insertDeleteButton(deleteCell);

    // DESFAZER COMENTÁRIOS
    // document.getElementById("newName").value = "";
    // document.getElementById("newFixedAcidity").value = "";
    // document.getElementById("newVolatileAcidity").value = "";
    // document.getElementById("newCitricAcid").value = "";
    // document.getElementById("newResidualSugar").value = "";
    // document.getElementById("newChlorides").value = "";
    // document.getElementById("newFreeSulfurDioxide").value = "";
    // document.getElementById("newTotalSulfurDioxide").value = "";
    // document.getElementById("newDensity").value = "";
    // document.getElementById("newPh").value = "";
    // document.getElementById("newSulphates").value = "";
    // document.getElementById("newAlcohol").value = "";

    removeElement();
}