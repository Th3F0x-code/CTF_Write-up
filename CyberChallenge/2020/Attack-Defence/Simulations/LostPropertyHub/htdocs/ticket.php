<?php
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');

if (!logged_in()) {
    header('Location: login.php');
}

include('includes/header.inc.php');

if (   isset($_POST['type']) 
    && isset($_POST['object']) 
    && isset($_POST['description']) 
    && isset($_POST['brand'])
    && isset($_POST['color'])
    && isset($_POST['details'])
    && isset($_POST['date'])
    && isset($_POST['place']) 
    && $_POST['type']!='' 
    && $_POST['object']!='' 
    && $_POST['description']!='' 
    && $_POST['date']!=''
    ){

  $db=db_connect();

  $stmt=$db->query("
    INSERT INTO Tickets (type, object, description, brand, color, details, date, place, userId)
    VALUES (     
             '".htmlspecialchars($_POST['type'])."', 
             '".htmlspecialchars($_POST['object'])."', 
             '".htmlspecialchars($_POST['description'])."', 
             '".htmlspecialchars($_POST['brand'])."', 
             '".htmlspecialchars($_POST['color'])."', 
             '".htmlspecialchars($_POST['details'])."', 
             '".htmlspecialchars($_POST['date'])."', 
             '".htmlspecialchars($_POST['place'])."', 
             '".htmlspecialchars($_SESSION['idUser'])."'
    )
  ");
  if(!$stmt){print_r($db->errorInfo());}
  $id=$db->lastInsertId();
  $stmt->closeCursor();

  ?>
  <h2 class="text-center text-uppercase font-weight-bold">New ticket</h2>  
  <div class="alert alert-success" role="alert">
    Ticket inserted, your ticket has number <?php echo $id; ?>. 
    <br>
    Go to your
    <a href="list.php" class="text-white font-weight-bold">list.</a>
  </div>

  <?php

  include('includes/footer.inc.php');
  exit();
}


?>

<h2 class="text-center text-uppercase font-weight-bold">New ticket</h2>

<div class="card">
  <h5 class="card-header bg-primary text-white">Item description</h5>
  <div class="card-body">
    
    <form method="POST">
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="type">Item type</label>
          <input type="text" class="form-control fa" id="type" name="type" placeholder="&#xf02b;  Type">
        </div>
        <div class="form-group col-md-6">
          <label for="object">Object</label>
          <input type="text" class="form-control fa" id="object" name="object" placeholder="&#xf02b;  Object">
        </div>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <input type="text" class="form-control fa" id="description" name="description" placeholder="&#xF002;  Description">
      </div>
      <div class="form-group">
        <label for="brand">Brand</label>
        <input type="text" class="form-control fa" id="brand" name="brand" placeholder="&#xF024;  Brand">
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="color">Color</label>
          <input type="text" class="form-control fa" id="color" name="color" placeholder="&#xF1FC;  Color">
        </div>
        <div class="form-group col-md-6">
          <label for="details">Other details</label>
          <input type="text" class="form-control fa" id="details" name="details" placeholder="&#xF05A;  Details">
        </div>
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="date">Date when it was lost</label>
          <input type="date" class="form-control fa" id="date" name="date">
        </div>
        <div class="form-group col-md-6">
          <label for="place">Place where it was lost</label>
          <input type="text" class="form-control fa" id="place" name="place" placeholder="&#xF1B9;  Place">
        </div>
      </div>
      
      <button type="submit" class="btn btn-primary mt-3">Send ticket</button>
</form>


  </div>
</div>

<?php 
include('includes/footer.inc.php');
?>
