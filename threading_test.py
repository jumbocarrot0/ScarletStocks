from threading import Thread


def foo(bar, result):
    print('hello {0}'.format(bar))
    result.append("foo")


results = []
threads = Thread(target=foo, args=('world!', results))

# threads.append()
threads.start()

# do some other stuff

# threads[-1].join()

print(results)
