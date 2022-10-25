""" trigger/52020030_qd/main30000336.xml """
import common


# 투르카와 전투
class 체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2003], questIds=[30000336], questStates=[2]):
            return 체크2(self.ctx)


class 체크2(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(isVisible=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.set_scene_skip(state=세번째연출대화진행05, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세번째연출대화진행_01(self.ctx)


class 세번째연출대화진행_01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003756, msg='...계획이 틀어졌군.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세번째연출대화진행(self.ctx)


class 세번째연출대화진행(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4017], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003753, msg='... 왔나.\n바보같은 행동을 했더군.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세번째연출대화진행02(self.ctx)


class 세번째연출대화진행02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4022], returnView=False)
        self.set_npc_emotion_sequence(spawnId=108, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003756, msg='... 할말 없어.\n그래서, 이제 어쩔 셈이지?', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 세번째연출대화진행03(self.ctx)


class 세번째연출대화진행03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4017], returnView=False)
        self.add_cinematic_talk(npcId=11003753, msg='훗. 바보같이.\n이제 흑성회가 움직이긴 어렵겠군.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세번째연출대화진행03_01(self.ctx)


class 세번째연출대화진행03_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4040], returnView=False)
        self.add_cinematic_talk(npcId=11003753, msg='또 다른 계획을 준비해야겠어.', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 세번째연출대화진행04(self.ctx)


class 세번째연출대화진행04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4022], returnView=False)
        self.set_npc_emotion_sequence(spawnId=108, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003753, msg='그 새로운 계획, 흑성회에도 당연히 전달해 주겠지?\n기대할께.', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 세번째연출대화진행05(self.ctx)


class 세번째연출대화진행05(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세번째연출대화진행06(self.ctx)


class 세번째연출대화진행06(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=2020017, portalId=4)


initial_state = 체크
