$(function () {
    var invoiceCounter = 1;
    $("#insertInvoiceRow").on("click", function (event) {
        event.preventDefault();
        var newRow = $("<tr>");
        var cols = '';
        cols += '<th scope="row">' + invoiceCounter + '</th>';
        cols += '<td><input class="form-control rounded-0" type="number" name="Quantity" placeholder="1"></td>';
        cols += '<td><input class="form-control rounded-0" type="text" name="ItemDescription" placeholder="1 hour of Labor"></td>';
        cols += '<td>$<input class="form-control rounded-0" type="number" name="price" placeholder="99"></td>';
        cols += '<td><button class="btn btn-danger rounded-0 deleteRow"><i class="bi bi-trash"></i></button></td>';
        newRow.append(cols);
        $(".Invoicetable").append(newRow);
        invoiceCounter++;
    });

    var equipmentCounter = 1;
    $("#insertEquipmentRow").on("click", function (event) {
        event.preventDefault();
        var newRow = $("<tr>");
        var cols = '';
        cols += '<th scope="row">' + equipmentCounter + '</th>';
        cols += '<td><input class="form-control rounded-0" type="text" name="EquipmentName" placeholder="Equipment Name"></td>';
        cols += '<td><input class="form-control rounded-0" type="text" name="SerialNumber" placeholder="Serial Number"></td>';
        cols += '<td><button class="btn btn-danger rounded-0 deleteRow"><i class="bi bi-trash"></i></button></td>';
        newRow.append(cols);
        $(".EquipmentTable").append(newRow);
        equipmentCounter++;
    });

    $("table").on("click", ".deleteRow", function (event) {
        $(this).closest("tr").remove();
        if ($(this).closest("table").hasClass("Invoicetable")) {
            invoiceCounter--;
        } else if ($(this).closest("table").hasClass("EquipmentTable")) {
            equipmentCounter--;
        }
    });
});