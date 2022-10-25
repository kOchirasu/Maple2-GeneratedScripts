""" trigger/52020020_qd/main_a.xml """
import common


class Idle(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200130], questStates=[2]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200130], questStates=[3]):
            return end(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52020020, portalId=6001)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Monologue_01(self.ctx)


class Monologue_01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='으으.......', duration=2500, align='Right')
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return Monologue_02(self.ctx)


class Monologue_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='도대체 무슨 일이 일어난 거지?', duration=2500, align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return Monologue_03(self.ctx)


class Monologue_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='.......', duration=3000, align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Monologue_04(self.ctx)


class Monologue_04(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='잠깐! 여기는?!', duration=3000, align='Right')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


initial_state = Idle
