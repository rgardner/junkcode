import pytest

import gitnetcode


@pytest.mark.parametrize('line,expected', [
    (' 8 files changed, 247 insertions(+), 135 deletions(-)', 112),
    (' 1 file changed, 22 insertions(+)', 22),
    (' 1 file changed, 2 deletions(-)', -2),
])
def test_calcnetlines_whencalled_iscorrect(line, expected):
    result = gitnetcode.calc_net_lines(line)
    assert result == expected
