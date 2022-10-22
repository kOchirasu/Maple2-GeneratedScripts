""" trigger/02100002_bf/15_tankrefil_pink.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='ActivateTank', value=0) # 메인 트리거에서 받는 신호
        set_user_value(key='DungeonQuit', value=0) # 메인 트리거에서 받는 신호
        set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_100') # Up
        set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_100') # Down
        set_effect(triggerIds=[5305], visible=False) # Paint_Add_Sound
        set_effect(triggerIds=[5405], visible=False) # Tank_Fill_Under_Sound
        set_effect(triggerIds=[5505], visible=False) # Tank_Fill_Above_Sound

    def on_tick(self) -> state.State:
        if user_value(key='ActivateTank', value=1):
            return Gauge100()


class Gauge100(state.State):
    def on_enter(self):
        set_user_value(triggerId=105, key='Gauge', value=100)
        set_timer(timerId='100100', seconds=15, clearAtZero=True)
        set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_100') # Up
        set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_100') # Down

    def on_tick(self) -> state.State:
        if time_expired(timerId='100100'):
            return Gauge75()
        if detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge100_Refil()
        if user_value(key='DungeonQuit', value=1):
            return Quit()


class Gauge100_Refil(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound
        reset_timer(timerId='100100')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Gauge100()


class Gauge75(state.State):
    def on_enter(self):
        set_user_value(triggerId=105, key='Gauge', value=75)
        reset_timer(timerId='100100')
        set_timer(timerId='10075', seconds=15, clearAtZero=True)
        set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_75') # Up
        set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_75') # Down

    def on_tick(self) -> state.State:
        if time_expired(timerId='10075'):
            return Gauge50()
        if detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge75_Refil()
        if user_value(key='DungeonQuit', value=1):
            return Quit()


class Gauge75_Refil(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound
        reset_timer(timerId='10075')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Gauge100()


class Gauge50(state.State):
    def on_enter(self):
        set_user_value(triggerId=105, key='Gauge', value=50)
        reset_timer(timerId='10075')
        set_timer(timerId='10050', seconds=15, clearAtZero=True)
        set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_50') # Up
        set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_50') # Down

    def on_tick(self) -> state.State:
        if time_expired(timerId='10050'):
            return Gauge25()
        if detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge50_Refil()
        if user_value(key='DungeonQuit', value=1):
            return Quit()


class Gauge50_Refil(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound
        reset_timer(timerId='10050')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Gauge75()


class Gauge25(state.State):
    def on_enter(self):
        set_user_value(triggerId=105, key='Gauge', value=25)
        reset_timer(timerId='10050')
        set_timer(timerId='10025', seconds=15, clearAtZero=True)
        set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_25') # Up
        set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_25') # Down

    def on_tick(self) -> state.State:
        if time_expired(timerId='10025'):
            return Gauge1()
        if detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge25_Refil()
        if user_value(key='DungeonQuit', value=1):
            return Quit()


class Gauge25_Refil(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound
        reset_timer(timerId='10025')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Gauge50()


class Gauge1(state.State):
    def on_enter(self):
        reset_timer(timerId='10025')
        set_user_value(triggerId=105, key='Gauge', value=1)
        set_actor(triggerId=4005, visible=True, initialSequence='Interaction_tankpink_A01_1') # Up
        set_actor(triggerId=4105, visible=True, initialSequence='Interaction_tankpink_A01_1') # Down

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2005], itemId=30000887):
            return Gauge1_Refil()
        if user_value(key='DungeonQuit', value=1):
            return Quit()


class Gauge1_Refil(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5305], visible=True) # Paint_Add_Sound
        set_effect(triggerIds=[5405], visible=True) # Tank_Fill_Under_Sound
        set_effect(triggerIds=[5505], visible=True) # Tank_Fill_Above_Sound

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Gauge25()


class Quit(state.State):
    def on_enter(self):
        set_user_value(triggerId=105, key='StopSpawn', value=1)


