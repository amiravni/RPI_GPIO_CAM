<?php 
require_once('./PHPMailer/class.phpmailer.php');
echo "Start... <br/>";
$myfile = fopen("TurnOn.txt", "w");
fclose($myfile);
echo "Waiting 5 seconds... <br/>";
sleep(5);

$bodytext = "Attached Output from Cam";
$email = new PHPMailer();
$email->From      = 'AmirPI@myPI.com';
$email->FromName  = 'AmirFromPI';
$email->Subject   = 'Video From Cam';
$email->Body      = $bodytext;
$email->AddAddress('amiravni83@gmail.com');

$file_to_attach = './output0.avi';

$email->AddAttachment( $file_to_attach , 'Caught.avi' );

 echo $email->Send() ? "Mail sent" : "Mail failed"; 
echo "end...";

//$command1 = escapeshellcmd("sudo /usr/bin/python /var/www/myInputSketch.py");
//$output = shell_exec($command1);
//echo $output;

?>

