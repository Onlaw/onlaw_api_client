.PHONY: pypiprod pypitest build_wheel


build_wheel:
	python3 setup.py sdist sdist bdist_wheel

clean_dist_folder:
	rm -rf dist/*

pypiprod: clean_dist_folder build_wheel	
	python3 -m twine upload --repository-url https://pypi.org/legacy/ dist/onlaw_api_client* 

pypitest: clean_dist_folder build_wheel	
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/onlaw_api_client*

