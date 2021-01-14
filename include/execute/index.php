<html>
	<head>
		<title>Executing</title>
	</head>
	<body>
		<?php
		//Receive input from delete image form with picture path
		echo "Test";
//		$message = exec("python3 /var/www/html/execute/main.py 2>&1");
//		$message = system("/user/lib/cgi-bin/main.py");
//		print_r($message);

		$output = exec('sh /var/www/html/execute/execute.sh', $output, $return_code);

//		$output = system('/usr/bin/python3 /home/pi/AppleWatchFaceAIColorPicker/test.py');
		//execute script that delete image with the image path 
		echo "<pre>$output</pre>";

		?>
		<?php
		//Allows for 1 second on page before redirect back to index.php
//		header("Refresh: 10; url=/");

		?>
</html>
