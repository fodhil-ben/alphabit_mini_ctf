<?php
session_start();

if (isset($_FILES['file'])) {
    if ($_FILES['file']['size'] < 5000) {
        if (isset($_SESSION['id'])) 
            $random = $_SESSION['id'];
        else {
            $random = bin2hex(random_bytes(16));
            $_SESSION['id'] = $random;
        }

        $dir = 'uploads/' . $random; 
        if (!is_dir($dir)) 
            mkdir($dir, 0777, true);

        $name = $_FILES['file']['name'];
        $temp_path = $_FILES['file']['tmp_name'];
        $path = $dir .'/'. $name;

        // Check if the uploaded file is an image using exif_imagetype
        if (exif_imagetype($temp_path)) {
            if (move_uploaded_file($temp_path, $path)) {
                echo '<!DOCTYPE html><html>
<head>
<title>Skill Hunter</title>
</head>
<body>
<div class="align-middle well">
<div class="container my-5 px-4">
    <h3>Thief book</h3>
    <p>the NEN ability is successfully stolen... You can find it at this page <a href="'. $path . '">here</a></p>
</div>
</div>
</body>
</html> ';
            }
        } else {
            die("the Ability is not a valid image.");
        }
    } else {
        die("Ability is too large, the book is meant for small abilities only");
    }
}
else {
    echo "No file sent";
}
?>
