""" trigger/02100001_bf/05_getmusicbuff.xml """
from common import *
import state


#  아프렐라 오지 : 연주 시 특수 효과가 발동되는 패시브 버프 부여 
class Wait(state.State):
    def on_enter(self):
        set_user_value(key='GiveBuffSlowly', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return GiveBuff01()


#  시작 초반에 철창 문이 닫히기 전까지 1초마다 버프 지급 
class GiveBuff01(state.State):
    def on_enter(self):
        add_buff(boxIds=[9900], skillId=71000030, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GiveBuff01()
        if user_value(key='GiveBuffSlowly', value=1):
            return GiveBuff02()


#  철창문이 닫힌 이후에는 세이프 존에 유저를 감지하면 세이프 존에 있는 유저에게 버프 지급 
class GiveBuff02(state.State):
    def on_enter(self):
        add_buff(boxIds=[9901], skillId=71000030, level=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9901]):
            return GiveBuff02()
        if user_value(key='GiveBuffSlowly', value=2):
            return Quit()


#  플레이 제한 시간이 끝나면 버프 지급을 멈춤 
class Quit(state.State):
    def on_enter(self):
        add_buff(boxIds=[9900], skillId=71000034, level=1)


