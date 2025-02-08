#!/usr/bin/env zsh

echo "###########Running all the tests###########"
pytest -s

echo "###########Running the tests marked as smoke###########"
pytest -m smoke

echo "###########Checking test coverage###########"
pytest --cov

echo "###########Running the tests in parallel###########"
pytest -n 4
