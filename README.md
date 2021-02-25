# interop-scenarios-prototype

This project is intended to explore the possibilities of having one repository to
contain one to many interoperability scenarios.

*Currently today each scenario has its own dedicated repository*

## Examples

**Disclaimer**

All examples below have already created a Python virtual environment and have
activated it.

```shell
virtualenv -p /usr/bin/python3.6 venv
source venv/bin/activate
```

### Install product1_openshift scenario

```
(venv) $ export SCENARIO=product1_openshift
# local install
(venv) $ pip install .
-- or --
# http url install
(venv) $ pip install git+https://github.com/ryankwilliams/interop-scenarios-prototype.git@main
(venv) $ ls -l venv/
bin  lib  lib64  product1_openshift  pyvenv.cfg
(venv) $ ls venv/product1_openshift/
ansible  ansible.cfg  CHANGELOG.md  config  __init__.py  keys  __pycache__  teflo  teflo.cfg  template_def.json  template_vars.sh  tests  tools  vars
(venv) $ pip list product1-openshift
product1-openshift  1.0.0
(venv) $ pip list teflo
teflo               1.0.0
(venv) $ pip list | grep ansible
ansible             2.9.0
```

### Install product2_openshift scenario

```
(venv) $ export SCENARIO=product2_openshift
# local install
(venv) $ pip install .
-- or --
# http url install
(venv) $ pip install git+https://github.com/ryankwilliams/interop-scenarios-prototype.git@main
(venv) $ ls -l venv/
bin  lib  lib64  product2_openshift  pyvenv.cfg
(venv) $ ls venv/product2_openshift/
ansible  ansible.cfg  CHANGELOG.md  config  __init__.py  keys  __pycache__  teflo  teflo.cfg  template_def.json  template_vars.sh  tests  tools  vars
(venv) $ pip list product2-openshift
product1-openshift  0.1.0
(venv) $ pip list | grep teflo
teflo               1.0.1
```
