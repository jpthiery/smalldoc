# Copyright 2021 Jean-Pascal Thiery
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Allow to write the dict generated by parser using Jinja as template render.
"""
from jinja2 import Template


def write(module: dict) -> str:
    """
    Now, allow to generate a single page documentation in markdown using the only on Jinja template available.
    The dictionary should be generated by parser.
    :param module: The dict of your module generated by parser.
    :return: A single page markdown representation of your documentation
    :rtype str
    """
    with open('smalldoc/onepage.md.jinja', 'r') as template_file:
        template = Template(template_file.read())
        return template.render(module=module)
