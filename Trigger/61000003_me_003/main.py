""" trigger/61000003_me_003/main.xml """
from common import *
import state


class 입장(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        create_widget(type='OxQuiz') # OX 퀴즈 선언
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True) # action name="포탈을설정한다" arg1="99" arg2="0" arg3="0" arg4="0"/
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[608], visible=False)
        set_effect(triggerIds=[609], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_effect(triggerIds=[611], visible=False)
        set_effect(triggerIds=[612], visible=False)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0) # O
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0) # X
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0) # 주변
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # 벽

    def on_tick(self) -> state.State:
        if count_users(boxId=100, boxId=50):
            return 시작준비()
        if wait_tick(waitTick=60000):
            return 시작준비()


class 시작준비(state.State):
    def on_enter(self):
        set_mini_game_area_for_hack(boxId=105) # 해킹 보안용 시작 box 설정
        widget_action(type='OxQuiz', func='DevMode', widgetArg='0') # 개발자 모드 On (문제에 정답이 보인다)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 안내01()


class 안내01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__0$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 안내02()


class 안내02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__1$', arg3='4000', arg4='0')
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 안내03()


class 안내03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__2$', arg3='4000', arg4='0')
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제1()


class 문제1(state.State):
    def on_enter(self):
        start_mini_game(boxId=105, round=10, gameName='oxquiz')
        start_mini_game_round(boxId=105, round=1)
        set_achievement(triggerId=100, type='trigger', achieve='oxquiz_start')
        set_achievement(triggerId=100, type='trigger', achieve='dailyquest_start') # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        give_guild_exp(boxId=0, type=2) # action name="이펙트를설정한다" arg1="612" arg2="1" /
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='1,10') # OX 퀴즈 문제 뽑기, arg3=난이도(1~5)
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='1')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제1벽생성()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제1벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제1정답체크()


class 문제1정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='1')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제1정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제1정답X()


class 문제1정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제2준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='1')


class 문제1정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제2준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='1')


class 문제2준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__3$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제2()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제2(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=105, round=2)
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='2,10')
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='1')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제2벽생성()


class 문제2벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제2정답체크()


class 문제2정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='2')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제2정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제2정답X()


class 문제2정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제3준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='2')


class 문제2정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제3준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='2')


class 문제3준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__4$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제3()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제3(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=105, round=3)
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='3,10')
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='2')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제3벽생성()


class 문제3벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제3정답체크()


class 문제3정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='3')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제3정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제3정답X()


class 문제3정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제4준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='3')


class 문제3정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제4준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='3')


class 문제4준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__5$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제4()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제4(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=105, round=4)
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='4,10')
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='2')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제4벽생성()


class 문제4벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제4정답체크()


class 문제4정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='4')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제4정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제4정답X()


class 문제4정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제5준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='4')


class 문제4정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제5준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='4')


class 문제5준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__6$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제5()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제5(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=105, round=5)
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='5,10')
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='3')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제5벽생성()


class 문제5벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제5정답체크()


class 문제5정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='5')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제5정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제5정답X()


class 문제5정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제6준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='5')


class 문제5정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제6준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='5')


class 문제6준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__7$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제6()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제6(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=105, round=6)
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='6,10')
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='3')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제6벽생성()


class 문제6벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제6정답체크()


class 문제6정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='6')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제6정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제6정답X()


class 문제6정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제7준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='6')


class 문제6정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제7준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='6')


class 문제7준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__8$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제7()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제7(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=105, round=7)
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='7,10')
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='4')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제7벽생성()


class 문제7벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제7정답체크()


class 문제7정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='7')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제7정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제7정답X()


class 문제7정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제8준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='7')


class 문제7정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제8준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='7')


class 문제8준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__9$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제8()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제8(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=105, round=8)
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='8,10')
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='4')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제8벽생성()


class 문제8벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제8정답체크()


class 문제8정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='8')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제8정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제8정답X()


class 문제8정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제9준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='8')


class 문제8정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제9준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='8')


class 문제9준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__10$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제9()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제9(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=105, round=9)
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='9,10')
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='5')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제9벽생성()


class 문제9벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제9정답체크()


class 문제9정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='9')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제9정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제9정답X()


class 문제9정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제10준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='9')


class 문제9정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제10준비()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='9')


class 문제10준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[605], visible=True) # action name="PlaySystemSoundInBox" arg1="105" arg2="System_Quiz_Ready_01"/
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__11$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제10()
        if not user_detected(boxIds=[105]):
            return 종료()


class 문제10(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=105, round=10)
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Start_01')
        set_event_ui(type=0, arg2='10,10')
        widget_action(type='OxQuiz', func='PickQuiz', widgetArg='5')
        widget_action(type='OxQuiz', func='ShowQuiz', widgetArg='15')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 문제10벽생성()


class 문제10벽생성(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 문제10정답체크()


class 문제10정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='PreJudge', widgetArg='10')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuiz', name='Correct'):
            return 문제10정답O()
        if widget_condition(type='OxQuiz', name='Incorrect'):
            return 문제10정답X()


class 문제10정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0.1)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=101, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030,9031,9032,9033,9034,9035,9036,9037,9038,9039,9040,9041,9042,9043,9044,9045,9046,9047,9048,9049"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 완료체크()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='10')


class 문제10정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0.1)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        set_achievement(triggerId=102, type='trigger', achieve='oxquiz_correct')
        widget_action(type='OxQuiz', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0) # action name="아이템을생성한다" arg1="9101,9102,9103,9104,9105,9106,9107,9108,9109,9110,9111,9112,9113,9114,9115,9116,9117,9118,9119,9120,9121,9122,9123,9124,9125,9126,9127,9128,9129,9130,9131,9132,9133,9134,9135,9136,9137,9138,9139,9140,9141,9142,9143,9144,9145,9146,9147,9148,9149"/
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 완료체크()

    def on_exit(self):
        widget_action(type='OxQuiz', func='Judge', widgetArg='10')


class 완료체크(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 성공()
        if not user_detected(boxIds=[105]):
            return 종료()


class 성공(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104) # action name="이펙트를설정한다" arg1="606" arg2="1" /

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 우승자카메라연출()


class 우승자카메라연출(state.State):
    def on_enter(self):
        set_event_ui(type=3, arg2='$61000003_ME_003__MAIN__12$', arg3='5000', arg4='105')
        set_event_ui(type=4, arg2='$61000003_ME_003__MAIN__13$', arg3='5000', arg4='!105')
        mini_game_camera_direction(boxId=105, cameraId=301)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_local_camera(cameraId=301, enable=False)
            return 완료보상()


class 완료보상(state.State):
    def on_enter(self):
        widget_action(type='OxQuiz', func='Winner')
        add_buff(boxIds=[105], skillId=70000019, level=1)
        mini_game_give_reward(winnerBoxId=105, contentType='miniGame')
        end_mini_game(winnerBoxId=105, gameName='oxquiz')
        set_achievement(triggerId=105, type='trigger', achieve='oxquiz_win')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 종료2()


class 종료(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=105)
        end_mini_game(winnerBoxId=105, gameName='oxquiz')
        set_effect(triggerIds=[608], visible=True)
        set_event_ui(type=0, arg2='0,0')
        set_event_ui(type=5, arg2='$61000003_ME_003__MAIN__14$', arg3='3000', arg4='0')
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료2()


class 종료2(state.State):
    def on_enter(self):
        unset_mini_game_area_for_hack() # 해킹 보안 종료
        set_effect(triggerIds=[609], visible=True)
        set_event_ui(type=1, arg2='$61000003_ME_003__MAIN__15$', arg3='3000', arg4='0')
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            move_user(mapId=0, portalId=0)
            return 대기()


