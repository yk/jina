from pathlib import Path

from jina.optimizers.parameters import (
    IntegerParameter,
    FloatParameter,
    LogUniformParameter,
    UniformParameter,
    CategoricalParameter,
    DiscreteUniformParameter,
    load_optimization_parameters,
)

import pytest


cur_dir = Path(__file__).parent

arg_dict = [
    (
        IntegerParameter,
        {
            'executor_name': 'executor',
            'low': 0,
            'high': 10,
            'step_size': 1,
            'log': False,
            'parameter_name': 'dummy_param',
        },
        {
            'name': 'JINA_EXECUTOR_DUMMY_PARAM',
            'low': 0,
            'high': 10,
            'step': 1,
            'log': False,
        },
    ),
    (
        FloatParameter,
        {
            'executor_name': 'executor',
            'low': 0,
            'high': 10,
            'step_size': 1,
            'log': False,
            'parameter_name': 'dummy_param',
        },
        {
            'name': 'JINA_EXECUTOR_DUMMY_PARAM',
            'low': 0,
            'high': 10,
            'step': 1,
            'log': False,
        },
    ),
    (
        UniformParameter,
        {
            'executor_name': 'executor',
            'low': 0,
            'high': 10,
            'parameter_name': 'dummy_param',
        },
        {
            'name': 'JINA_EXECUTOR_DUMMY_PARAM',
            'low': 0,
            'high': 10,
        },
    ),
    (
        LogUniformParameter,
        {
            'executor_name': 'executor',
            'low': 0,
            'high': 10,
            'parameter_name': 'dummy_param',
        },
        {
            'name': 'JINA_EXECUTOR_DUMMY_PARAM',
            'low': 0,
            'high': 10,
        },
    ),
    (
        CategoricalParameter,
        {
            'executor_name': 'executor',
            'choices': ['a', 'b'],
            'parameter_name': 'dummy_param',
        },
        {
            'name': 'JINA_EXECUTOR_DUMMY_PARAM',
            'choices': ['a', 'b'],
        },
    ),
    (
        DiscreteUniformParameter,
        {
            'executor_name': 'executor',
            'low': 0,
            'high': 10,
            'q': 0.1,
            'parameter_name': 'dummy_param',
        },
        {'name': 'JINA_EXECUTOR_DUMMY_PARAM', 'low': 0, 'high': 10, 'q': 0.1},
    ),
]


@pytest.mark.parametrize('paramter_class, inputs, outputs', arg_dict)
def test_parameters(paramter_class, inputs, outputs):
    param = paramter_class(**inputs)
    assert param.to_optuna_args() == outputs


def test_parameter_file_loading():
    load_optimization_parameters(cur_dir / 'parameters.yml')