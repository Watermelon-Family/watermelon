import pytest as pytest

from watermelon.event.utils import create


def return_file_name():
    return '/Users/bytedance/projects/py_programs/watermelon/watermelon/resources/db.json'

def return_test_data():
    return [
        [return_file_name(),
         'test',
         5]
    ]

@pytest.mark.parametrize("filename,event_name,priority",return_test_data())
def test_create(filename, event_name, priority):
    create(filename, event_name, priority)