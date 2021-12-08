import context
from projpkg import eda

# Test we_need_to_talk()
def test_we_need_to_talk():

    res = eda.we_need_to_talk()
    assert res == 'I <3 U!'

    res = eda.we_need_to_talk(break_up=False)
    assert res == 'I <3 U!'

    res = eda.we_need_to_talk(break_up=True)
    assert res == "It's not you, it's me..."