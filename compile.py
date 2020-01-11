from jinja2 import Template, Environment, FileSystemLoader
from pathlib import Path
import glob, sys

config = {
    "template_base_dir": "templates/",
    "html_base_dir": "docs"
}


def render_templates():
    environment = Environment(loader=FileSystemLoader(config['template_base_dir']))

    for template_file in Path(config['template_base_dir']).rglob("*.html"):
        template_relative_path = template_file.relative_to(config['template_base_dir'])
        output_path = Path(config['html_base_dir']) / template_relative_path

        print(f'Compiling {template_relative_path} to {output_path}')
   
        template = environment.get_template(str(template_relative_path))

        # generer le texte du template
        rendered_template_text = template.render()

        # ecrire le texte du template sur disque
        output_path.write_text(rendered_template_text, encoding='utf8')


def main():
    render_templates()


main()
