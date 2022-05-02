from figure import Triangle

t1 = Triangle(1)
t2 = Triangle(2)
t3 = Triangle(1)
t4 = Triangle(3)


class TestEq:
    def test_eq(self):
        assert t1 == t3


class TestGt:
    def test_gt(self):
        assert t2 > t3
        assert t4 > t2


class TestLt:
    def test_lt(self):
        assert t2 < t4
        assert t1 < t2


class TestGe:
    def test_ge(self):
        assert t1 >= t3
        assert t2 >= t1


class TestLe:
    def test_lt(self):
        assert t2 <= t4
        assert t1 <= t3


class TestAdd:
    def test_add(self):
        assert t1 + t3 == 1
        assert t1 + t2 == 2.5
