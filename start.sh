curl -s https://raw.githubusercontent.com/python/peps/master/pep-0008.txt > _pep8.rst
make gettext
sphinx-intl update -p _build/gettext/ -l fa
make html