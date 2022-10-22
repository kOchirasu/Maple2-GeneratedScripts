""" trigger/52000043_qd/50001453.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1003,2003])
        set_agent(triggerIds=[9000], visible=False)
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_agent(triggerIds=[9005], visible=False)
        set_agent(triggerIds=[9006], visible=False)
        set_agent(triggerIds=[9007], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001453], questStates=[1]):
            destroy_monster(spawnIds=[1003,2003])
            return 시작조건()


class 시작조건(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1003,2003], arg2=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001020], state=2)
        set_interact_object(triggerIds=[10001021], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001021], arg2=0):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9000], visible=True)
        set_agent(triggerIds=[9001], visible=True)
        set_agent(triggerIds=[9002], visible=True)
        set_agent(triggerIds=[9003], visible=True)
        set_agent(triggerIds=[9004], visible=True)
        set_agent(triggerIds=[9005], visible=True)
        set_agent(triggerIds=[9006], visible=True)
        set_agent(triggerIds=[9007], visible=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[2100,2101], arg2=False)
        select_camera(triggerId=303, enable=True)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1004A')
        move_npc(spawnId=2003, patrolName='MS2PatrolData_2004A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPC대사01()


class NPC대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)
        set_conversation(type=2, spawnId=29000121, script='$52000043_QD__50001453__0$', arg4=3)
        set_skip(state=NPC대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 준타대사01()


class NPC대사01스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사01()


class 준타대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001453__1$', arg4=3)
        set_skip(state=준타대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 준타대사02()


class 준타대사01스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사02()


class 준타대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001453__2$', arg4=2)
        set_skip(state=준타대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 틴차이대사01()


class 준타대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사01()


class 틴차이대사01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[605], visible=True)
        set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001453__3$', arg4=4)
        set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출종료()


class 틴차이대사01스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[605], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1003,2003])
        create_monster(spawnIds=[1004,2004], arg2=False)
        set_agent(triggerIds=[9000], visible=False)
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_agent(triggerIds=[9005], visible=False)
        set_agent(triggerIds=[9006], visible=False)
        set_agent(triggerIds=[9007], visible=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=303, enable=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2100,2101]):
            return 연출02시작()


class 연출02시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_interact_object(triggerIds=[10001021], state=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1002C')
        move_npc(spawnId=2004, patrolName='MS2PatrolData_2002C')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1004]):
            return NPC교체01()


class NPC교체01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1004])
        create_monster(spawnIds=[1003], arg2=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[2004]):
            return NPC교체02()


class NPC교체02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2004])
        create_monster(spawnIds=[2003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출종료2()


class 연출종료2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 종료()


class 종료(state.State):
    pass


