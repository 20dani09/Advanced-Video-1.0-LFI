# Advanced-Video-1.0-LFI with HTTPS
## Advanced Video WordPress Plugin 1.0 - Local File Inclusion (LFI) Exploit
This repository contains a Python script that exploits a Local File Inclusion vulnerability in the WordPress Plugin Advanced Video version 1.0. This vulnerability allows an attacker to include files from the server, potentially leading to sensitive information exposure or remote code execution.

### Prerequisites
- Python 3.x
- urllib library

### Usage 

```bash
python3 39646.py
```

### How it Works

The Python script sends a malicious request to the WordPress site with the vulnerable plugin installed. It leverages the Local File Inclusion vulnerability to include sensitive files from the server. In this case, the /wp-config.php file is hidden within a randomly named JPEG image located at:

```bash
https://IP/wordpress/wp-content/uploads/[random_number].jpeg
```

To access the content, you can use the following curl command:

```bash
curl "https://IP/wordpress/wp-content/uploads/[random_number].jpeg" -k
```
Replace [random_number] with the specific random number generated for the JPEG image. The content of the wp-config.php file embedded in the JPEG image will be displayed in the terminal.


