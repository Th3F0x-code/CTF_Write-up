<?php 
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');
if (logged_in()) header('Location: index.php');

if (isset($_POST['email']) && isset($_POST['password']) && $_POST['email']!='' && $_POST['password']!=''){

  $db=db_connect();

  $stmt=$db->query("
        SELECT * FROM Users 
        WHERE mail='".mysql_real_escape_string($_POST['email'])."' 
        AND pwd=\"".mysql_real_escape_string($_POST['password'])."\"");
  if(!$stmt){print_r($db->errorInfo());}
  $resp=$stmt->fetch();
  $stmt->closeCursor();
  if (count($resp,1)>1) {
    // login
    $_SESSION['idUser']=$resp['idUser'];
    $_SESSION['name']=$resp['name'];
    $_SESSION['pwd']=$resp['pwd'];
    $_SESSION['mail']=$resp['mail'];
    $_SESSION['tel']=$resp['tel'];
    $_SESSION['address']=$resp['address'];
    $_SESSION['isAdmin']=$resp['isAdmin'];
    header('Location: index.php');
  }else{
    $wrong=true;
  }
}

include('includes/header.inc.php');

?>
<h2 class="text-center text-uppercase font-weight-bold">Log in</h2>

<form class="form-signin" method="post">
  <label for="email" class="">Email address:</label>
  <input type="email" id="email" name="email" class="form-control" placeholder="Email address" required autofocus>
  <label for="password" class=" mt-3">Password:</label>
  <input type="password" id="password" name="password" class="form-control" placeholder="Password" required>

  <?php if ($wrong){ ?>
  <p class="mt-4 text-danger mb-0">Wrong credetials!</p>
  <?php } ?>
  
  <button class="btn btn-primary mt-4" type="submit">Sign in</button>
  <p class="text-muted mt-4"><a class="text-muted" href="register.php">or Register!</a></p>
</form>

<?php
include('includes/footer.inc.php');
?>