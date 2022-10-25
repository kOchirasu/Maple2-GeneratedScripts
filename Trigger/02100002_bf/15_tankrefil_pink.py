""" trigger/02100002_bf/15_tankrefil_pink.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='ActivateTank', value=0) # 메인 트리거에서 받는 신호
        self.set_user_value(key='DungeonQuit', value=0) # 메인 트리거에서 받는 신호
        self.set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_100') # Up
        self.set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_100') # Down
        self.set_effect(triggerIds=[5305], visible=False) # Paint_Add_Sound
        self.set_effect(triggerIds=[5405], visible=False) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5505], visible=False) # Tank_Fill_Above_Sound

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ActivateTank', value=1):
            return Gauge100(self.ctx)


class Gauge100(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=105, key='Gauge', value=100)
        self.set_timer(timerId='100100', seconds=15, startDelay=1)
        self.set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_100') # Up
        self.set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_100') # Down

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='100100'):
            return Gauge75(self.ctx)
        if self.detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge100_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge100_Refil(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound
        self.reset_timer(timerId='100100')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge100(self.ctx)


class Gauge75(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=105, key='Gauge', value=75)
        self.reset_timer(timerId='100100')
        self.set_timer(timerId='10075', seconds=15, startDelay=1)
        self.set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_75') # Up
        self.set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_75') # Down

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10075'):
            return Gauge50(self.ctx)
        if self.detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge75_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge75_Refil(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound
        self.reset_timer(timerId='10075')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge100(self.ctx)


class Gauge50(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=105, key='Gauge', value=50)
        self.reset_timer(timerId='10075')
        self.set_timer(timerId='10050', seconds=15, startDelay=1)
        self.set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_50') # Up
        self.set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_50') # Down

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10050'):
            return Gauge25(self.ctx)
        if self.detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge50_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge50_Refil(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound
        self.reset_timer(timerId='10050')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge75(self.ctx)


class Gauge25(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=105, key='Gauge', value=25)
        self.reset_timer(timerId='10050')
        self.set_timer(timerId='10025', seconds=15, startDelay=1)
        self.set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_25') # Up
        self.set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_25') # Down

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10025'):
            return Gauge1(self.ctx)
        if self.detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge25_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge25_Refil(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound
        self.reset_timer(timerId='10025')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge50(self.ctx)


class Gauge1(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='10025')
        self.set_user_value(triggerId=105, key='Gauge', value=1)
        self.set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_1') # Up
        self.set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_1') # Down

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge1_Refil(self.ctx)
        if self.user_value(key='DungeonQuit', value=1):
            return Quit(self.ctx)


class Gauge1_Refil(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        self.set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        self.set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Gauge25(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=105, key='StopSpawn', value=1)


initial_state = Wait
