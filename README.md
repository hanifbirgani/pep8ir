# Persian PEP 8

This project is a continuous deployment pipeline for translating the [Python PEP 8](https://www.python.org/dev/peps/pep-0008/) to the Persian language and auto-deploy the translated version to [pep8.ir](https://pep8.ir)

## Contributing

Contributions are always welcome!
- To improve translations, use the [Transifex service](https://www.transifex.com/persian-peps/persian-pep8/).
- To make improvements in [pep8.ir](https://pep8.ir) website template use this GitHub repository.

## Continuous Deployment Pipeline

1. We use the [Transifex service](https://www.transifex.com/persian-peps/persian-pep8/) to translate original PEP 8 strings to the Persian language.
2. A GitHub workflow runs every 12 hours to pull new translations and merge updated translation files to the `main` branch of this repository.
3. The [Cloudflare Pages](https://pages.cloudflare.com/) build script runs automatically on every pull-request merge on the main branch, makes the output html files using the [Sphinx](https://www.sphinx-doc.org/), and deploys them to the [pep8.ir](https://pep8.ir).

## Build

To build the project locally, run the commands below:

1. Install python requirements:
```
pip install -r requirements.txt
```

2. Make html files:

```
./build_html.sh
```
  
## Author
- [Hanif Birgani](https://www.github.com/hanifbirgani)



<div dir="rtl">

# مشارکت در پروژه
ما از هر گونه مشارکت در پروژه استقبال می‌کنیم :)
- برای مشارکت در ترجمه پروژه به [مخزن ترجمه‌ها در سایت Transifex](https://www.transifex.com/persian-peps/persian-pep8/) مراجعه کنید. پیشنهاد می‌کنیم از نام کاربری مشابه با نام کاربری گیتهاب خود استفاده کنید.
- پس از انجام تغییرات در ترجمه و تایید شدن آن توسط ویرایشگران، برای افزودن نام خود به مشارکت‌کنندگان، فایل `CONTRIBUTORS.rst` را مطابق الگوی موجود ویرایش و نام خود را به آن اضافه کنید. سپس با ایجاد یک پول‌ریکوئست تغییرات را به مخزن گیتهاب بفرستید.
- برای ایجاد بهبود و تغییرات در ظاهر سایت [pep8.ir](https://pep8.ir) در همین مخزن گیتهاب مسائل را مطرح کنید.
</div>
