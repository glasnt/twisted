
from twisted.trial.unittest import SynchronousTestCase

from twisted.tubes.test.util import FakeFount, FakeDrain
from twisted.tubes.fan import Out



class FanOutTests(SynchronousTestCase):
    """
    Tests for L{twisted.tubes.fan.Out}
    """

    def test_fanOut(self):
        """

        """
        ff = FakeFount()
        fdA = FakeDrain()
        fdB = FakeDrain()

        out = Out()
        fountA = out.newFount()
        fountB = out.newFount()
        nothing = ff.flowTo(out.drain)
        self.assertIdentical(nothing, None)

        fountA.flowTo(fdA)
        fountB.flowTo(fdB)
        ff.drain.receive("foo")

        self.assertEquals(fdA.received, ["foo"])
        self.assertEquals(fdB.received, ["foo"])