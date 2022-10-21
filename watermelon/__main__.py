from pathlib import Path

from watermelon.event.event import create_event, finish_event, remove_event, list_event, watermelon, list_achievement

def run(options):
    BASEDIR = Path(__file__).parent
    config = BASEDIR / 'resources' / 'db.json'

    if options.new_event is not None:
        create_event(config, options.new_event)

    if options.finish_event is not None:
        finish_event(config, options.finish_event)

    if options.remove_event is not None:
        remove_event(config, options.remove_event)

    if options.list_event is not None:
        list_event(config, options.list_event)

    if options.work is not None:
        watermelon(config, options.work)

    if options.list_achive is not None:
        list_achievement(config, options.list_achive)


def main():
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option('-n', dest='new_event', action='store', default=None,
                      help='create a event with priority like [name:priority]')
    parser.add_option('-f', dest='finish_event', action='store', default=None,
                      help='finish a event by name')
    parser.add_option('-r', dest='remove_event', action='store', default=None,
                      help='remove a event by name')
    parser.add_option('-l', dest='list_event', action='store', default=None,
                      help='list event [day｜week|month|year]')
    parser.add_option('-g', dest='work', action='store', default=None,
                      help='start a timer with [work_time:rest_time:event_name]')
    parser.add_option('-a', dest='list_achive', action='store', default=None,
                      help='list achievement [day|week|month|year]')

    options, args = parser.parse_args()

    try:
        run(options)
    except Exception as e:
        print(f'Watermelon quit unexpectedly: {e}')

        

if __name__ == '__main__':
    main()
    
