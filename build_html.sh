# Build .mo file from .po for Persian (Farsi) language
msgfmt ./locale/fa/LC_MESSAGES/index.po -o ./locale/fa/LC_MESSAGES/index.mo
# Make html files using sphinx-build
make html
