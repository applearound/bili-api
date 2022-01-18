import unittest

from bili_api.reply.reply_api import bv_to_av, get_replies


class TestReply(unittest.TestCase):
    def test_bv_to_av(self):
        av = bv_to_av("BV1gr4y1D7Nf")
        self.assertEqual(764745872, av, 'av not equal')

    def test_get_replies(self):
        av = bv_to_av("BV1gr4y1D7Nf")
        replies = get_replies(av)
        print(replies)


if __name__ == "__main__":
    unittest.main()
