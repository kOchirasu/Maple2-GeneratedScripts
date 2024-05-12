""" trigger/02000298_bf/hack_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000371], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[115]):
            return 스폰(self.ctx)


class 스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1031], animationEffect=False)
        self.set_interact_object(triggerIds=[10000371], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000371], stateValue=0):
            return 코드체크(self.ctx)


class 코드체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=197, spawnIds=[1279]):
            return 코드_1279(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1238]):
            return 코드_1238(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1358]):
            return 코드_1358(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1489]):
            return 코드_1489(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1567]):
            return 코드_1567(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[1679]):
            return 코드_1679(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2389]):
            return 코드_2389(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2347]):
            return 코드_2347(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2478]):
            return 코드_2478(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2456]):
            return 코드_2456(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2569]):
            return 코드_2569(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[2678]):
            return 코드_2678(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[3458]):
            return 코드_3458(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[3589]):
            return 코드_3589(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[3679]):
            return 코드_3679(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[3789]):
            return 코드_3789(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[4567]):
            return 코드_4567(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[4578]):
            return 코드_4578(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[4689]):
            return 코드_4689(self.ctx)
        if self.npc_detected(boxId=197, spawnIds=[4789]):
            return 코드_4789(self.ctx)


class 코드_1279(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__0$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__1$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1358(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=3)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__2$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1489(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__3$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1567(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__4$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__5$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2389(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__6$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2347(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__7$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2478(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__8$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2456(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__9$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2569(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__10$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2678(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__11$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_3458(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__12$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_3589(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__13$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_3679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__14$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_3789(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__15$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_4567(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__16$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_4578(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__17$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_4689(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__18$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_4789(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_03__19$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
