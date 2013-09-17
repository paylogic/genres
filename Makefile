all:
	pip install -r make_requirements.txt
	./setup.py develop
	./setup.py extract_messages
	./setup.py update_catalog
	./setup.py compile_catalog
	./setup.py export_json

pull:
	tx pull -af

push: 
	tx push -stf --no-interactive
