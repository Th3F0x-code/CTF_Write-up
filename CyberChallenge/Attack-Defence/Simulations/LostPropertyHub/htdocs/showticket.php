<?php
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');

if (!logged_in()) {
    header('Location: login.php');
}

include('includes/header.inc.php');

if (   isset($_GET['id'])  
    && $_GET['id']!='' 
    ){

  $db=db_connect();

  $stmt=$db->query("
    SELECT * FROM Tickets WHERE idTicket='".mysql_real_escape_string($_GET['id'])."'
  ");
  if(!$stmt){print_r($db->errorInfo());} 
  $tick=$stmt->fetch();
  $stmt->closeCursor();

  if (count($tick)==1) {
    ?>
    <h2 class="text-center text-uppercase font-weight-bold">Show Ticket</h2>
      <div class="alert alert-danger" role="alert">
      Ticket not found! 
      <br>
      Go to your
      <a href="list.php" class="text-white font-weight-bold">list.</a>
    </div>
<?php
  exit();
  }

  ?>

  <!-- show ticket here -->
<h2 class="text-center text-uppercase font-weight-bold">Show Ticket</h2>

<div class="card">
  <h5 class="card-header bg-primary text-white">Item description - <?php echo $tick['idTicket']?> </h5>
  <div class="card-body">
    
    <div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="type">Item type</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2">&#xf02b;</span> <?php echo htmlspecialchars($tick['type'])?>
            </div>
          </div>
        </div>
        <div class="form-group col-md-6">
          <label for="object">Object</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2">&#xf02b;</span> <?php echo htmlspecialchars($tick['object'])?>
            </div>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2">&#xf002;</span> <?php echo htmlspecialchars($tick['description'])?>
            </div>
          </div>
      </div>
      <div class="form-group">
        <label for="brand">Brand</label>
        <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2">&#xf024;</span> <?php echo htmlspecialchars($tick['brand'])?>
            </div>
          </div>
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="color">Color</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2">&#xf1fc;</span> <?php echo htmlspecialchars($tick['color'])?>
            </div>
          </div>
        </div>
        <div class="form-group col-md-6">
          <label for="details">Other details</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2">&#xf05a;</span> <?php echo htmlspecialchars($tick['details'])?>
            </div>
          </div>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="date">Date when it was lost</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2">&#xf133;</span> <?php echo htmlspecialchars($tick['date'])?>
            </div>
          </div>
        </div>
        <div class="form-group col-md-6">
          <label for="place">Place where it was lost</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2">&#xf1b9;</span> <?php echo htmlspecialchars($tick['place'])?>
            </div>
          </div>
        </div>
      </div>
</div>
<?php
  if ($tick['reviewed']==1){

    $stmt=$db->query("
      SELECT * FROM Users WHERE idUser='".htmlspecialchars($tick['revby'])."'
    ");
    if(!$stmt){print_r($db->errorInfo());}
    $reviewer=$stmt->fetch();
    $stmt->closeCursor();
    ?>
    <div class="alert alert-success mt-3 mb-1" role="alert">
      Your ticket has been reviewed by 
      <br>
      <?php 
      if($reviewer)
          echo htmlspecialchars($reviewer['name']).' - '.htmlspecialchars($reviewer['mail']);
      else
          echo "-<strong>The staff member that reviewed your ticket has been fired!</strong>-"
      ?> 
    </div>


    <?php
  }
?>

  </div>
</div>

  <?php

  include('includes/footer.inc.php');
  exit();
}


?>
<h2 class="text-center text-uppercase font-weight-bold">Show Ticket</h2>
<div class="alert alert-danger" role="alert">
  Ticket not specified! 
  <br>
  Go to your
  <a href="list.php" class="text-white font-weight-bold">list.</a>
</div>


<?php 
include('includes/footer.inc.php');
?>
