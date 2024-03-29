""" trigger/61000021_me_003/main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='OxQuizUGC') # OX 퀴즈 선언
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_effect(triggerIds=[606], visible=False)
        self.set_effect(triggerIds=[607], visible=False)
        self.set_effect(triggerIds=[608], visible=False)
        self.set_effect(triggerIds=[609], visible=False)
        self.set_effect(triggerIds=[610], visible=False)
        self.set_effect(triggerIds=[611], visible=False)
        self.set_effect(triggerIds=[612], visible=False)
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, delay=0, scale=0) # O
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, delay=0, scale=0) # X
        self.set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, delay=0, scale=0) # 주변
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, delay=0, scale=0) # 벽

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=100, boxId=50):
            return 준비(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_mini_game_area_for_hack(boxId=105)
        self.set_timer(timerId='2', seconds=1)
        self.move_user(mapId=61000021, portalId=99, boxId=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 시작(self.ctx)
        if not self.user_detected(boxIds=[105]):
            return 종료(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_mini_game_area_for_hack(boxId=105)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='OxQuizUGC', name='IsQuizSubmit'):
            return 문제표시(self.ctx)
        if self.widget_condition(type='OxQuizUGC', name='IsFinished'):
            return 종료(self.ctx)


class 문제표시(trigger_api.Trigger):
    def on_enter(self):
        self.start_mini_game(boxId=105, round=10, gameName='oxquiz_ugc')
        self.widget_action(type='OxQuizUGC', func='PeekQuiz')
        self.widget_action(type='OxQuizUGC', func='ShowQuiz', widgetArg='15')
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, delay=0, scale=0)
        self.set_timer(timerId='15', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='15'):
            return 벽생성(self.ctx)


class 벽생성(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, delay=0, scale=0)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 정답체크(self.ctx)


class 정답체크(trigger_api.Trigger):
    def on_enter(self):
        self.widget_action(type='OxQuizUGC', func='PreJudge', widgetArg='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='OxQuizUGC', name='Correct'):
            return 문제정답O(self.ctx)
        if self.widget_condition(type='OxQuizUGC', name='Incorrect'):
            return 문제정답X(self.ctx)


class 문제정답O(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=101, expRate=0.1)
        self.play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        self.widget_action(type='OxQuizUGC', func='ShowAnswer', widgetArg='5')
        self.set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        self.set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, delay=0, scale=0)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 문제정리(self.ctx)


class 문제정답X(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=102, expRate=0.1)
        self.play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        self.play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        self.widget_action(type='OxQuizUGC', func='ShowAnswer', widgetArg='5')
        self.set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        self.set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, delay=0, scale=0)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 문제정리(self.ctx)


class 문제정리(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, delay=0, scale=0)
        self.set_timer(timerId='20', seconds=10)
        self.widget_action(type='OxQuizUGC', func='CleanUpQuiz')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='20'):
            return 준비(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game(winnerBoxId=105, gameName='oxquiz_ugc')
        self.set_effect(triggerIds=[608], visible=True)
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=5, arg2='$61000003_ME_003__MAIN__14$', arg3='3000', arg4='0')


class 종료2(trigger_api.Trigger):
    def on_enter(self):
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_effect(triggerIds=[609], visible=True)
        self.set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__15$', arg3='3000', arg4='0')
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            self.move_user(mapId=0, portalId=0)
            return 대기(self.ctx)


initial_state = 입장
