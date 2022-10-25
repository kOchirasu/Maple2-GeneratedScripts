""" trigger/63000036_cs/listen01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # Voice_DarkShadow_02000986
        self.set_effect(triggerIds=[5001], visible=False) # Voice_Kandura_00001863
        self.set_effect(triggerIds=[5002], visible=False) # Voice_Kandura_00001864

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Enter01(self.ctx)


class Enter01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[90000455], questStates=[1]):
            return CameraWalk01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000455], questStates=[2]):
            return CameraWalk01(self.ctx)
        if self.wait_tick(waitTick=4000):
            return PCTeleport02(self.ctx)


class CameraWalk01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102], animationEffect=False)
        self.select_camera(triggerId=500, enable=True)
        self.set_scene_skip(state=DialogueSkip03, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraWalk02(self.ctx)


class CameraWalk02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraWalk03(self.ctx)


class CameraWalk03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Dialogue01(self.ctx)


class Dialogue01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # Voice_DarkShadow_02000986
        self.set_conversation(type=2, spawnId=11001701, script='$63000036_CS__LISTEN01__0$', arg4=12) # 검은 그림자 02000986

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return DialogueSkip01(self.ctx)


class DialogueSkip01(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue02(self.ctx)


class Dialogue02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True) # Voice_Kandura_00001863
        self.set_conversation(type=2, spawnId=11001559, script='$63000036_CS__LISTEN01__1$', arg4=11) # 칸두라 00001863
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return DialogueSkip02(self.ctx)


class DialogueSkip02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Dialogue03(self.ctx)


class Dialogue03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True) # Voice_Kandura_00001864
        self.set_conversation(type=2, spawnId=11001559, script='$63000036_CS__LISTEN01__2$', arg4=9) # 칸두라 00001864

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return DialogueSkip03(self.ctx)


class DialogueSkip03(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return PCTeleport01(self.ctx)


class PCTeleport01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCTeleport02(self.ctx)


class PCTeleport02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000062, portalId=13)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
