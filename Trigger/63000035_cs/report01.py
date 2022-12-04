""" trigger/63000035_cs/report01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # Beep_Loop
        self.set_effect(triggerIds=[5001], visible=False) # MonitorOn_Pop
        self.set_effect(triggerIds=[6000], visible=False) # Voice_Kandura_Satisfied_00001866
        self.set_effect(triggerIds=[6001], visible=False) # Voice_Kandura_Think_00001867
        self.set_sound(triggerId=10000, enable=False) # BGM
        self.set_sound(triggerId=10001, enable=False) # AMB_BrokenTV
        self.set_sound(triggerId=10002, enable=False) # AMB_AbandonedFacility
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0) # MonitorOff
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0) # MonitorOn
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PlayOpeningMovie02(self.ctx)


class PlayOpeningMovie02(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='common\Common_Opening.usm', movieId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='2'):
            return PlayMovie01(self.ctx)
        if self.wait_tick(waitTick=190000):
            return PlayMovie01(self.ctx)


class PlayMovie01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PlayMovie02(self.ctx)


class PlayMovie02(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Cut_Vivid_Dream.swf', movieId=1) # 소울바인더 인트로 컷신

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return LodingDelay01(self.ctx)
        if self.wait_tick(waitTick=77000):
            return LodingDelay01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=500, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=10000, enable=True) # BGM
        self.set_sound(triggerId=10001, enable=True) # AMB_BrokenTV
        self.set_sound(triggerId=10002, enable=True) # AMB_AbandonedFacility
        self.set_effect(triggerIds=[5000], visible=True) # Beep_Loop
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Operator01(self.ctx)


class Operator01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001705, script='$63000035_CS__REPORT01__0$', arg4=6) # 오퍼레이터
        self.set_scene_skip(state=PCTeleport01, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return OperatorSkip01(self.ctx)


class OperatorSkip01(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Operator02(self.ctx)


class Operator02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001705, script='$63000035_CS__REPORT01__1$', arg4=6) # 오퍼레이터

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return OperatorSkip02(self.ctx)


class OperatorSkip02(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return MonitorOn01(self.ctx)


class MonitorOn01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=502, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return MonitorOn02(self.ctx)


class MonitorOn02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # Beep_Loop
        self.set_effect(triggerIds=[5001], visible=True) # MonitorOn_Pop
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0) # MonitorOn
        self.set_mesh(triggerIds=[3000], visible=False, arg3=100, delay=0, scale=0) # MonitorOff

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return MonitorOn03(self.ctx)


class MonitorOn03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=503, enable=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return KahnTalk01(self.ctx)


class KahnTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001559, script='$63000035_CS__REPORT01__2$', arg4=6) # 칸두라 00001867
        self.set_effect(triggerIds=[6001], visible=True) # Voice_Kandura_Think_00001867

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return KahnTalk02(self.ctx)


class KahnTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return KahnTalk03(self.ctx)


class KahnTalk03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=504, enable=True)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A') # 칸두라

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return KahnTalk04(self.ctx)


class KahnTalk04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return KahnTalk05(self.ctx)


class KahnTalk05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001559, script='$63000035_CS__REPORT01__3$', arg4=6) # 칸두라 00001866
        self.set_effect(triggerIds=[6000], visible=True) # Voice_Kandura_Satisfied_00001866

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return KahnTalk06(self.ctx)


class KahnTalk06(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCTeleport02(self.ctx)


class PCTeleport02(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=10000, enable=False) # BGM
        self.set_sound(triggerId=10001, enable=False) # AMB_BrokenTV
        self.set_sound(triggerId=10002, enable=False) # AMB_AbandonedFacility

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PCTeleport03(self.ctx)


class PCTeleport03(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000024, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=504, enable=False)


initial_state = Wait
