""" trigger/02000298_bf/hack_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000370], state=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[116]):
            return 스폰(self.ctx)


class 스폰(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1032], animationEffect=False)
        self.set_interact_object(triggerIds=[10000370], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000370], stateValue=0):
            return 코드체크(self.ctx)


class 코드체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
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


class 코드_1279(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__0$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1238(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__1$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1358(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__2$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1489(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__3$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1567(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__4$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_1679(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__5$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2389(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__6$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2347(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__7$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2478(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__8$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2456(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__9$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2569(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__10$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_2678(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__11$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_3458(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__12$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_3589(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__13$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_3679(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__14$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_3789(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__15$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_4567(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__16$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_4578(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__17$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_4689(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__18$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 코드_4789(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__19$', arg3='2000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
