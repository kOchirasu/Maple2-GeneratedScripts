""" trigger/52010033_qd/main_quest10003078.xml """
import common


# 페리온 병원 : 52010033
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003078], questStates=[2]):
            return 유저감지(self.ctx)


class 유저감지(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.visible_my_pc(isVisible=False)
        self.move_user(mapId=52010033, portalId=6001)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 티나감사(self.ctx)


class 티나감사(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=나메드들어옴02, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.add_cinematic_talk(npcId=11003420, msg='$52010033_QD__MAIN_QUEST10003078__0$', duration=4000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__1$', duration=3000)
        self.add_cinematic_talk(npcId=11003420, msg='$52010033_QD__MAIN_QUEST10003078__2$', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 나메드들어옴(self.ctx)


class 나메드들어옴(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[201], animationEffect=True) # 나메드:
        self.select_camera_path(pathIds=[4002,4001], returnView=False)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        self.show_caption(type='VerticalCaption', title='$52010033_QD__MAIN_QUEST10003078__3$', desc='$52010033_QD__MAIN_QUEST10003078__4$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2)
        self.add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__5$', duration=5000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__6$', duration=4500)
        self.add_cinematic_talk(npcId=11003420, msg='$52010033_QD__MAIN_QUEST10003078__7$', duration=2000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__8$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010033_QD__MAIN_QUEST10003078__9$', duration=2000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010033_QD__MAIN_QUEST10003078__10$', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=22000):
            return 나메드들어옴_1(self.ctx)


class 나메드들어옴_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 나메드들어옴02(self.ctx)


class 나메드들어옴02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52010032, portalId=1)


initial_state = idle
