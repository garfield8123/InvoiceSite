<!DOCTYPE html>
<html>
    <head>
        <title>Computer Zone - We do it all: Professional Computer Repair and Sales</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="./Scripts/index.css">
        <link rel="shortcut icon" href="./Images/ComputerZoneLogo.gif">
        <script src="./Scripts/index.js"></script>
    </head>
    <body>
        <nav class="navbar navbar-expand-md navbar-custom fixed-top">
            <li class="navbar-brand"><a href="/"><img src="./Images/ComputerZoneLogo.gif" alt="Computer Zone Logo"></a></li>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsenavbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="collapsenavbar">
                <ul class="navbar-nav">
                    <div class="dropdown show">
                        <a class="dropdown-toggle" href="./CreateStandardOrder" role="button" id="dropdownMenuLink" data-toggle="dropdown">
                            Create Work order
                        </a>
                        <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                            <a class="dropdown-item" href="/CreateMobileOrder">Mobile Work Order</a>
                            <a class="dropdown-item" href="/CreateStandardOrder">Standard/PC Work Order</a>
                        </div>
                    </div>
                    <li class="nav-item">
                        <a class="nav-link" href="/CreateSaleOrder">Create Sale Order</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/InvoiceList">List of Work Orders</a>
                    </li>
                </ul>
            </div>
        </nav>
        <h2 class="gap"></h2>
        <div class="row">
            <div class="col-md-12" align="Center">
                <form method="POST" action="./CreatedInvoice">
                    {{!InvoiceTitle}}
                    <label>Employee: </label>
                    <input name="EmployeeName" placeholder="Employee Name" required>
                    <label>Date Created: </label>
                    <input name="CreatedDate" type="date" required><br>
                    <h3>Customer Information</h3>
                    <Label>Customer Name:</Label>
                    <input name="customerName" placeholder="Customer Name" required> 
                    <Label>Customer Email: </Label>
                    <input type="email" name="customerEmail" placeholder="customer@email.com"> <br>
                    {{!PhoneNumber}}
                    <label>Customer Phone Number: </label>
                    <input type="tel" name="CustomerPhoneNumber" placeholder="831-123-1122"> <br>
                    <h3>System Information</h3>
                    {{!ServicePassword}}
                    <label>Trouble Reported: </label>
                    <input type="text" name="TroubleReported" placeholder="System turns on, but display turns black" required>
                    <h3>Equipment Turned In</h3>
                    <div class="table-responsive">
                        <table class="EquipmentTable">
                            <thead>
                                <tr>
                                    <th scope="col">Column #</th>
                                    <th scope="col">Equipment Name: </th>
                                    <th scope="col">Serial Number</th>
                                </tr>
                            </thead>
                        </table>
                    </div>
                    <a class="btn rounded-0 btn-block" id="insertEquipmentRow">Add New Row</a>
                   
                    <h3>Invoice Breakdown: </h3>
                    <div class="table-responsive">
                        <table class="Invoicetable">
                            <thead>
                                <tr>
                                    <th scope="col">Column #</th>
                                    <th scope="col">Quantity: </th>
                                    <th scope="col">Item Description: </th>
                                    <th scope="col">Price</th>
                                </tr>
                            </thead>
                        </table>
                    </div>
                    <a class="btn rounded-0 btn-block" id="insertInvoiceRow">Add New Row</a><br>
                    <div class="row">
                        <div class="col-md-4">
                        </div>
                        <div class="col-md-4 center">
                            <label>Payment Type: </label>
                            <select id="paymentType" name="paymentType">
                                <option value="Cash" name="Cash">Cash</option>
                                <option value="Credit/Debit" name="Credit/Debit">Credit/Debit</option>
                                <option value="Check" name="Check">Check</option>
                            </select><br>
                            <label>Labor Totel: </label>
                            <input type="number" name="NumberofHours" placeholder="1"> HRS
                            $ <input type="number" name="LaborCost" placeholder="99"> <br>
                            <label>Diagnostics/Trip Fee: </label>
                            $ <input type="number" name="DiagnosticsFee" placeholder="20"> <br>
                            <label>Parts Total: </label>
                            $ <input type="number" name="PartCost" placeholder="20"> <br>
                            <label>Subtotal (No tax): </label>
                            $ <input type="number" name="SubTotalNoTax" placeholder="199"> <br>
                            <label>Discount ? : </label>
                            $ <input type="number" name="DiscountCost" placeholder="20"> <br>
                            <label>Tax (9.25%): </label>
                            $ <input type="number" name="TaxCost" placeholder="10"> <br>
                            <label>Total W/ Tax: </label>
                            $ <input type="number" name="TotalCost" placeholder="215"> <br>
                            <label> Owe: </label>
                            $ <input type="number" name="AmountOwe" placeholder="100"> <br>
                            <input id="login" class="button" type="submit" value="Submit"> 
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </body>
    <footer>
        <div class="row">
            <div class="col-md-4" align="Center">
                <h2>Hours (Mission)</h2> <br>
                <p>M-F: 10am - 7pm</p>
                <p>Sat: 10am - 4pm</p>
                <p>Sun: By Appointment</p>
            </div>
            <div class="col-md-4" align="Center">
                <h2>Telephone</h2> <br>
                <p> Mission Street: </p> <br>
                <a href="tel: 831-466-9099"><p>(831) 466-9099</p></a><br>
                <p>Laurel Street: </p> <br>
                <a href="tel:831-466-9065"><p>(831) 466-9065</p></a>
            </div>
            <div class="col-md-4" align="Center">
                <h2>Email</h2>
                <a href="mailto:surplus@computerzone1.com">surplus@computerzone1.com</a>
            </div>
        </div>
    </footer>
</html>