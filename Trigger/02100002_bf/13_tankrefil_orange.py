""" trigger/02100002_bf/13_tankrefil_orange.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='ActivateTank', value=0) # 메인 트리거에서 받는 신호
        self.set_user_value(key='DungeonQuit', value=0) # 메인 트리거에서 받는 신호
        self.set_actor(triggerId=4003, visible=True, initialSequence='Interaction_tankorange_A01_100') # Up
        self.set_actor(triggerId=4103, visible=True, initialSequence='Interaction_tankorange_A01_100') # Down
        self.set_effect(triggerIds=[5303], visible=False) # Paint_Add_Sound
        self.set_effect(triggerIds=[5403], visible=False) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5503], visible=False) # Tank_Fill_Above_Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ActivateTank', value=1):
            return Gauge100(self.ctx)


class Gauge100(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=103, key='Gauge', value=100)
        self.set_timer(timerId='100100', seconds=15, startDelay=1)
        self.set_actor(triggerId=4003, visible=True, initialSequence='Interaction_tankorange_A01_100') # Up
        self.set_actor(triggerId=4103, visible=True, initialSequence='Interaction_tankorange_A01_100') # Down

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100100'):
            return Gauge75(self.ctx)
        if self.detect_liftable_object(boxIds=[2003], itemId=30000884):
            return Gauge100_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge100_Refil(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5303], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5403], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5503], visible=True) # Tank_Fill_Above_Sound
        self.reset_timer(timerId='100100')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge100(self.ctx)


class Gauge75(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=103, key='Gauge', value=75)
        self.reset_timer(timerId='100100')
        self.set_timer(timerId='10075', seconds=15, startDelay=1)
        self.set_actor(triggerId=4003, visible=True, initialSequence='Interaction_tankorange_A01_75') # Up
        self.set_actor(triggerId=4103, visible=True, initialSequence='Interaction_tankorange_A01_75') # Down

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10075'):
            return Gauge50(self.ctx)
        if self.detect_liftable_object(boxIds=[2003], itemId=30000884):
            return Gauge75_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge75_Refil(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5303], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5403], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5503], visible=True) # Tank_Fill_Above_Sound
        self.reset_timer(timerId='10075')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge100(self.ctx)


class Gauge50(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=103, key='Gauge', value=50)
        self.reset_timer(timerId='10075')
        self.set_timer(timerId='10050', seconds=15, startDelay=1)
        self.set_actor(triggerId=4003, visible=True, initialSequence='Interaction_tankorange_A01_50') # Up
        self.set_actor(triggerId=4103, visible=True, initialSequence='Interaction_tankorange_A01_50') # Down

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10050'):
            return Gauge25(self.ctx)
        if self.detect_liftable_object(boxIds=[2003], itemId=30000884):
            return Gauge50_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge50_Refil(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5303], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5403], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5503], visible=True) # Tank_Fill_Above_Sound
        self.reset_timer(timerId='10050')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge75(self.ctx)


class Gauge25(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=103, key='Gauge', value=25)
        self.reset_timer(timerId='10050')
        self.set_timer(timerId='10025', seconds=15, startDelay=1)
        self.set_actor(triggerId=4003, visible=True, initialSequence='Interaction_tankorange_A01_25') # Up
        self.set_actor(triggerId=4103, visible=True, initialSequence='Interaction_tankorange_A01_25') # Down

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10025'):
            return Gauge1(self.ctx)
        if self.detect_liftable_object(boxIds=[2003], itemId=30000884):
            return Gauge25_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge25_Refil(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5303], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5403], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5503], visible=True) # Tank_Fill_Above_Sound
        self.reset_timer(timerId='10025')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge50(self.ctx)


class Gauge1(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='10025')
        self.set_user_value(triggerId=103, key='Gauge', value=1)
        self.set_actor(triggerId=4003, visible=True, initialSequence='Interaction_tankorange_A01_1') # Up
        self.set_actor(triggerId=4103, visible=True, initialSequence='Interaction_tankorange_A01_1') # Down

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000884):
            return Gauge1_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge1_Refil(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5303], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5403], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5503], visible=True) # Tank_Fill_Above_Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge25(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=103, key='StopSpawn', value=1)


initial_state = Wait
