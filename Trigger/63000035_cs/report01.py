""" trigger/63000035_cs/report01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # Beep_Loop
        set_effect(triggerIds=[5001], visible=False) # MonitorOn_Pop
        set_effect(triggerIds=[6000], visible=False) # Voice_Kandura_Satisfied_00001866
        set_effect(triggerIds=[6001], visible=False) # Voice_Kandura_Think_00001867
        set_sound(triggerId=10000, arg2=False) # BGM
        set_sound(triggerId=10001, arg2=False) # AMB_BrokenTV
        set_sound(triggerId=10002, arg2=False) # AMB_AbandonedFacility
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # MonitorOff
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # MonitorOn
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Enter01()


class Enter01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PlayOpeningMovie02()


class PlayOpeningMovie02(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='common\Common_Opening.usm', movieId=2)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='2'):
            return PlayMovie01()
        if wait_tick(waitTick=190000):
            return PlayMovie01()


class PlayMovie01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PlayMovie02()


class PlayMovie02(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Cut_Vivid_Dream.swf', movieId=1) # 소울바인더 인트로 컷신

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return LodingDelay01()
        if wait_tick(waitTick=77000):
            return LodingDelay01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class LodingDelay01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=500, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraWalk01()


class CameraWalk01(state.State):
    def on_enter(self):
        set_sound(triggerId=10000, arg2=True) # BGM
        set_sound(triggerId=10001, arg2=True) # AMB_BrokenTV
        set_sound(triggerId=10002, arg2=True) # AMB_AbandonedFacility
        set_effect(triggerIds=[5000], visible=True) # Beep_Loop
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Operator01()


class Operator01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001705, script='$63000035_CS__REPORT01__0$', arg4=6) # 오퍼레이터
        set_scene_skip(state=PCTeleport01, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return OperatorSkip01()


class OperatorSkip01(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Operator02()


class Operator02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001705, script='$63000035_CS__REPORT01__1$', arg4=6) # 오퍼레이터

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return OperatorSkip02()


class OperatorSkip02(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return MonitorOn01()


class MonitorOn01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=502, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return MonitorOn02()


class MonitorOn02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # Beep_Loop
        set_effect(triggerIds=[5001], visible=True) # MonitorOn_Pop
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # MonitorOn
        set_mesh(triggerIds=[3000], visible=False, arg3=100, arg4=0, arg5=0) # MonitorOff

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return MonitorOn03()


class MonitorOn03(state.State):
    def on_enter(self):
        select_camera(triggerId=503, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return KahnTalk01()


class KahnTalk01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001559, script='$63000035_CS__REPORT01__2$', arg4=6) # 칸두라 00001867
        set_effect(triggerIds=[6001], visible=True) # Voice_Kandura_Think_00001867

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return KahnTalk02()


class KahnTalk02(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return KahnTalk03()


class KahnTalk03(state.State):
    def on_enter(self):
        select_camera(triggerId=504, enable=True)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A') # 칸두라

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return KahnTalk04()


class KahnTalk04(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KahnTalk05()


class KahnTalk05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001559, script='$63000035_CS__REPORT01__3$', arg4=6) # 칸두라 00001866
        set_effect(triggerIds=[6000], visible=True) # Voice_Kandura_Satisfied_00001866

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return KahnTalk06()


class KahnTalk06(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCTeleport01()


class PCTeleport01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCTeleport02()


class PCTeleport02(state.State):
    def on_enter(self):
        set_sound(triggerId=10000, arg2=False) # BGM
        set_sound(triggerId=10001, arg2=False) # AMB_BrokenTV
        set_sound(triggerId=10002, arg2=False) # AMB_AbandonedFacility

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PCTeleport03()


class PCTeleport03(state.State):
    def on_enter(self):
        move_user(mapId=63000024, portalId=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        select_camera(triggerId=504, enable=False)


