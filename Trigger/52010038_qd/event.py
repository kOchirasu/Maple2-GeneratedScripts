""" trigger/52010038_qd/event.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)
        self.set_agent(triggerIds=[8009], visible=True)
        self.set_agent(triggerIds=[8010], visible=True)
        self.set_agent(triggerIds=[8011], visible=True)
        self.set_agent(triggerIds=[8012], visible=True)
        self.set_agent(triggerIds=[8013], visible=True)
        self.set_skill(triggerIds=[710], enable=False)
        self.set_skill(triggerIds=[711], enable=False)
        self.set_effect(triggerIds=[6110], visible=False)
        self.set_effect(triggerIds=[6111], visible=False)
        self.set_effect(triggerIds=[6298], visible=False)
        self.set_actor(triggerId=220, visible=False)
        self.set_actor(triggerId=221, visible=False)
        self.set_actor(triggerId=222, visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EventStart', value=1):
            return 이벤트조건(self.ctx)


class 이벤트조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6298], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 이벤트시작(self.ctx)


class 이벤트시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1200], animationEffect=False)
        self.destroy_monster(spawnIds=[1201])
        self.set_conversation(type=1, spawnId=1200, script='$52010038_QD__EVENT__0$', arg4=2, arg5=0)
        self.move_npc(spawnId=1200, patrolName='MS2PatrolData_1200')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=104, spawnIds=[1200]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[710], enable=True)
        self.set_effect(triggerIds=[6110], visible=True)
        self.create_monster(spawnIds=[2012,2013,2014,2015], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 감지대기(self.ctx)


class 감지대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_agent(triggerIds=[8009], visible=False)
        self.set_agent(triggerIds=[8010], visible=False)
        self.set_agent(triggerIds=[8011], visible=False)
        self.set_agent(triggerIds=[8012], visible=False)
        self.set_agent(triggerIds=[8013], visible=False)
        self.set_conversation(type=1, spawnId=1200, script='$52010038_QD__EVENT__2$', arg4=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[105]):
            return 폭발시퀀스시작(self.ctx)


class 폭발시퀀스시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=220, visible=True, initialSequence='Regen_A')
        self.set_actor(triggerId=221, visible=True, initialSequence='Regen_A')
        self.set_actor(triggerId=222, visible=True, initialSequence='Regen_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 폭발딜레이(self.ctx)


class 폭발딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=220, visible=True, initialSequence='Attack_01_A')
        self.set_actor(triggerId=221, visible=True, initialSequence='Attack_01_A')
        self.set_actor(triggerId=222, visible=True, initialSequence='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 폭발(self.ctx)


class 폭발(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=220, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=221, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=222, visible=True, initialSequence='Attack_02_A')
        self.set_skill(triggerIds=[711], enable=True)
        self.set_effect(triggerIds=[6298], visible=False)
        self.set_effect(triggerIds=[6111], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return 폭탄숨김(self.ctx)


class 폭탄숨김(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=220, visible=False)
        self.set_actor(triggerId=221, visible=False)
        self.set_actor(triggerId=222, visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1300):
            return 점수(self.ctx)


class 점수(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[4010], animationEffect=False)
        self.create_monster(spawnIds=[4030], animationEffect=False)
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$52010038_QD__event__4$', voice='ko/Npc/00002105')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
