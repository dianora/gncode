from jinja2 import Template, Environment, FileSystemLoader
from pathlib import Path
import glob, sys
from babel.support import Translations, Locale

config = {
    "template_base_dir": "templates/",
    "html_base_dir": "docs"
}

def gettext():
    pass 

def render_templates():
    for locale in ['fr',  'en']:
        environment = Environment(loader=FileSystemLoader(config['template_base_dir']), extensions=['jinja2.ext.i18n'])
        translation = Translations.load("translations", locales=[locale])
        print(translation)
        environment.install_gettext_translations(translation)

        locale_html_base_dir = Path(config['html_base_dir']) / locale

        for template_file in Path(config['template_base_dir']).rglob("*.html"):
            template_relative_path = template_file.relative_to(config['template_base_dir'])
            input_path = Path(config['template_base_dir']) / template_relative_path # for logging only
            output_path = locale_html_base_dir / template_relative_path

            if not output_path.parent.is_dir():
                output_path.parent.mkdir(parents=True)

            print(f'Compiling {input_path} to {output_path}')
    
            template = environment.get_template(str(template_relative_path.as_posix()))

            # generer le texte du template
            rendered_template_text = template.render({"lang": locale})

            # ecrire le texte du template sur disque
            output_path.write_text(rendered_template_text, encoding='utf8')


def main():
    render_templates()


main()
