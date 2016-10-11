import pytest
from threading import Thread
from background_worker import BackgroundWorker as background_worker

def test__thread_works_in_background():
    from time import sleep
    times = 5

    @background_worker(1)
    def t1(x, **kwargs):
        y=kwargs.get("y")
        x.append(1)
        y.append(1)
    _listx = []
    _listy = []
    t1(_listx, y=_listy)
    sleep(times)
    assert abs(len(_listx) - times) < 2
    assert abs(len(_listy) - times) < 2

