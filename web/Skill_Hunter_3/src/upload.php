<?php
if (isset($_GET["source"])) {
    die(highlight_file(__FILE__));
}

session_start();

function generateRandomId($length = 20) {
    return bin2hex(random_bytes($length));
}

if (!isset($_SESSION["id"])) {
    $_SESSION["id"] = generateRandomId();
}

$random = $_SESSION["id"];
$dir = 'uploads/' . $random;

if (!is_dir($dir)) {
    mkdir($dir, 0777, true);
}

$disallowed_ext = array(
    "php",
    "php3",
    "php4",
    "php5",
    "php7",
    "pht",
    "phtm",
    "phtml",
    "phar",
    "phps",
);

if (isset($_FILES['file'])) {
    if ($_FILES['file']['error'] !== UPLOAD_ERR_OK) {
        die("Upload failed");
    }

    $name = $_FILES['file']['name'];
    $temp_path = $_FILES['file']['tmp_name'];
    $path = $dir . '/' . $name;

    // Check file extension
    $parts = pathinfo($name);
    $ext = $parts['extension'];

    if (in_array($ext, $disallowed_ext, true)) {
        die("Invalid file type");
    }

    // Check filename
    if (empty($parts['filename']) || empty($parts['extension'])) {
        die("Invalid filename");
    }

    // Check content
    $image = file_get_contents($temp_path);
    if (mb_strpos($image, "<?") !== FALSE) {
        die("PHP code not allowed in image.");
    }

    // Check if the uploaded file is an image using exif_imagetype
    if (!exif_imagetype($temp_path)) {
        die("Not an image.");
    }

    // Move the uploaded file to the destination directory
    if (move_uploaded_file($temp_path, $path)) {
        echo '<!DOCTYPE html><html>
<head>
<title>Skill Hunter</title>
</head>
<body>
<div class="align-middle well">
<div class="container my-5 px-4">
    <h3>Thief book</h3>
    <p>The NEN ability is successfully stolen... You can find it at this page <a href="' . $path . '">here</a></p>
</div>
</div>
</body>
</html>';
    } else {
        die("File upload failed");
    }
} else {
    echo "No file sent";
}
?>
