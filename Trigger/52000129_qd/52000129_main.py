""" trigger/52000129_qd/52000129_main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002691], questStates=[1]):
            return 퀘스트진행_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002691], questStates=[2]):
            return 퀘스트완료가능_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002691], questStates=[3]):
            return 페이드아웃_01(self.ctx)
        if self.user_detected(boxIds=[701]):
            return 잠시대기(self.ctx)


class 잠시대기(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라이동_01(self.ctx)


class 카메라이동_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 카메라이동_02(self.ctx)


class 카메라이동_02(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000129_QD__52000129_MAIN__0$', desc='$52000129_QD__52000129_MAIN__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 카메라리셋_01(self.ctx)


class 카메라리셋_01(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 계단타고이동_01(self.ctx)


class 계단타고이동_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=25201291, textId=25201291)
        self.set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702]):
            return 퀘스트받기_01(self.ctx)


class 퀘스트받기_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201291)
        self.set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011], visible=False)
        self.show_guide_summary(entityId=25201292, textId=25201292)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[40002691], questStates=[1]):
            return 퀘스트진행_01(self.ctx)


class 퀘스트진행_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201291)
        self.hide_guide_summary(entityId=25201292)
        self.show_guide_summary(entityId=25201293, textId=25201293)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[40002691], questStates=[2]):
            return 퀘스트완료가능_01(self.ctx)


class 퀘스트완료가능_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25201291)
        self.hide_guide_summary(entityId=25201292)
        self.hide_guide_summary(entityId=25201293)
        self.show_guide_summary(entityId=25201294, textId=25201294)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[40002691], questStates=[3]):
            return 페이드아웃_01(self.ctx)


class 페이드아웃_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entityId=25201291)
        self.hide_guide_summary(entityId=25201292)
        self.hide_guide_summary(entityId=25201293)
        self.hide_guide_summary(entityId=25201294)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 페이드아웃_02(self.ctx)


class 페이드아웃_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000129, portalId=99)
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 페이드인_01(self.ctx)


class 페이드인_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMaskEff_fadein_1sec.xml')
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        self.set_scene_skip(state=마무리, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 감시_01(self.ctx)


class 감시_01(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        self.set_conversation(type=1, spawnId=101, script='$52000129_QD__52000129_MAIN__2$', arg4=2, arg5=0)
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 감시_02(self.ctx)


class 감시_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002,8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 감시_03(self.ctx)


class 감시_03(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2002')
        self.set_conversation(type=1, spawnId=102, script='$52000129_QD__52000129_MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 마무리(self.ctx)


class 마무리(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000130, portalId=1)


initial_state = 준비
