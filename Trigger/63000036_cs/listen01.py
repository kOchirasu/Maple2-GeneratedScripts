""" trigger/63000036_cs/listen01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # Voice_DarkShadow_02000986
        set_effect(triggerIds=[5001], visible=False) # Voice_Kandura_00001863
        set_effect(triggerIds=[5002], visible=False) # Voice_Kandura_00001864

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Enter01()


class Enter01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[90000455], questStates=[1]):
            return CameraWalk01()
        if quest_user_detected(boxIds=[9000], questIds=[90000455], questStates=[2]):
            return CameraWalk01()
        if wait_tick(waitTick=4000):
            return PCTeleport02()


class CameraWalk01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102], arg2=False)
        select_camera(triggerId=500, enable=True)
        set_scene_skip(state=DialogueSkip03, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraWalk02()


class CameraWalk02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk03()


class CameraWalk03(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Dialogue01()


class Dialogue01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # Voice_DarkShadow_02000986
        set_conversation(type=2, spawnId=11001701, script='$63000036_CS__LISTEN01__0$', arg4=12) # 검은 그림자 02000986

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return DialogueSkip01()


class DialogueSkip01(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue02()


class Dialogue02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # Voice_Kandura_00001863
        set_conversation(type=2, spawnId=11001559, script='$63000036_CS__LISTEN01__1$', arg4=11) # 칸두라 00001863
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return DialogueSkip02()


class DialogueSkip02(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue03()


class Dialogue03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # Voice_Kandura_00001864
        set_conversation(type=2, spawnId=11001559, script='$63000036_CS__LISTEN01__2$', arg4=9) # 칸두라 00001864

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return DialogueSkip03()


class DialogueSkip03(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return PCTeleport01()


class PCTeleport01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCTeleport02()


class PCTeleport02(state.State):
    def on_enter(self):
        move_user(mapId=2000062, portalId=13)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    pass


