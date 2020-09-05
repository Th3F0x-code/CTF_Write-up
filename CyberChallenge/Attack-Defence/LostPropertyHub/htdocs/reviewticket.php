<?php
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');

if (!logged_in()) {
    header('Location: login.php');
}
if (!is_admin()) {
    header('Location: index.php');
    exit();
}

include('includes/header.inc.php');

if (   isset($_POST['review'])
    && isset($_POST['ticketid'])
    && $_POST['review']!=''
    && $_POST['ticketid']!=''
    && $_POST['review']==$_SESSION['idUser']) 
{
  $db=db_connect();

  $stmt=$db->query("
    UPDATE Tickets SET reviewed=1, revby='".mysql_real_escape_string($_SESSION['idUser'])."' 
    WHERE idTicket='".mysql_real_escape_string($_POST['ticketid'])."'  
  ");
  if(!$stmt){print_r($db->errorInfo());}
  $id=$db->lastInsertId();
  $stmt->closeCursor();

?>
  <h2 class="text-center text-uppercase font-weight-bold">Ticket Reviewed</h2>  
  <div class="alert alert-success" role="alert">
    Ticket reviewed, the ticket <?php echo $_POST['ticketid']; ?> is now closed. 
    <br>
    Go to the review
    <a href="review.php" class="text-white font-weight-bold">list.</a>
  </div>

  <?php

  include('includes/footer.inc.php');
  exit();  


}


if (   isset($_GET['id'])  
    && $_GET['id']!='' 
    ){

  $db=db_connect();
  $stmt=$db->query("
    SELECT * FROM Tickets WHERE idTicket=\"".mysql_real_escape_string($_GET['id'])."\"
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
<h2 class="text-center text-uppercase font-weight-bold">Review Ticket</h2>

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

<form method="POST">
    <input type="hidden" name="review" value="<?php echo $_SESSION['idUser']?>">
    <input type="hidden" name="ticketid" value="<?php echo $tick['idTicket']?>">
    <button type="submit" class="btn btn-primary mt-3 pull-right">Close Ticket</button>
</form>

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
