""" trigger/02000241_bf/trigger_01_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[701,702], visible=True)
        set_actor(triggerId=501, visible=True, initialSequence='Closed')
        set_actor(triggerId=502, visible=True, initialSequence='Closed')
        set_actor(triggerId=503, visible=True, initialSequence='Closed')
        set_actor(triggerId=504, visible=True, initialSequence='Closed')
        set_actor(triggerId=505, visible=True, initialSequence='Closed')
        set_actor(triggerId=506, visible=True, initialSequence='Closed')
        destroy_monster(spawnIds=[601,602,603,604,605,606])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[401]):
            return 버튼눌림()


class 버튼눌림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=501, visible=True, initialSequence='Opened')
        set_actor(triggerId=502, visible=True, initialSequence='Opened')
        create_monster(spawnIds=[601,602], arg2=False)
        move_npc(spawnId=601, patrolName='MS2PatrolData_601')
        move_npc(spawnId=602, patrolName='MS2PatrolData_602')


