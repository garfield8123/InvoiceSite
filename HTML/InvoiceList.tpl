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
        <link rel="stylesheet" href="../Scripts/index.css">
        <link rel="shortcut icon" href="../Images/ComputerZoneLogo.gif">
    </head>
    <body>
        <nav class="navbar navbar-expand-md navbar-custom fixed-top">
            <li class="navbar-brand"><a href="/"><img src="../Images/ComputerZoneLogo.gif" alt="Computer Zone Logo"></a></li>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsenavbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="collapsenavbar">
                <ul class="navbar-nav">
                    <div class="dropdown show">
                        <a class="dropdown-toggle" href="/CreateStandardOrder" role="button" id="dropdownMenuLink" data-toggle="dropdown">
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
        <div class="col-md-12 passwordInput" align="center">
            {{!InvoiceTable}}
        </div>
    </body>
</html>