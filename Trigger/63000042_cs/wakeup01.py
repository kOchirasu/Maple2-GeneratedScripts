""" trigger/63000042_cs/wakeup01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001484], questStates=[2]):
            return LodingDelay00()


class LodingDelay00(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_enter(self):
        move_user(mapId=63000042, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LodingDelay02()


class LodingDelay02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[101], arg2=False)
        select_camera(triggerId=500, enable=True)
        set_pc_emotion_loop(sequenceName='Down_Idle_D', duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCDownIdle01()


class PCDownIdle01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=PCDownIdle02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCDownIdle02()


class PCDownIdle02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DoctorTalk01()


class DoctorTalk01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000038, script='$63000042_CS__WAKEUP01__0$', arg4=4)
        set_skip(state=DoctorTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return DoctorTalk01Skip()


class DoctorTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return LookAround01()


class LookAround01(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=False)
        select_camera(triggerId=501, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=18000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LookAround02()


class LookAround02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DoctorTalk02()


class DoctorTalk02(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=5000)
        set_conversation(type=2, spawnId=11000038, script='$63000042_CS__WAKEUP01__1$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DoctorTalk03()


class DoctorTalk03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=5000)
        set_conversation(type=2, spawnId=11000038, script='$63000042_CS__WAKEUP01__2$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return DoctorTalk04()


class DoctorTalk04(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=5000)
        set_conversation(type=2, spawnId=11000038, script='$63000042_CS__WAKEUP01__3$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SceneEnd01()


class SceneEnd01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SceneEnd02()


class SceneEnd02(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=False)
        set_pc_emotion_sequence(sequenceNames=['Idle_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)


