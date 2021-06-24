# Fetch latest pep8 document
curl -s https://raw.githubusercontent.com/python/peps/master/pep-0008.txt > _pep8.rst
# Generate .pot catalogue from downloaded pep document
make gettext
# Update .po files for Persian (Farsi) language
sphinx-intl update -p _build/gettext/ -l fa
# Push updated files to the Transifex.com service
# tx push --source
