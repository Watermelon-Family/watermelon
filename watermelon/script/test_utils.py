import pytest as pytest

from watermelon.__main__ import get_resource
from watermelon.event.utils import create


def return_file_name():
    return get_resource()

def return_test_data():
    return [
        [return_file_name(),
         'test',
         5]
    ]

@pytest.mark.parametrize("filename,event_name,priority",return_test_data())
def test_create(filename, event_name, priority):
    create(filename, event_name, priority)