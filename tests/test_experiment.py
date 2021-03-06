import os
import re
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to
from api.experiment import Experiment
from api.handler import NetLogoServiceHandler


def test_experiment():
    exp = Experiment(steps=42, params={'bar': 'baz'}, name='Quxperiment')
    exp.add_metric(color='foo')

    with open('tests/experiment-fixture.xml') as fixture:
        assert_that(re.sub(r'\s+', '', exp.to_xml()),
                    equal_to(re.sub(r'\s+', '', fixture.read())))


def test_altruism():
    """
    Performs a full system test, invoking a local instance of NetLogo.

    Set environment variable CI=true in continuous integration to skip.
    """
    # Do not run system tests for continuous integration.
    if os.environ.get('CI'): # pragma: no cover
        return

    result = NetLogoServiceHandler().altruism(0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 100)
    assert_that(len(result.splitlines()), equal_to(108))