.PHONY: run-example

run-example:
	@if [ -z "$(SCRIPT)" ]; then \
		echo "Usage: make run-example SCRIPT=examples/path/to/script.py"; \
		exit 1; \
	fi
	PYTHONPATH=. python $(SCRIPT)

# Example usage: make run-example SCRIPT=examples/code-generation/code-explanation-detailed.py
