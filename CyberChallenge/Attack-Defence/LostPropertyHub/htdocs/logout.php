<?php
session_name('LPH_SESSID');
session_start();
session_destroy();
header("Location: index.php");
exit;
?>