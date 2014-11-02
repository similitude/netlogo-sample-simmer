from collections import OrderedDict
from operator import itemgetter
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to

from api.handler import build_clargs, COMMAND


def test_build_clargs():
    arg_dict = {
        '--a': None,
        '-b': 'cde',
        '-f': False,
        '-hello': 4.2,
        'world': 1,
        'zzz': '',
        # TODO(orlade): Handle quoting of strings with whitespace/symbols/lists.
    }
    items = arg_dict.items()
    items.sort(key=itemgetter(0))
    arg_dict = OrderedDict(items)

    expected = [COMMAND, '--a', '-b', 'cde', '-f', 'False', '-hello', '4.2',
                'world', '1', 'zzz']

    assert_that(build_clargs(arg_dict), equal_to(expected))