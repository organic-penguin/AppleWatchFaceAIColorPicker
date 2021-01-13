all: install_services add_to_repo
core: install_services

install_services:
	@echo "Service installation has not been generated"
	sudo apt-get update
	sudo apt-get install -y  python-opencv libatlas-base-dev libwebp-dev python python3 python3-pip libtiff5  libilmbase-dev libopenexr-dev libgstreamer1.0-dev libopenjp2-7
	yes | pip3 install numpy opencv-python

add_to_repo:
	@echo "Creating new branch for your GitHub page... not completed yet"
	git remote set-url origin <ENTER YOUR GITHUB REPO URL HERE>
	git rm --cached . -r
	rm .gitignore
	cp .gitignorePOST .gitignore
	git add openCVImage.png index.html
	git commit -m "Initial commit"
	git config credential.helper store
	@echo "Complete... your next 'git push origin' will save your credentials locally to allow it to continuouslly update your GitHub Pages site"
