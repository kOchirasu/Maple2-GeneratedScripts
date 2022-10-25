""" trigger/52010018_qd/main.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[1]):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[1002,1003,1004,1006], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_A')
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_A')
        self.move_npc(spawnId=1006, patrolName='MS2PatrolData_1006_A')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[1002]):
            return 둔바대사01(self.ctx)
        if self.npc_detected(boxId=102, spawnIds=[1003]):
            return 둔바대사01(self.ctx)


class 둔바대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001217, script='$52010018_QD__MAIN__0$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 에레브대사01(self.ctx)


class 에레브대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52010018_QD__MAIN__1$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 미카대사01(self.ctx)


class 미카대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010018_QD__MAIN__2$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 미카이동01(self.ctx)


class 미카이동01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)
        self.move_npc(spawnId=1006, patrolName='MS2PatrolData_1006_B')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[1006]):
            return 동영상재생대기(self.ctx)


class 동영상재생대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 동영상재생(self.ctx)


class 동영상재생(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='awaken.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 동영상종료대기(self.ctx)


class 동영상종료대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 업적발생(self.ctx)


class 업적발생(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=100, type='trigger', achieve='ChangeMika')
        self.destroy_monster(spawnIds=[1006])
        self.create_monster(spawnIds=[1005], animationEffect=False)


initial_state = 대기
