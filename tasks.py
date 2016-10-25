#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from invoke import task, run

docs_dir = 'docs'
build_dir = os.path.join(docs_dir, '_build')


@task
def clean(ctx, bytecode=True, extra=''):
    patterns = []
    patterns.append('dist')
    patterns.append('*.egg*')

    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        run("rm -rf %s" % pattern)


@task(pre=[clean])
def build(ctx):
    run("python setup.py build && python setup.py egg_info")
    run("python setup.py sdist bdist_wheel")


@task
def pep8(ctx):
    run("pycodestyle --first --count --config=setup.cfg **/*.py")


@task(pre=[pep8, clean])
def test(ctx):
    run("python run_tests.py")


@task
def publish(pre=[build]):
    run("twine upload dist/*")


@task
def register(pre=[build]):
    run("twine register dist/retexto-1.0-py2.py3-none-any.whl")
    run("twine register dist/retexto-1.0.tar.gz")
