<?php
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');

if (!logged_in()) {
    header('Location: login.php');
    exit();
}

include('includes/header.inc.php');

$db=db_connect();

$stmt=$db->query("
  SELECT * FROM Tickets WHERE userId=".mysql_real_escape_string($_SESSION['idUser'])."
");
if(!$stmt){print_r($db->errorInfo());}
$tickets=$stmt->fetchall();
$stmt->closeCursor();


?>

<h2 class="text-center text-uppercase font-weight-bold">Your Tickets</h2>

<h4>Tickets list</h4>
<div class="list-group">
  <?php 
  if (count($tickets)==0){
    echo "<li class=\"list-group-item text-muted\">- no data -</li>";
  }else{
    foreach ($tickets as $tick) {
      if ($tick['reviewed']==1)
        echo '<a href="showticket.php?id='.$tick['idTicket'].'" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">'.$tick['idTicket'].' - '.htmlspecialchars($tick['object']).'<span class="badge badge-success badge-pill">Closed</span></a>';
      else
        echo '<a href="showticket.php?id='.$tick['idTicket'].'" class="list-group-item list-group-item-action">'.$tick['idTicket'].' - '.htmlspecialchars($tick['object']).'</a>';
    }
  ?>
  <?php } ?>
</div>



<?php 
include('includes/footer.inc.php');
?>
