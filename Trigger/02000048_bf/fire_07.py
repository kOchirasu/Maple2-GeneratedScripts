""" trigger/02000048_bf/fire_07.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000312], state=1)
        self.set_mesh(triggerIds=[207], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[307], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000312], stateValue=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[207], visible=True, arg3=0, delay=0, scale=1)
        self.set_effect(triggerIds=[307], visible=True)
        self.create_monster(spawnIds=[407], animationEffect=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=407, script='$02000048_BF__FIRE_07__0$', arg4=2)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 몬스터와전투(self.ctx)


class 몬스터와전투(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[407]):
            return 딜레이(self.ctx)
        if not self.monster_in_combat(boxIds=[407]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[407]):
            self.reset_timer(timerId='1')
            return None
        if self.monster_dead(boxIds=[407]):
            return 소멸대기(self.ctx)
        if self.time_expired(timerId='1'):
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 딜레이(self.ctx)
        if self.monster_in_combat(boxIds=[407]):
            return 몬스터소멸(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[407])
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
