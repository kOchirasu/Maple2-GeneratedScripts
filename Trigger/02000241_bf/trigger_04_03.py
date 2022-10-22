""" trigger/02000241_bf/trigger_04_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[306], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[707,708], visible=True)
        set_mesh(triggerIds=[309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324], visible=False)
        set_actor(triggerId=507, visible=True, initialSequence='Closed')
        set_actor(triggerId=508, visible=True, initialSequence='Closed')
        set_actor(triggerId=509, visible=True, initialSequence='Closed')
        set_actor(triggerId=510, visible=True, initialSequence='Closed')
        set_actor(triggerId=511, visible=True, initialSequence='Closed')
        set_actor(triggerId=512, visible=True, initialSequence='Closed')
        destroy_monster(spawnIds=[607,608,609,610,611,612])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[406]):
            return 버튼눌림()


class 버튼눌림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[306], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=509, visible=True, initialSequence='Opened')
        set_actor(triggerId=510, visible=True, initialSequence='Opened')
        create_monster(spawnIds=[609,610], arg2=False)
        move_npc(spawnId=609, patrolName='MS2PatrolData_609')
        move_npc(spawnId=610, patrolName='MS2PatrolData_610')


