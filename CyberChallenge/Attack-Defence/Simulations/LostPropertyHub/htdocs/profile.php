<?php
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');

if (!logged_in()) {
    header('Location: login.php');
}

include('includes/header.inc.php');

if (   isset($_POST['pwd']) 
    && isset($_POST['changepwd']) 
    && $_POST['pwd']!='' 
    && $_POST['changepwd']!='' 
    ){

  $db=db_connect();

  $stmt=$db->query("
    UPDATE Users SET pwd='".mysql_real_escape_string($_POST['pwd'])."' 
    WHERE idUser='".mysql_real_escape_string($_SESSION['idUser'])."'
  ");
  if(!$stmt){print_r($db->errorInfo());}
  $stmt->closeCursor();
  $_SESSION['pwd']=mysql_real_escape_string($_POST['pwd'])
  ?>
  <h2 class="text-center text-uppercase font-weight-bold">Profile</h2>  
  <div class="alert alert-success" role="alert">
    Password changed. 
    <br>
    Go to your
    <a href="profile.php" class="text-white font-weight-bold">profile.</a>
  </div>

  <?php

  include('includes/footer.inc.php');
  exit();
}


?>

<h2 class="text-center text-uppercase font-weight-bold">Profile</h2>

<div class="card">
  <h5 class="card-header bg-primary text-white">Profile fields <?php if ($_SESSION['isAdmin']==1) echo ' - Admin'?></h5>
  <div class="card-body">
     <div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="name">Name</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2 fa-user"></span> <?php echo htmlspecialchars($_SESSION['name'])?>
            </div>
          </div>
        </div>
        <div class="form-group col-md-6">
          <label for="pwd">Password</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2 fa-key"></span> <?php echo htmlspecialchars($_SESSION['pwd'])?>
            </div>
          </div>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="mail">E-Mail address</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2 fa-envelope"></span> <?php echo htmlspecialchars($_SESSION['mail'])?>
            </div>
          </div>
        </div>
        <div class="form-group col-md-6">
          <label for="tel">Telephone number</label>
          <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2 fa-phone"></span> <?php echo htmlspecialchars($_SESSION['tel'])?>
            </div>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="address">Address</label>
        <div class="card">
            <div class="card-body py-2 px-2">
              <span class="fa text-muted mr-2 fa-tag"></span> <?php echo htmlspecialchars($_SESSION['address'])?>
            </div>
          </div>
      </div>
      
    </div>
    
  </div>
</div>

<div class="card">
  <h5 class="card-header bg-primary text-white">Change password</h5>
  <div class="card-body">
  
  <form method="POST">
    <div class="form-group">
      <label for="inputPassword" class="">New Password</label>
      <input type="password" class="form-control" id="pwd" name="pwd" placeholder="Password">
      <input type="hidden" name="changepwd" value="yes">
    </div>
    <button type="submit" class="btn btn-primary mt-3">Change Password</button>
  </form>

  </div>
</div>

<?php 
include('includes/footer.inc.php');
?>
