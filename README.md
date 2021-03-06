# OpenSAFELY Research Template

This is a template repository for making new OpenSAFELY resarch projects.

## _Python Project Example_ ##

This repo is based on [the opensafely research project template](https://github.com/opensafely/research-template) but uses a Python analytics model instead of Stata or R

* Developers and epidemiologists interested in the framework should review [the OpenSAFELY documentation](https://docs.opensafely.org)

## About the OpenSAFELY framework ##

The OpenSAFELY framework is a secure analytics platform for
electronic health records research in the NHS.

Instead of requesting access for slices of patient data and
transporting them elsewhere for analysis, the framework supports
developing analytics against dummy data, and then running against the
real data *within the same infrastructure that the data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org).

## Getting Started ##

To use this example follow the [OpenSAFELY installation instructions](https://docs.opensafely.org/en/latest/install-intro/)

The available jobs and output are configured in `project.yaml`

You'll need Docker and to install the OpenSAFELY CLI - then you can execute:

```opensafely run run_model```

The Docker container will spin up and execute `analysis/pymodel.py` to output a log file in the `logs` directory and a Seaborn correlation heatmap in `output/plots` 
