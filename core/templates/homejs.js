document.addEventListener('DOMContentLoaded', function () {
    let productName = '';

    document.querySelector('.form-select').onchange = function () {
        productName = this.value;
    }
    document.querySelector('#saveProduct').onclick = () => {

        const productBatch = document.querySelector('#batchNumber').value;
        const productExpireDate = document.querySelector('#expireDateSelected').value;
        const productQuantity = document.querySelector('#quantitySet').value;
        let newProduct = new Object()
        newProduct.name = productName;
        newProduct.batch = productBatch;
        newProduct.expireDate = productExpireDate;
        newProduct.quantity = productQuantity;

        let tbodyRef = document.getElementById('productsTable').getElementsByTagName('tbody')[0];

        let newRow = tbodyRef.insertRow();

        let productBatchCell = newRow.insertCell();
        let productNameCell = newRow.insertCell();
        let productExpireDateCell = newRow.insertCell();
        let productQuantityCell = newRow.insertCell();
        let inButtonCell = newRow.insertCell();
        let outButtonCell = newRow.insertCell();

        let productNameText = document.createTextNode(newProduct.name);
        let productBatchText = document.createTextNode(newProduct.batch);
        let productExpireDateText = document.createTextNode(newProduct.expireDate);
        let productQuantityText = document.createTextNode(newProduct.quantity);

        productNameCell.appendChild(productNameText);
        productBatchCell.appendChild(productBatchText);
        productExpireDateCell.appendChild(productExpireDateText);
        productQuantityCell.appendChild(productQuantityText);
        inButtonCell.innerHTML = '<td class="centered-row"><i class="bi bi-plus-circle text-success"></i></td>';
        outButtonCell.innerHTML = '<td class="centered-row"><i class="bi bi-dash-circle text-danger"></i></td>';

    };
})