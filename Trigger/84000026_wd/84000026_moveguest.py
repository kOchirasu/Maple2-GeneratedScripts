""" trigger/84000026_wd/84000026_moveguest.xml """
from common import *
import state


class 초기화(state.State):
    def on_enter(self):
        set_user_value(key='Weddingceremonystartsready', value=0) # 초기화
        set_user_value(key='Weddingceremonyfail', value=0) # 초기화

    def on_tick(self) -> state.State:
        if true():
            return 시작()


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wedding_hall_state(hallState='weddingComplete'):
            return 종료()
        if user_value(key='Weddingceremonystartsready', value=1):
            set_user_value(key='Weddingceremonystartsready', value=0)
            return 새로운하객있는지감지()


class 새로운하객있는지감지(state.State):
    def on_tick(self) -> state.State:
        if wedding_hall_state(hallState='weddingComplete'):
            return 종료()
        if user_value(key='Weddingceremonyfail', value=1):
            set_user_value(key='Weddingceremonyfail', value=0)
            return 시작()
        if wait_tick(waitTick=1000):
            return 방금입장한하객은하객석으로위치이동()


class 방금입장한하객은하객석으로위치이동(state.State):
    def on_enter(self):
        wedding_move_user(entryType='Guest', mapId=84000026, portalIds=[22,23], boxId=701) # 799번 박스(입장구역)에 있는 하객들은 22,23번으로 랜덤이동

    def on_tick(self) -> state.State:
        if true():
            return 새로운하객있는지감지()


class 하객은버진로드밖으로위치이동(state.State):
    def on_enter(self):
        wedding_move_user(entryType='Guest', mapId=84000026, portalIds=[22,23], boxId=701) # 701번 박스(버진로드)에 있는 하객들은 22,23번으로 랜덤이동

    def on_tick(self) -> state.State:
        if true():
            return 새로운하객있는지감지()


class 종료(state.State):
    pass


