from square import Square

s1 = Square(1)
s2 = Square(2)
s3 = Square(1)
s4 = Square(3)


class TestEq:
    def test_eq(self):
        assert s1 == s3


class TestGt:
    def test_gt(self):
        assert s2 > s3
        assert s4 > s2


class TestLt:
    def test_lt(self):
        assert s2 < s4
        assert s1 < s2


class TestGe:
    def test_ge(self):
        assert s1 >= s3
        assert s2 >= s1


class TestLe:
    def test_lt(self):
        assert s2 <= s4
        assert s1 <= s3


class TestAdd:
    def test_add(self):
        assert s1 + s3 == 2
        assert s1 + s2 == 5
