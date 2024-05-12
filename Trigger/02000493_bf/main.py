""" trigger/02000493_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6001], visible=False)
        self.set_effect(triggerIds=[6002], visible=True)
        self.set_effect(triggerIds=[6003], visible=True)
        self.set_effect(triggerIds=[6004], visible=True)
        self.set_effect(triggerIds=[6005], visible=True)
        self.set_effect(triggerIds=[6006], visible=True)
        self.set_effect(triggerIds=[6007], visible=True)
        self.set_effect(triggerIds=[6008], visible=True)
        self.set_effect(triggerIds=[6009], visible=True)
        self.set_effect(triggerIds=[6010], visible=True)
        self.set_skill(triggerIds=[7001], enable=False)
        self.set_skill(triggerIds=[7002], enable=False)
        self.set_skill(triggerIds=[7003], enable=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3060,3061,3062,3063,3064,3065,3066,3067], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3070,3071], visible=True, arg3=0, delay=0, scale=0)
        self.set_ladder(triggerIds=[3101], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3102], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3103], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3104], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3105], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3106], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3107], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3108], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3109], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3110], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3111], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[3112], visible=True, animationEffect=True, animationDelay=0)
        self.set_interact_object(triggerIds=[10000978], state=2)
        self.set_interact_object(triggerIds=[10000979], state=2)
        self.set_interact_object(triggerIds=[10000980], state=2)
        self.set_interact_object(triggerIds=[10000981], state=2)
        self.set_interact_object(triggerIds=[10000982], state=2)
        self.set_portal(portalId=32, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102,103,111,112,113,114,115,116,119,121,122,123,124,125,126,127], animationEffect=False)
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Nutaman_intro.swf', movieId=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 전투01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 전투01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,111,112,113,114,115,116,119,121,122,123,124,125,126,127]):
            return 전투02(self.ctx)


class 전투02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000978], state=1)
        self.set_interact_object(triggerIds=[10000979], state=1)
        self.set_interact_object(triggerIds=[10000980], state=1)
        self.create_monster(spawnIds=[201,202,203,204,205,211,212,213,214,215,216,217,218,221,222,223,224,225,226,227,228], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205,211,212,213,214,215,216,217,218,221,222,223,224,225,226,227,228]):
            return 전투03(self.ctx)


class 전투03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000981], state=1)
        self.set_interact_object(triggerIds=[10000982], state=1)
        self.create_monster(spawnIds=[301,302,303], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[301,302,303]):
            self.set_mesh(triggerIds=[3060,3061,3062,3063,3064,3065,3066,3067], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056], visible=True, arg3=0, delay=50, scale=1)
            return 전투04(self.ctx)


"""
class 사다리감지대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1002]):
            return None # Missing State: 붕괴시작

"""


"""
class 붕괴시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056], visible=False, arg3=0, delay=50, scale=1)
            return None # Missing State: 붕괴02

"""


"""
class 붕괴02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_ladder(triggerIds=[3101], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3102], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3103], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3104], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3105], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3106], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3107], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3108], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3109], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3110], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3111], visible=False, animationEffect=False, animationDelay=0)
            self.set_ladder(triggerIds=[3112], visible=False, animationEffect=False, animationDelay=0)
            self.set_skill(triggerIds=[7001], enable=True)
            return None # Missing State: 붕괴03

"""


"""
class 붕괴03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_skill(triggerIds=[7002], enable=True)
            return None # Missing State: 붕괴04

"""


"""
class 붕괴04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_skill(triggerIds=[7003], enable=True)
            return 전투04(self.ctx)

"""


class 전투04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[411,412,413,414,421,422,423,424], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[411,412,413,414,421,422,423,424]):
            return 포털개방(self.ctx)


class 포털개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6002], visible=False)
        self.set_effect(triggerIds=[6003], visible=False)
        self.set_effect(triggerIds=[6004], visible=False)
        self.set_effect(triggerIds=[6005], visible=False)
        self.set_effect(triggerIds=[6006], visible=False)
        self.set_effect(triggerIds=[6007], visible=False)
        self.set_effect(triggerIds=[6008], visible=False)
        self.set_effect(triggerIds=[6009], visible=False)
        self.set_effect(triggerIds=[6010], visible=False)
        self.set_mesh(triggerIds=[3070,3071], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
