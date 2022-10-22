""" trigger/52000067_qd/portal_03.xml """
from common import *
import state


#  포탈 파괴 연출 
class idle(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return portal()


class portal(state.State):
    def on_enter(self):
        create_monster(spawnIds=[801], arg2=True) # 포탈

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[801]):
            return portal_off()


class portal_off(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=108, script='$52000067_QD__PORTAL_03__0$', arg4=3, arg5=1)
        set_conversation(type=1, spawnId=115, script='$52000067_QD__PORTAL_03__1$', arg4=3, arg5=1)
        set_effect(triggerIds=[7012], visible=False) # 다크 포탈
        set_effect(triggerIds=[7112], visible=True) # 다크 포탈 폭발


