<?php 
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');
if (logged_in()) header('Location: index.php');

if (   isset($_POST['email']) 
    && isset($_POST['username']) 
    && isset($_POST['password']) 
    && isset($_POST['verifypassword']) 
    && $_POST['email']!='' 
    && $_POST['username']!='' 
    && $_POST['password']!='' 
    && $_POST['verifypassword']!=''
    ){

  if ($_POST['password']===$_POST['verifypassword']){

    $db=db_connect();

    $stmt=$db->query("
      INSERT INTO Users (name, pwd, mail, tel, address)
       VALUES ('".htmlspecialchars($_POST['username'])."',
               '".htmlspecialchars($_POST['password'])."',
               '".htmlspecialchars($_POST['email'])."',
               '".htmlspecialchars($_POST['tel'])."', 
               '".htmlspecialchars($_POST['address'])."')
    ");
    if(!$stmt){print_r($db->errorInfo());}
    $id=$db->lastInsertId();
    $stmt->closeCursor();

    header('Location: login.php');

  } else {
      $wrong=true;
  }
}

include('includes/header.inc.php');

?>
<h2 class="text-center text-uppercase font-weight-bold">Register</h2>

      <form class="form-signin" method="post">        
        <label for="email" class="">Email address:</label>
        <input type="email" id="email" name="email" class="form-control" placeholder="Email address" required autofocus>

        <label for="username" class="mt-3">Username:</label>
        <input type="text" id="username" name="username" class="form-control" placeholder="Username" required>

        <label for="bio" class="mt-3">Telephone number:</label>
        <input type="text" id="tel" name="tel" class="form-control" placeholder="Telephone">

        <label for="bio" class="mt-3">Address:</label>
        <input type="text" id="address" name="address" class="form-control" placeholder="Address">
        
        <label for="password" class="mt-3">Password:</label>
        <input type="password" id="password" name="password" class="form-control" placeholder="Password" required>
        
        <label for="verifypassword" class="mt-3">Verify Password:</label>
        <input type="password" id="verifypassword" name="verifypassword" class="form-control" placeholder="Verify Password" required>
        
        <?php if ($wrong){ ?>
        <p class="mt-4 text-danger mb-0">Passwords don't match!</p>
        <?php } ?>

        <button class="btn btn-primary mt-4" type="submit">Register!</button>
        <p class=" text-muted mt-4">or <a class="text-muted" href="login.php">Sign In!</a></p>
      </form>

<?php
include('includes/footer.inc.php');
?>