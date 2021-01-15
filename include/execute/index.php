<html>
	<head>
		<title>Executing</title>
	</head>
	<body>
		<?php
		//Receive input from delete image form with picture path
		$output = exec('sh /var/www/html/execute/execute.sh', $output, $return_code);
		echo "<pre>$output</pre>";

		?>
		<?php
		//Allows for 5 seconds on page before redirect back to index.php
		header("Refresh: 5; url=/");

		?>
</html>
