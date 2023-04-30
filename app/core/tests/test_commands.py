"""
Test custom Django custom commands.
"""

from unittest.mock import patch
# we mock the behavior of the the DB, we simulate the reponse of the DB

from psycopg2 import OperationalError as Psycopg2Error
# OperationalError is one fo the error we may encounter when we run a service before a DB is ready!.

from django.core.management import call_command
from django.db.utils import OperationalError
# Gives info about the init step of the DB (a bit like OperationalError above) 

from django.test import SimpleTestCase


# Looks cryptic but lookt at filesystem ;)
# btw "Command" (in) base class that is inherited in "Command" class in 
# wait_for_db for db func has a check method...
# We basically mock that check ethod to simulate the response (throwing an Exception or not)
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """
    Test commands.
    """

    def test_wait_for_db_ready(self, patched_check):
        """
        Test waiting for db if db ready.
        """
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    # order of the damn decorator arguments are not intuitive so check this out:
    """
    https://www.udemy.com/course/django-python-advanced/learn/lecture/32238844#overview
    (Video 40 in section 8: config DB)
    """
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep ,patched_check):
        """Test waiting for db when getting OperationalError"""
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        # 2 * 3 = 6 (see above): if it's more than 6 then test fails.

        patched_check.assert_called_with(databases=['default'])


"""
We need to mock the Sleep method now!

And here preicely we see the obvious advantage of mocking.
Instead of really sleeping, we go directly to the next process. 
We don't want to wait in our unittest. So we add another patch.
"""