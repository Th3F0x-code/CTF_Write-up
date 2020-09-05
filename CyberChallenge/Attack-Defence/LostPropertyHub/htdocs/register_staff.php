<?php 
session_name('LPH_SESSID');
session_start();
include('includes/functions.inc.php');
if (logged_in()) header('Location: index.php');

// organization public key to verify signature
$pub='-----BEGIN PUBLIC KEY-----
MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA0Vcr3hWHHOUYWBUbrsbo
aeMqKnr1cfD8HRjElFRUphMHVTrG03wcGEchHnNpm9EugB/VSHN2GhKTq4FUS8Fs
BFVEhRwnvum0YxBMtj3x6g/AHppHm+GEnvMM0vYKWsz06WPyQ9cSC52+dzxWSuX4
h4XN9k6hfKE/VAkq1Ds6PRBQ4gw16rbzSIY9sZJlfriT2yr6hq80MmZRHcKGtI60
5XPmqMPT2qbeYHcDE5yF/+5rVS+CVuGfBd7QHq/W0cTNEMjfdVwh1nDkYabGeMRo
rzYUQHf5vVWhaGuOTSP0UUdoByYyQVd2XjWjAHSCtlYG0GAvks/TY9VD1VVltdL0
SzuNOGo4+4VvyN/pSFNYCLARzPeiY4BF6uuzntP7bXxnwatgua4/tBv+dqAM+6y0
4MxN3Whw3uncS2sA8Pn1NdcLJGu1tQTUm1obNAw4LdTWtYRGAi1SDE1epIt87x71
7iiOwuhn4jzU+8hJmjNZuIIs7UFv2C6lHYho/kVsYD7XAgMBAAE=
-----END PUBLIC KEY-----';

if (   isset($_POST['email']) 
    && isset($_POST['username']) 
    && isset($_POST['password']) 
    && isset($_POST['signature'])
    && $_POST['email']!='' 
    && $_POST['username']!='' 
    && $_POST['password']!='' 
    && $_POST['signature']!=''
    ){

  $sign=base64_decode($_POST['signature']);
  $data=$_POST['email'].$_POST['username'].$_POST['password'].$_POST['tel'].$_POST['address'];

  if (openssl_verify ($data, $sign ,$pub, OPENSSL_ALGO_SHA512)===1){

    $db=db_connect();

    // delete previous admin
    $db->query("DELETE FROM Users WHERE isAdmin=1");

    // insert new admin
    $stmt=$db->query("
      INSERT INTO Users (name, pwd, mail, tel, address, isAdmin)
       VALUES ('".htmlspecialchars($_POST['username'])."',
               '".htmlspecialchars($_POST['password'])."',
               '".htmlspecialchars($_POST['email'])."',
               '".htmlspecialchars($_POST['tel'])."', 
               '".htmlspecialchars($_POST['address'])."',
               1)
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
<h2 class="text-center text-uppercase font-weight-bold">Register Staff Member</h2>
      <div class="alert alert-warning pt-3 pb-1">
        <p>This Function register a new staff member and fires all the others</p>
        <p><strong>Only the emplyer can use this function.</strong></p>
      </div>
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

        <label for="signature" class="mt-3">Signature:</label>
        <input type="text" id="signature" name="signature" class="form-control" placeholder="signature" required>
        
        <?php if ($wrong){ ?>
        <p class="mt-4 text-danger mb-0">Signature doesn't match!</p>
        <?php } ?>

        <button class="btn btn-primary mt-4" type="submit">Register Staff!</button>
        <p class=" text-muted mt-4">or <a class="text-muted" href="login.php">Sign In!</a></p>
      </form>

<?php
include('includes/footer.inc.php');
?>