""" trigger/52000067_qd/portal_05.xml """
from common import *
import state


#  포탈 파괴 연출 
class idle(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return portal()


class portal(state.State):
    def on_enter(self):
        create_monster(spawnIds=[802], arg2=True) # 포탈

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[802]):
            return portal_off()


class portal_off(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7014], visible=False) # 다크 포탈
        set_effect(triggerIds=[7114], visible=True) # 다크 포탈 폭발


