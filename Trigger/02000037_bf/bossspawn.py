""" trigger/02000037_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000931], state=2)
        self.set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009], visible=False, arg3=0, delay=0, scale=0) # Stairs 10
        self.set_mesh(triggerIds=[4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034], visible=False, arg3=0, delay=0, scale=0) # Bridge 15
        self.set_mesh(triggerIds=[4040,4041,4042,4043,4044,4045,4046], visible=False, arg3=0, delay=0, scale=0) # Slab 7
        self.set_mesh(triggerIds=[4050], visible=True, arg3=0, delay=0, scale=0) # invisible barrier
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5000], visible=False) # StairsAppear
        self.set_effect(triggerIds=[5001], visible=False) # Vibrate

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 난이도체크(self.ctx)


class 난이도체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_level(level=2):
            return 레이드(self.ctx)
        if self.dungeon_level(level=3):
            return 카오스레이드(self.ctx)


class 레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2000], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2000]):
            return 연출딜레이(self.ctx)


class 카오스레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 연출딜레이(self.ctx)


class 연출딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


# <state name="연출시작">
# <onEnter>
# <action name="연출UI를설정한다" arg1="1"/>
# <action name="연출UI를설정한다" arg1="3"/>
# <action name="대화를설정한다" arg1="2" arg2="11000144" arg3="$02000037_BF__BOSSSPAWN__0$" arg4="5"/>
# </onEnter>
# <condition name="WaitTick" waitTick="5000">
# <transition state="연출종료"/>
# </condition>
# </state>
class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_cinematic_ui(type=0)
        # self.set_cinematic_ui(type=2)
        self.set_interact_object(triggerIds=[10000931], state=1)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000931]):
            return 사념등장01(self.ctx)


class 사념등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4050], visible=False, arg3=0, delay=0, scale=0) # invisible barrier
        self.set_effect(triggerIds=[5000], visible=True) # StairsAppear
        self.set_effect(triggerIds=[5001], visible=True) # Vibrate
        self.set_random_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009], visible=True, meshCount=10, arg4=0, delay=50)
        self.set_random_mesh(triggerIds=[4040,4041,4042,4043,4044,4045,4046], visible=True, meshCount=7, arg4=400, delay=50)
        self.set_random_mesh(triggerIds=[4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034], visible=True, meshCount=15, arg4=800, delay=50)


initial_state = 시작대기중
