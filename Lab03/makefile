FILE_NAME := calculator_test.py
CACHE := ./__pycache__

.PHONY: clean

run:
	flake8 --max-line-length=127 $(FILE_NAME)
	python3 -m unittest -v $(FILE_NAME)

clean:
	@$(RM) -r $(CACHE)