from sorter import Sorter

def test_ascend():
    # test ascending array of numbers
    input = [3, 4, 2, 1]
    sorter = Sorter("list 1")
    sorter.set_array(input)
    assert sorter.get_ascending() == [1, 2, 3, 4]
    
def test_ascend_with_duplicates():
    # test ascending with duplicaes
    input = [3, 4, 2, 1, 1, 1]
    sorter = Sorter("list 1")
    sorter.set_array(input)
    
    # commented out because it hangs
    assert False
    # assert sorter.get_ascending() == [1, 1, 1, 2, 3, 4]