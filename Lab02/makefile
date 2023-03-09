FILE_NAME := app_test.py
CACHE := ./__pycache__

.PHONY: clean

run:
	@python3 -m unittest $(FILE_NAME) 2>/dev/null
	@python3 -m unittest $(FILE_NAME) -b -v

clean:
	@$(RM) -r $(CACHE)