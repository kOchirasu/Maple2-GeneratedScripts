""" trigger/02010087_bf/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False) # 기본 배치 될 몬스터 등장
        self.set_effect(triggerIds=[7301], visible=False)
        self.set_effect(triggerIds=[7302], visible=False)
        self.set_effect(triggerIds=[7303], visible=False)
        self.set_effect(triggerIds=[7304], visible=False)
        self.set_effect(triggerIds=[7305], visible=False)
        self.set_effect(triggerIds=[7310], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=701, minUsers='1'):
            return 폭발01(self.ctx)


class 폭발01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7301], visible=True) # 폭발 이펙트
        self.set_skill(triggerIds=[8301], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, minUsers='1'):
            return 폭발02(self.ctx)


class 폭발02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7302], visible=True) # 폭발 이펙트
        self.set_skill(triggerIds=[8302], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=703, minUsers='1'):
            return 폭발03(self.ctx)


class 폭발03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7303], visible=True) # 폭발 이펙트
        self.set_effect(triggerIds=[7304], visible=True) # 폭발 이펙트
        self.set_skill(triggerIds=[8303], enable=True) # 벽 날리는 스킬
        self.set_skill(triggerIds=[8304], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=704, minUsers='1'):
            return 폭발04(self.ctx)


class 폭발04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7305], visible=True) # 폭발 이펙트
        self.set_skill(triggerIds=[8305], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=705, minUsers='1'):
            return 폭발04(self.ctx)


initial_state = 시작
