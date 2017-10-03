#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from pybuilder.core import use_plugin, init, Author, task
import os


use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("exec")
use_plugin('python.pycharm')
# use_plugin("python.stdeb")
use_plugin("python.sphinx")
use_plugin("python.pdoc")

name = "configAWSEnv"
summary = "An extensible, easy to use continuous build tool for Python"
description = """PyBuilder is a build automation tool for python.
PyBuilder is a software build tool written in pure Python which mainly targets Python applications.
It is based on the concept of dependency based programming but also comes along with powerful plugin mechanism that
allows the construction of build life cycles similar to those known from other famous build tools like Apache Maven.
"""

authors = [Author("Ittiel", "ittiel@gmail.com")]
url = "http://some utl"
license = "Apache License"
packages=["configAWSEnv"]



# Dependencies
RUNTIME_DEPENDENCIES = [
    'boto3==1.4.7',
    'argparse==1.4.0'
]

BUILD_DEPENDENCIES = [
]

@init
def set_properties(project, logger):

    project.version = "0.0.1"

    # Set project dependencies
    for dependency in RUNTIME_DEPENDENCIES:
        project.depends_on(dependency)

    for dependency in BUILD_DEPENDENCIES:
        project.build_depends_on(dependency)

    # get running environments (Jenkins r local on developer machine)
    # branch is required
    if (os.getenv("pybuilder_environment")) == 'jenkins':
        pass
        # project.default_task = ["clean", "git_checkout", "prepare", "tk_unit_test", "analyze",
        #                        'tk_sonar',  "package", 'upload', "git_commit"]
    else:
        # do not release or commit changes on local builds
        logger.warn("LOCAL Environment")
        logger.warn("=================")
        logger.warn("Important: The build steps for local builds are different then the Jenkins steps")
        project.default_task = ["clean", "prepare",  "analyze", "package"]
    project.build_depends_on('setuptools')
    # project.build_depends_on('stdeb')
    project.set_property("verbose", True)

    # Coverage properties
    project.set_property("coverage_break_build", False)
    project.set_property("coverage_threshold_warn", 70)

    project.set_property('dir_source_unittest_python', 'src/unittest/')
    project.set_property('unittest_module_glob', '*.py')

    # Enable debug output for unit tests
    project.set_property("run_unit_tests_propagate_stdout", True)
    project.set_property("run_unit_tests_propagate_stderr", True)
    project.set_property("dir_target", "target")
    project.set_property("dir_source_main_python", "src/main/python/")

    #doc site
    project.include_file("pybuilder", "LICENSE")
    project.set_property("pdoc_module_name", "configAWSEnv")

    # Package
    # dist = "target/dist/{}-{}".format(project.name, project.version)
    # project.set_property("dir_dist", dist)
    # project.set_property('distutils_commands', ['bdist'])
    # project.set_property('distutils_commands', ['sdist'])
    project.set_property('distutils_use_setuptools', True)
    project.set_property("dir_dist_scripts", 'scripts')
    # project.set_property("distutils_console_scripts", ["configAWSEnv_ = pybuilder.cli:main"])
    project.set_property("distutils_entry_points", {'console_scripts': ["configAWSEnv=configAWSEnv:config_ec2_env.main"]})
    project.set_property("distutils_classifiers", [
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'])


    # Release property
    project.set_property("distutils_upload_repository", "http://pypi.repo.infra.taykey.com")
