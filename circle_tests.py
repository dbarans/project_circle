from circle import Circle

c1 = Circle(1)
c2 = Circle(2)
c3 = Circle()
c4 = Circle(3)


class TestEq:
    def test_eq(self):
        assert c1 == c3


class TestGt:
    def test_gt(self):
        assert c2 > c3
        assert c4 > c2


class TestLt:
    def test_lt(self):
        assert c2 < c4
        assert c1 < c2


class TestGe:
    def test_ge(self):
        assert c1 >= c3
        assert c2 >= c1


class TestLe:
    def test_lt(self):
        assert c2 <= c4
        assert c1 <= c3


class TestAdd:
    def test_add(self):
        assert c1 + c3 == 6.283185307179586
        assert c1 + c2 == 15.707963267948966
