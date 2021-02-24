<?php
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');

include('includes/header.inc.php');
?>

<h2 class="text-center text-uppercase font-weight-bold">Lost Items</h2>
<div class="row mt-5">
    <div class="col-sm-6">
        <div class="card">
          <h5 class="card-header">Open Ticket!</h5>
          <div class="card-body">
            <h5 class="card-title">New Lost item request</h5>
            <p class="card-text"> 
                Click the button to make a new lost item request.
                You will be updated about the status of your request.
            </p>
            <a href="ticket.php" class="btn btn-primary pull-right">Open Ticket</a>
          </div>
        </div>
    </div>
    <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Verify the status of your requests</h5>
            <p class="card-text"> 
                Click the button to show the list of your requests. The reviewed ones
                are listed as closed. 
            </p>
            <a href="list.php" class="btn btn-secondary pull-right">Go to the List</a>
          </div>
        </div>
    </div>
</div>
<div class="row mt-5">
    <div class="col-sm-12">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title mb-4 font-weight-bold">Lost Property Office</h5>
            <p>
                The lost-property service at Last Airport is managed by the in house Lost Property Office.
            </p>
            <p>
                The Office is <strong>open for the public</strong>, to pick up items, <strong>from 09:00 to 12:00 and from 15:00 to 18:00</strong>. The Airport Lost Property Office is in the “Arrivals” hall, on the ground floor.
            </p>
            <p>
                In some cases, lost property is managed by the Lost&Found offices of the airlines. In this case, we can provide you with their contact details.
            </p>
            <p>
                Enter lostpropertyhub to insert a new request or to check the status of previously inserted ones.
            </p>
            <p>
                A staff member will <strong>review</strong> your request and <strong>get in touch</strong> to provide more informations.
            </p>
        </div>
    </div>
    </div>
</div>

<?php 
include('includes/footer.inc.php');
?>
