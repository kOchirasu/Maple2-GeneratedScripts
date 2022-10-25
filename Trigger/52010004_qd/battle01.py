""" trigger/52010004_qd/battle01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[10000], visible=False)
        self.set_agent(triggerIds=[10001], visible=False)
        self.set_agent(triggerIds=[10002], visible=False)
        self.set_agent(triggerIds=[10003], visible=False)
        self.create_monster(spawnIds=[101], animationEffect=False) # Quest
        self.set_mesh(triggerIds=[7000,7001,7002,7003], visible=False, arg3=0, delay=0, scale=0) # BattleZone

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002800], questStates=[2]):
            return 둔바교체01(self.ctx)


class 둔바교체01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_mesh(triggerIds=[7000,7001,7002,7003], visible=True, arg3=0, delay=0, scale=0) # BattleZone
        self.destroy_monster(spawnIds=[101]) # Quest
        self.create_monster(spawnIds=[102], animationEffect=False) # Act

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 둔바연출준비01(self.ctx)


class 둔바연출준비01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.select_camera(triggerId=601, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 둔바대화01(self.ctx)


class 둔바대화01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=2)
        self.set_conversation(type=2, spawnId=11001217, script='$52010004_QD__BATTLE01__0$', arg4=2)
        self.set_skip(state=둔바대화02대기)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 둔바대화02대기(self.ctx)


class 둔바대화02대기(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 둔바대화02(self.ctx)


class 둔바대화02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=2)
        self.set_conversation(type=2, spawnId=11001217, script='$52010004_QD__BATTLE01__1$', arg4=2)
        self.set_skip(state=둔바대화03대기)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='11'):
            return 둔바대화03대기(self.ctx)


class 둔바대화03대기(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 둔바대화03(self.ctx)


class 둔바대화03(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='12', seconds=2)
        self.set_conversation(type=2, spawnId=11001217, script='$52010004_QD__BATTLE01__2$', arg4=2)
        self.set_skip(state=둔바연출종료01)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='12'):
            return 둔바연출종료01(self.ctx)


class 둔바연출종료01(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_timer(timerId='13', seconds=1)
        self.select_camera(triggerId=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='13'):
            return 전투준비01(self.ctx)


class 전투준비01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=1)
        self.set_agent(triggerIds=[10000], visible=True)
        self.set_agent(triggerIds=[10001], visible=True)
        self.set_agent(triggerIds=[10002], visible=True)
        self.set_agent(triggerIds=[10003], visible=True)
        self.destroy_monster(spawnIds=[102]) # Act
        self.create_monster(spawnIds=[201], animationEffect=True) # Monster

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='20'):
            return 전투중01(self.ctx)


class 전투중01(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52010004, portalId=50, boxId=9000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[201]):
            return 둔바교체대기02(self.ctx)


class 둔바교체대기02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7000,7001,7002,7003], visible=False, arg3=0, delay=0, scale=0) # BattleZone
        self.set_timer(timerId='30', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='30'):
            return 둔바교체02(self.ctx)


class 둔바교체02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201]) # Monster
        self.create_monster(spawnIds=[101], animationEffect=False) # Quest


initial_state = 대기
