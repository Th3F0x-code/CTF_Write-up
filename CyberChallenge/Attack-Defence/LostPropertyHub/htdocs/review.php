<?php
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');

if (!logged_in()) {
    header('Location: login.php');
}

if (is_admin()!==true) {
    header('Location: index.php');
}

include('includes/header.inc.php');

$db=db_connect();

$stmt=$db->query("
  SELECT * FROM Tickets WHERE reviewed=0
");

if(!$stmt){print_r($db->errorInfo());}
$tickets=$stmt->fetchall();
$stmt->closeCursor();


?>

<h2 class="text-center text-uppercase font-weight-bold">Tickets to review</h2>

<h4>Tickets review list</h4>
<div class="list-group">
  <?php 
  if (count($tickets)==0){
    echo "<li class=\"list-group-item text-muted\">- no data -</li>";
  }else{
    foreach ($tickets as $tick) {
      echo '<a href="reviewticket.php?id='.$tick['idTicket'].'" class="list-group-item list-group-item-action">'.$tick['idTicket'].' - '.htmlspecialchars($tick['object']).'</a>';
    }
  ?>
  <?php } ?>
</div>



<?php 
include('includes/footer.inc.php');
?>
