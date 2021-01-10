all: install_services add_to_repo
core: install_services

install_services:
	@echo "Service installation has not been generated"
	
add_to_repo:
	@echo "Creating new branch for your GitHub page... not completed yet"
	git remote set-url origin https://github.com/organic-penguin/Apple-Watch-Face-Color-Picker.git
	git rm --cached .
	git add openCVImage.png index.html
	rm .gitignore
	cp .gitignorePOST .gitignore
	git commit -m "Initial commit"
	git config credential.helper store
