<!DOCTYPE html>
<html>
<head>
    <title>LostPropertyHub</title>
    <meta charset="utf-8">
    <!-- Latest compiled and minified CSS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="includes/bootstrap_yeti.min.css">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN"
        crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="includes/style.css">

</head>
<body>
<nav class="navbar navbar-light navbar-expand-lg mb-3 headershadow">
    <div class="container"> <!-- container --> 
    
    <a href="/" class="navbar-brand" style="font-size: 22px">
        <span class="text-primary">Last</span>Airport
        <small class="ml-3 text-muted">
        <span class="text-primary">L</span>ost<span class="text-primary">P</span>roperty<span class="text-primary">H</span>ub
        </small>
    </a>
    
    <!-- <div class="collapse navbar-collapse"> -->
    <div>
    <?php if (logged_in()){ ?>
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="logout.php"><span class="fa fa-lg fa-sign-out"></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="profile.php"><span class="fa fa-lg fa-user"></a>
      </li>
    </ul>
    <?php } else { ?>
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="login.php"><span class="fa fa-lg fa-sign-in"></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="register.php"><span class="fa fa-lg fa-user-plus"></a>
      </li>
    </ul>
    <?php } ?>
    </div>

    
    </div> <!-- container -->
</nav>
<div class="container"> <!-- container --> 
