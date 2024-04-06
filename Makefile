.POSIX:
.SILENT:

.PHONY: all $(MAKECMDGOALS)

SORT ?= no

.check_defined:
ifndef FILE
	echo "FILE variable is not defined"
	exit 1
endif

run: .check_defined
	python main.py $(FILE) $(SORT)

run_container: .check_defined
	docker run --rm -v $(PWD):/opt/app -w /opt/app -e PYTHON_PATH=/opt/app \
		docker.io/library/python:3.6-slim \
		python main.py $(FILE) $(SORT)

test:
	find . \
		-wholename "./test/wordlists/*.txt" \
		-exec $(MAKE) run FILE={} \;

test_container:
	find . \
		-wholename "./test/wordlists/*.txt" \
		-exec $(MAKE) run_container FILE={} \;

generate:
	python ./test/scripts/generate_wordlists.py ./test/wordlists
