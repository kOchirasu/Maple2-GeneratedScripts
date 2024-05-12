""" trigger/02000369_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=False)
        self.set_effect(trigger_ids=[6002], visible=True)
        self.set_effect(trigger_ids=[6003], visible=True)
        self.set_effect(trigger_ids=[6004], visible=True)
        self.set_effect(trigger_ids=[6005], visible=True)
        self.set_effect(trigger_ids=[6006], visible=True)
        self.set_effect(trigger_ids=[6007], visible=True)
        self.set_effect(trigger_ids=[6008], visible=True)
        self.set_effect(trigger_ids=[6009], visible=True)
        self.set_effect(trigger_ids=[6010], visible=True)
        self.set_skill(trigger_ids=[7001], enable=False)
        self.set_skill(trigger_ids=[7002], enable=False)
        self.set_skill(trigger_ids=[7003], enable=False)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3060,3061,3062,3063,3064,3065,3066,3067], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3070,3071], visible=True, start_delay=0, interval=0, fade=0)
        self.set_ladder(trigger_ids=[3101], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3102], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3103], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3104], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3105], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3106], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3107], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3108], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3109], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3110], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3111], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[3112], visible=True, enable=True, fade=0)
        self.set_interact_object(trigger_ids=[10000978], state=2)
        self.set_interact_object(trigger_ids=[10000979], state=2)
        self.set_interact_object(trigger_ids=[10000980], state=2)
        self.set_interact_object(trigger_ids=[10000981], state=2)
        self.set_interact_object(trigger_ids=[10000982], state=2)
        self.set_portal(portal_id=32, visible=False, enable=False, minimap_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103,111,112,113,114,115,116,117,118,119,121,122,123,124,125,126,127,128,129], auto_target=False)
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Nutaman_intro.swf', movie_id=1)
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
        if self.monster_dead(spawn_ids=[101,102,103,111,112,113,114,115,116,117,118,119,121,122,123,124,125,126,127,128,129]):
            return 전투02(self.ctx)


class 전투02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000978], state=1)
        self.set_interact_object(trigger_ids=[10000979], state=1)
        self.set_interact_object(trigger_ids=[10000980], state=1)
        self.spawn_monster(spawn_ids=[201,202,203,204,205,211,212,213,214,215,216,217,218,221,222,223,224,225,226,227,228], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205,211,212,213,214,215,216,217,218,221,222,223,224,225,226,227,228]):
            return 전투03(self.ctx)


class 전투03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000981], state=1)
        self.set_interact_object(trigger_ids=[10000982], state=1)
        self.spawn_monster(spawn_ids=[301,302,303], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301,302,303]):
            self.set_mesh(trigger_ids=[3060,3061,3062,3063,3064,3065,3066,3067], visible=False, start_delay=0, interval=0, fade=0)
            self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056], visible=True, start_delay=0, interval=50, fade=1)
            return 전투04(self.ctx)


"""
class 사다리감지대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1002]):
            return None # Missing State: 붕괴시작

"""


"""
class 붕괴시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056], visible=False, start_delay=0, interval=50, fade=1)
            return None # Missing State: 붕괴02

"""


"""
class 붕괴02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_ladder(trigger_ids=[3101], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3102], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3103], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3104], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3105], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3106], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3107], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3108], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3109], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3110], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3111], visible=False, enable=False, fade=0)
            self.set_ladder(trigger_ids=[3112], visible=False, enable=False, fade=0)
            self.set_skill(trigger_ids=[7001], enable=True)
            return None # Missing State: 붕괴03

"""


"""
class 붕괴03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_skill(trigger_ids=[7002], enable=True)
            return None # Missing State: 붕괴04

"""


"""
class 붕괴04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_skill(trigger_ids=[7003], enable=True)
            return 전투04(self.ctx)

"""


class 전투04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[411,412,413,414,421,422,423,424], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[411,412,413,414,421,422,423,424]):
            return 포털개방(self.ctx)


class 포털개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=False)
        self.set_effect(trigger_ids=[6003], visible=False)
        self.set_effect(trigger_ids=[6004], visible=False)
        self.set_effect(trigger_ids=[6005], visible=False)
        self.set_effect(trigger_ids=[6006], visible=False)
        self.set_effect(trigger_ids=[6007], visible=False)
        self.set_effect(trigger_ids=[6008], visible=False)
        self.set_effect(trigger_ids=[6009], visible=False)
        self.set_effect(trigger_ids=[6010], visible=False)
        self.set_mesh(trigger_ids=[3070,3071], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
