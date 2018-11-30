# coding=utf-8
import socket
import sys
import logging

sys.getdefaultencoding()
logging.basicConfig(format='%(levelname)s: %(message)s')


def G(s):
    return "%s[32;2m%s%s[0m" % (chr(27), s, chr(27))


def A(s):
    return "%s[36;2m%s%s[0m" % (chr(27), s, chr(27))


def R(s):
    return "%s[31;2m%s%s[0m" % (chr(27), s, chr(27))


def tcp_test(url, port):
    """abcd"""
    sk = socket.socket()
    sk.settimeout(1)
    url, port = sys.argv[1], sys.argv[2]
    try:
        sk.connect((url, int(port)))
    except Exception:
        return 'Server(%s) port %s ' % (url, port) + R('not connect!')
    sk.close()
    return 'Server(%s) port %s ' % (url, port) + G('OK!')


class RangeError(BaseException):
    pass


if __name__ == '__main__':
    opts = sys.argv
    if len(opts) == 1:
        print "Usage:\n  python tcp_test_test.py <url> <port>"
        exit()
    try:
        if len(opts) < 3:
            raise AttributeError('This script must take 2 param.')
        url = opts[1]
        port = int(opts[2])
        if not(1 <= port <= 65535):
            raise RangeError('Port must be in (1-65535).')
        result = tcp_test(url, port)
        print result
    except AttributeError as e:
        logging.error(e)
    except ValueError as e:
        logging.error('Port must be a number.')
    except RangeError as e:
        logging.error(e)
