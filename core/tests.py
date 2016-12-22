import datetime

from django.test import TestCase
from freezegun import freeze_time

from .models import Transaction, Party


class TransactionTestCase(TestCase):
    def setUp(self):
        global INA
        INA = Party.objects.create(name="INA")

    @freeze_time("2016-12-19-00-00")
    def test_today_date(self):
        """
        Tests if a Transaction carried out today has a correct date.
        """
        t = Transaction.objects.create(party=INA, description="First receipt")
        self.assertEqual(t.invoice_date, datetime.datetime.now())

    @freeze_time("2017-01-01")
    def test_january(self):
        """
        Tests if a Transaction carried out on Jan 1st 2017 has a default start
        date of 2017-01-01 and a default end date of 2016-01-31.
        """
        t = Transaction.objects.create(party=INA, description="Second receipt")
        self.assertEqual(t.start_date, datetime.datetime(2017, 1, 1))
        self.assertEqual(t.end_date, datetime.datetime(2017, 1, 31))

    @freeze_time("2016-02-29")
    def test_february(self):
        """
        Tests if a Transaction carried out on Feb 29th 2016 has a default start
        date of 2016-02-01 and a default end date of 2016-02-29.
        """
        t = Transaction.objects.create(party=INA, description="Fourth receipt")
        self.assertEqual(t.start_date, datetime.datetime(2016, 2, 1))
        self.assertEqual(t.end_date, datetime.datetime(2016, 2, 29))
