all: install_services add_to_repo
core: install_services

install_services:
	@echo "Service installation has not been generated"

add_to_repo:
        @echo "Creating new branch for your GitHub page... not completed yet"
        git remote set-url origin https://github.com/organic-penguin/Apple-Wa$
        git rm --cached . -r
        rm .gitignore
        cp .gitignorePOST .gitignore
        git add openCVImage.png index.html
        git commit -m "Initial commit"
        git config credential.helper store
	@echo "Complete... your next 'git push origin' will save your credentials locally to allow it to continuouslly update your GitHub Pages site"
