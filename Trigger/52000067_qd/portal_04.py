""" trigger/52000067_qd/portal_04.xml """
from common import *
import state


#  포탈 파괴 연출 
class idle(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return portal()


class portal(state.State):
    def on_enter(self):
        create_monster(spawnIds=[804], arg2=True) # 포탈

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[804]):
            return portal_off()


class portal_off(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=104, script='$52000067_QD__PORTAL_04__0$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=105, script='$52000067_QD__PORTAL_04__1$', arg4=3, arg5=2)
        set_effect(triggerIds=[7013], visible=False) # 다크 포탈
        set_effect(triggerIds=[7113], visible=True) # 다크 포탈 폭발


