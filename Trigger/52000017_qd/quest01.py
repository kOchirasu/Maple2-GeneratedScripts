""" trigger/52000017_qd/quest01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.create_monster(spawnIds=[1001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[50001444], questStates=[2]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Cut_Remember_Vision.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 말풍선딜레이(self.ctx)


class 말풍선딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return PC말풍선01(self.ctx)


class PC말풍선01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000017_QD__QUEST01__0$', arg4=3, arg5=0)
        self.set_scene_skip(state=종료, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC대사01(self.ctx)


class NPC대사01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True)
        self.set_conversation(type=2, spawnId=11001560, script='$52000017_QD__QUEST01__1$', arg4=4)
        self.set_skip(state=NPC대사01스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return NPC대사02(self.ctx)


class NPC대사01스킵(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NPC대사02(self.ctx)


class NPC대사02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_conversation(type=2, spawnId=11001560, script='$52000017_QD__QUEST01__2$', arg4=3)
        self.set_skip(state=NPC대사02스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출종료(self.ctx)


class NPC대사02스킵(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000040, portalId=1)


initial_state = 대기
