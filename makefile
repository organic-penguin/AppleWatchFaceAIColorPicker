git: install_services add_to_repo git_files
local_web: install_services apache apache_files

install_services:
	@echo "Installing required backend services...."
	sudo apt-get update
	sudo apt-get install -y  python-opencv libatlas-base-dev libwebp-dev python python3 python3-pip libtiff5  libilmbase-dev libopenexr-dev libgstreamer1.0-dev libopenjp2-7
	yes | sudo pip3 install numpy opencv-python
	@echo "Backend services are complete"

add_to_repo:
	@echo "Changing GIT remote URL to your repository. If you have not edited this makefile with your repo URL do this now"
	git remote set-url origin <<<<<INSERT YOUR REPO URL HERE>>>>>>
	git rm --cached . -r
	git add openCVImage.png index.html
	git commit -m "Initial commit"
	git config credential.helper store
	@echo "Complete... your next 'git push origin' will save your credentials locally to allow it to continuouslly update your GitHub Pages site. If you did not previously setup your git global configs for email and user name you will need to do so and then re-commit and push before continuing"

apache:
	@echo "Installing Apache2 Web Server"
	sudo apt-get install -y apache2 libapache2-mod-php
	@echo "Modifying index.html to allow editing of index.html from the script. This will be set as all users can read/write/766"
	sudo chmod 766 /var/www/html/index.html
	@echo "Adding Apache user 'www-data' to sudoers no password required *Required for main.py to access the camera from web browser* 
	sudo echo 'www-data ALL=(ALL) NOPASSWD:ALL' | sudo tee -a  /etc/sudoers
	@echo "Apache2 configuration complete"

git_files:
	@echo "Moving the required python scripts relative to the GIT version to the main root folder"
	cp include/gitVersion.py main.py
	cp include/initializeButton.py initializeButton.py
	cp include/index.html index.html
	@echo "GIT files complete"

apache_files:
	@echo "Moving the required python script relative to the local Apache2 Web Server version to the main root folder"
	cp include/localWebVersion.py main.py
	@echo "Apache files complete"
