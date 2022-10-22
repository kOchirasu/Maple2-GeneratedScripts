""" trigger/02000545_bf/egg2.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702], jobCode=0):
            return 아르키아체력()


class 아르키아체력(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=30, spawnId=102, isRelative=True):
            return 알메쉬생성()


class 알메쉬생성(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23300010, illust='ArakiaDark_normal', duration=4000, script='$02000545_BF__EGG2__0$')
        set_mesh(triggerIds=[2150,2151], visible=True)
        create_monster(spawnIds=[505,507], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[505]):
            return 알파괴1()
        if monster_dead(boxIds=[507]):
            return 알파괴2()
        if monster_dead(boxIds=[505,507]):
            return 종료()


class 알파괴1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2150], visible=False)
        set_ai_extra_data(key='phase', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[507]):
            return 알파괴2()
        if monster_dead(boxIds=[505,507]):
            return 종료()


class 알파괴2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2151], visible=False)
        set_ai_extra_data(key='phase', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[505]):
            return 알파괴1()
        if monster_dead(boxIds=[505,507]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2150,2151], visible=False)


