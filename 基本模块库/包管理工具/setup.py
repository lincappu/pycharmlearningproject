# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from distutils.core import setup
# 根包发布：根目录本身就是一个包，所以也有 init 文件，根包的packages=['']就是这个，表示是指定目录的全部文件。
setup(
	name='foobar',
	version='0.1',
	author='fls',
	author_email='lincappu@163.com',
	packages=[''],
	package_dir={'':'src'}
)


# 包发布：packages=['foobar'],执行包的名称，如果模板名和包名不是同一个，还要执行packages_dir 来指定路径
setup(
	name='foobar2',
	version='0.1',
	author='fls',
	author_email='lincappu@163.com',
	packages=['foobar'],
	package_dir={'foobar':'src'}
)


'''包发布（包存在于根目录）或者你想把包放在发布根目录，如：
&lt;root>/
        setup.py
        __init__.py
        foo.py
        bar.py
这种情况下你的setu脚本将会是：
'''
setup(name='foobar',
	version='1.0',
	package_dir={'foobar': ''},
	packages=['foobar'],
)
#（空字符串同样也代表当前目录)



'''包发布（多子包）
如果你有多个子包，它们必须被显在地列举在packages参数中，但是其他任何在package_dir参数中的实体自动扩展到子包。（换句话说，Distutils并不浏览你的源文件树（source tree），而是通过寻找__init__.py文件来计算相应Python包的目录。）因此，如果默认的层次有一个子包：

&lt;root>/
        setup.py
        foobar/
            __init__.py
            foo.py
            bar.py
            subfoo/
                __init__.py
                blah.py
那么相应的setup脚本将会是：
'''

setup(name='foobar',
	version='1.0',
	packages=['foobar', 'foobar.subfoo'],
	)

'''注意：发布一个包，就是将该包所在目录所有模块全部发布。那么我们就不能只发布包内部分模块。例如，文件结构如下：
&lt;root>/
        setup.py
        sub_package1/
            __init__.py
            sub_model1
            sub_model2
        sub_package2/
            __init__.py
            sub_model3
使用Distutils，我们无法在发布包sub_packe1和sub_package2的同时，不发布sub_model2模块.
'''



# 完整标准的例子
"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name='sampleproject',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/guides/single-sourcing-package-version/
    version='2.0.0',  # Required

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description='A sample Python project',  # Optional

    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional

    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)

    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url='https://github.com/pypa/sampleproject',  # Optional

    # This should be your name or the name of the organization which owns the
    # project.
    author='A. Random Developer',  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='author@example.com',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a list of additional keywords, separated
    # by commas, to be used to assist searching for the distribution in a
    # larger catalog.
    keywords='sample, setuptools, development',  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={'': 'src'},  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where='src'),  # Required

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='>=3.6, <4',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    # 安装当前模块需要的包
    install_requires=[
		'redis>=2.10.5', # 例子

	],  # Optional

	# setup.py本身需要依赖的包，这通常是为一些setuptools的插件准备的配置
	setup_require=[],

	#  仅在测试时需要使用的依赖，在正常发布的代码中是没有用的。，在执行python setup.py test时，可以自动安装这三个库，确保测试的正常运行。
	tests_require=[
        'pytest>=3.3.1',
        'pytest-cov>=2.5.1',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={  # Optional
        'sample': ['package_data.dat'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'sample=sample:main',
        ],
    },

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
    },
)