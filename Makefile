all:
	./setup.py develop
	./setup.py extract_messages
	./setup.py update_catalog
	./setup.py compile_catalog

push: 
	tx push -stf --no-interactive
	tx pull -af
