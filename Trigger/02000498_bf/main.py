""" trigger/02000498_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[500], visible=True)
        self.set_effect(triggerIds=[501], visible=True)
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_effect(triggerIds=[6010], visible=False)
        self.set_effect(triggerIds=[6011], visible=False)
        self.set_effect(triggerIds=[6012], visible=False)
        self.set_effect(triggerIds=[6013], visible=False)
        self.set_effect(triggerIds=[6015], visible=False)
        self.set_effect(triggerIds=[6016], visible=False)
        self.set_effect(triggerIds=[6017], visible=False)
        self.set_effect(triggerIds=[6018], visible=False)
        self.set_effect(triggerIds=[6019], visible=False)
        self.set_effect(triggerIds=[6020], visible=False)
        self.set_effect(triggerIds=[6021], visible=False)
        self.set_effect(triggerIds=[6022], visible=False)
        self.set_effect(triggerIds=[6023], visible=False)
        self.set_effect(triggerIds=[6024], visible=False)
        self.set_effect(triggerIds=[6025], visible=False)
        self.set_effect(triggerIds=[6026], visible=False)
        self.set_effect(triggerIds=[6027], visible=False)
        self.set_effect(triggerIds=[6028], visible=False)
        self.set_effect(triggerIds=[6029], visible=False)
        self.set_effect(triggerIds=[6030], visible=False)
        self.set_effect(triggerIds=[6031], visible=False)
        self.set_effect(triggerIds=[6032], visible=False)
        self.set_effect(triggerIds=[6110], visible=False)
        self.set_effect(triggerIds=[6111], visible=False)
        self.set_effect(triggerIds=[6112], visible=False)
        self.set_effect(triggerIds=[6113], visible=False)
        self.set_effect(triggerIds=[6101], visible=False)
        self.set_skill(triggerIds=[701], enable=False)
        self.set_skill(triggerIds=[702], enable=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100009]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[100009], skillId=70000102, level=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100001]):
            return 시작연출(self.ctx)


class 시작연출(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6011], visible=True)
        self.set_effect(triggerIds=[6012], visible=True)
        self.set_event_ui(type=1, arg2='다크스크림의 새로운 차원의 틈으로 진입 했습니다.', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100002]):
            return 시작연출_2(self.ctx)


class 시작연출_2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6013], visible=True)
        self.set_effect(triggerIds=[6010], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100003]):
            return 시작연출_3(self.ctx)


class 시작연출_3(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6023], visible=True)
        self.set_effect(triggerIds=[6022], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100004]):
            return 시작연출_4(self.ctx)


class 시작연출_4(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6021], visible=True)
        self.set_effect(triggerIds=[6024], visible=True)
        self.set_event_ui(type=1, arg2='더 가까이 다가가십시오.', arg3='3000')
        self.set_effect(triggerIds=[500], visible=False)
        self.set_effect(triggerIds=[501], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100005]):
            return 시작연출_5(self.ctx)


class 시작연출_5(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6028], visible=True)
        self.set_effect(triggerIds=[6027], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100006]):
            return 시작연출_6(self.ctx)


class 시작연출_6(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6025], visible=True)
        self.set_effect(triggerIds=[6026], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100007]):
            return 시작연출_7(self.ctx)


class 시작연출_7(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6032], visible=True)
        self.set_effect(triggerIds=[6029], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100008]):
            return 시작연출_8(self.ctx)


class 시작연출_8(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6031], visible=True)
        self.set_effect(triggerIds=[6030], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
