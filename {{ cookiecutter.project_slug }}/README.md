# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

{% include "README.%s.jinja" % cookiecutter.packaging %}
## Publishing

The GitHub workflow includes an action to publish on release.
To run this action, uncomment the commented portion of `publish.yml`, and modify the steps for the desired behaviour (publishing a Docker image, publishing to PyPI, deploying documentation etc.)
