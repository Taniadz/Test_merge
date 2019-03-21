from max_row.max_row import max_rating_row


class TestMaxRow:

    def test_one(self):
        assert(max_rating_row([1]) == 1)

    def test_none(self):
        assert(max_rating_row([15]) == 0)


    def test_two(self):
        assert(max_rating_row([1, 15]) == 1)

    def test_end_true(self):
        assert(max_rating_row([11, 12, 13, 1, 2, 3]) == 3)

    def test_end_false(self):
        assert (max_rating_row([11, 12, 13, 1, 2, 3, 15]) == 3)

    def test_second_row_max(self):
        assert (max_rating_row([11, 12, 13, 1, 2, 3, 15, 1, 2, 3, 4]) == 4)

    def test_first_row_max(self):
        assert (max_rating_row([11, 12, 13, 1, 2, 3, 4, 5, 15, 1, 2, 3, 4]) == 5)


