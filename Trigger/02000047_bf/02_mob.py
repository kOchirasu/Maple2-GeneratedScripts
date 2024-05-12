""" trigger/02000047_bf/02_mob.xml """
import trigger_api


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000078], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000078], stateValue=0):
            return 몬스터리젠(self.ctx)


class 몬스터리젠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[102])
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 우레우스대사(self.ctx)


class 우레우스대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=102, script='$02000047_BF__02_MOB__0$', arg4=3)
        self.set_conversation(type=1, spawnId=102, script='$02000047_BF__02_MOB__1$', arg4=3)
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        """
        <onExit>
        <action name="몬스터를생성한다" arg1="102"/>
        </onExit>
        """
        if self.time_expired(timerId='1'):
            # self.destroy_monster(spawnIds=[101])
            return 몬스터와전투(self.ctx)


"""
class 휴지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 몬스터와전투(self.ctx)

"""


class 몬스터와전투(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[102]):
            return 우레우스소멸(self.ctx)


class 우레우스소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[102]):
            self.reset_timer(timerId='1')
        if self.monster_dead(boxIds=[102]):
            return 소멸대기(self.ctx)
        if self.time_expired(timerId='1'):
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 트리거초기화(self.ctx)
        if self.monster_in_combat(boxIds=[102]):
            return 우레우스소멸(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[102]):
            return 우레우스소멸(self.ctx)
        if not self.monster_in_combat(boxIds=[102]):
            self.destroy_monster(spawnIds=[102])
            return 반응대기(self.ctx)


initial_state = 반응대기
