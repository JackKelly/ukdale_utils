from __future__ import print_function
import os
import errno
import glob
import datetime


def get_unix_timestamp(filename):
    """Convert FLAC filename to unix timestamp.

    Arguments
    ---------
    filename : str
        e.g. 'vi-1363702740_859492.flac'

    Returns
    -------
    timestamp : float
    """
    split_a = filename.split('-')
    split_b = split_a[1].split('.')
    timestamp_str = split_b[0].replace('_', '.')
    return float(timestamp_str)


def mkdir_p(path):
    """Replicates mkdir -p.
    From http://stackoverflow.com/a/600612
    """
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


filenames = glob.glob('*.flac')
n = len(filenames)


for i, filename in enumerate(filenames):
    print('{:05d}/{:d}'.format(i, n), end=' ')

    timestamp = get_unix_timestamp(filename)
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    year, week, _ = dt.isocalendar()

    # Format string for new directory
    year = str(year)
    week = 'wk{:02d}'.format(week)
    new_dir = os.path.join(year, week)
    new_filename = os.path.join(new_dir, filename)

    print(filename, new_filename)
    mkdir_p(new_dir)
    os.rename(filename, new_filename)
