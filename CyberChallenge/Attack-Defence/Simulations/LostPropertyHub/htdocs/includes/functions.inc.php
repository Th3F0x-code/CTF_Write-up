<?php

require_once('config.inc.php');

function db_connect() {
    global $db_params;
    try {
        $dbh = new PDO("mysql:host=".$db_params["host"].";dbname=".$db_params["database"],
                       $db_params["user"], $db_params["password"]);
        $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, 0);
        $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch(PDOException $e) {
        echo 'Connection failed: ' . $e->getMessage();
        exit;
    }
    return $dbh;
}

function logged_in(){
    if (isset($_SESSION['name']) && $_SESSION['name']!="")
        return true;
    else
        return false;
}

function is_admin(){
    if (isset($_SESSION['isAdmin']) && $_SESSION['isAdmin']==1)
        return true;
    else
        return flase;
}

function mysql_real_escape_string($query){
    return preg_replace("/'/", "\'", $query);
}

// disable warnings
error_reporting(E_ALL ^ E_NOTICE ^ E_WARNING);

// set session expiration to 60 second with gc probability 10%
ini_set('session.gc_probability', 1);
ini_set('session.gc_divisor', 10);
ini_set('session.gc_maxlifetime', 60);


?>
