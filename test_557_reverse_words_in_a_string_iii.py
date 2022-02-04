import code_557_reverse_words_in_a_string_iii as c1

def test_example_1():
    s = c1.Solution()
    assert s.reverseWords("Let\'s take LeetCode contest") == "s\'teL ekat edoCteeL tsetnoc"

def test_example_2():
    s = c1.Solution()
    assert s.reverseWords("God Ding") == "doG gniD"