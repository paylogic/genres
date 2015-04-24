requirements:
	pip install -r make_requirements.txt
all: requirements

	./setup.py develop
	jsonchecker src/paylogic_genres.json
	python scripts/check_json.py src/paylogic_genres.json
	./setup.py extract_messages
	./setup.py update_catalog
	./setup.py compile_catalog
	./setup.py export_json

pull: requirements
	tx pull -af

push: requirements
	tx push -stf --no-interactive

test: requirements
	jsonchecker src/paylogic_genres.json
	python scripts/check_json.py src/paylogic_genres.json