{% if cookiecutter.command_line_interface|lower == 'fire' %}
import fire
{% endif %}

def hello_world() -> str:
    return "Hello, world!"


def run():
    print(hello_world())
{% if cookiecutter.command_line_interface|lower == 'fire' %}

if __name__ == '__main__':
    fire.Fire()
{% endif %}