""" trigger/61000011_me/main.xml """
from common import *
import state


class 입장(state.State):
    def on_enter(self):
        create_widget(type='OxQuizUGC')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)
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
        widget_action(type='OxQuizUGC', func='ShowHostUI')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuizUGC', name='IsStarted'):
            return 게임시작()
        if widget_condition(type='OxQuizUGC', name='IsCanceled'):
            return 게임취소()


class 게임시작(state.State):
    def on_enter(self):
        start_mini_game(boxId=105, round=10, gameName='oxquiz_ugc', isShowResultUI=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        set_mini_game_area_for_hack(boxId=105)
        set_timer(timerId='2', seconds=1)
        move_user(mapId=61000021, portalId=99, boxId=104)
        widget_action(type='OxQuizUGC', func='StartRound') # StartMiniGameRound 는 OxQuizUGC 위젯의 StartRound 에서 불러줌
        widget_action(type='OxQuizUGC', func='HostUIChange', widgetArg='InputQuiz')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_mini_game_area_for_hack(boxId=105)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[105]):
            return 종료()
        if widget_condition(type='OxQuizUGC', name='IsCanceled'):
            return 게임취소()
        if widget_condition(type='OxQuizUGC', name='IsFinished'):
            return 게임끝()
        if widget_condition(type='OxQuizUGC', name='IsQuizSubmit'):
            return 문제표시()


class 문제표시(state.State):
    def on_enter(self):
        widget_action(type='OxQuizUGC', func='ShowQuiz', widgetArg='15')
        widget_action(type='OxQuizUGC', func='HostUIChange', widgetArg='Move')
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='15', seconds=15)
        set_achievement(triggerId=100, type='trigger', achieve='bjoxquiz_start')

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 벽생성()


class 벽생성(state.State):
    def on_enter(self):
        widget_action(type='OxQuizUGC', func='CreateWall')
        play_system_sound_in_box(boxIds=[105], sound='System_Quiz_Popup_Off_01')
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 정답대기()


class 정답대기(state.State):
    def on_enter(self):
        widget_action(type='OxQuizUGC', func='HostUIChange', widgetArg='SelectAnswer')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuizUGC', name='IsRemoveWall'):
            return 문제표시()
        if widget_condition(type='OxQuizUGC', name='IsAnswerSubmit'):
            return 정답체크()


class 정답체크(state.State):
    def on_enter(self):
        widget_action(type='OxQuizUGC', func='PreJudge', widgetArg='1')
        widget_action(type='OxQuizUGC', func='HostUIChange', widgetArg='Judge')

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuizUGC', name='Correct'):
            return 문제정답O()
        if widget_condition(type='OxQuizUGC', name='Incorrect'):
            return 문제정답X()


class 문제정답O(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=101, expRate=0, meso=0)
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Wrong_01')
        widget_action(type='OxQuizUGC', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제정리()


class 문제정답X(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=102, expRate=0, meso=0)
        play_system_sound_in_box(boxIds=[102], sound='System_Quiz_Answer_Correct_01')
        play_system_sound_in_box(boxIds=[101], sound='System_Quiz_Answer_Wrong_01')
        widget_action(type='OxQuizUGC', func='ShowAnswer', widgetArg='5')
        set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=False, meshCount=49, arg4=0, delay=10)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 문제정리()


class 문제정리(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='20', seconds=2)
        widget_action(type='OxQuizUGC', func='EndRound')
        move_user(mapId=61000011, portalId=99, boxId=104)

    def on_tick(self) -> state.State:
        if widget_condition(type='OxQuizUGC', name='IsFinished'):
            return 게임끝()
        if widget_condition(type='OxQuizUGC', name='IsCanceled'):
            return 게임취소()
        if time_expired(timerId='20'):
            return 준비()


class 게임끝(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        move_user(mapId=61000003, portalId=99, boxId=104)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 성공()
        if not user_detected(boxIds=[105]):
            return 종료()


class 게임취소(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000011_ME__GAME_END_BY_CANCEL$', arg3='3000', arg4='0')
        set_timer(timerId='2', seconds=10)
        move_user(mapId=61000003, portalId=99, boxId=104)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 마무리()

    def on_exit(self):
        widget_action(type='OxQuizUGC', func='EndGame')
        end_mini_game(winnerBoxId=105, gameName='oxquiz_ugc', isOnlyWinner='1')


class 성공(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333,3334,3335,3336,3337,3338,3339,3340,3341,3342,3343,3344,3345,3346,3347,3348,3349,3350,3351,3352,3353,3354,3355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521], visible=False, arg3=0, arg4=0, arg5=0)
        move_user(mapId=61000003, portalId=99, boxId=104)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 우승자카메라연출()


class 우승자카메라연출(state.State):
    def on_enter(self):
        set_event_ui(type=3, arg2='$61000011_ME__WINNER_IS$', arg3='5000', arg4='105')
        set_event_ui(type=3, arg2='$61000011_ME__ENVY_IS$', arg3='5000', arg4='!105')
        mini_game_camera_direction(boxId=105, cameraId=301)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_local_camera(cameraId=301, enable=False)
            return 완료보상()


class 완료보상(state.State):
    def on_enter(self):
        widget_action(type='OxQuizUGC', func='EndGame')
        end_mini_game(winnerBoxId=105, gameName='oxquiz_ugc', isOnlyWinner='1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 성공알림()


class 종료(state.State):
    def on_enter(self):
        widget_action(type='OxQuizUGC', func='EndGame')
        end_mini_game(winnerBoxId=105, gameName='oxquiz_ugc', isOnlyWinner='1')
        set_effect(triggerIds=[608], visible=True)
        set_event_ui(type=0, arg2='0,0')
        set_event_ui(type=5, arg2='$61000011_ME__GAME_END_BY_ALL_RETIRED$', arg3='3000', arg4='0')
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 마무리()


class 성공알림(state.State):
    def on_enter(self):
        set_event_ui(type=7, arg2='$61000011_ME__MAIN__SUCCESS_IS$', arg3='3000', arg4='0')
        set_timer(timerId='40', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='40'):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        unset_mini_game_area_for_hack() # 해킹 보안 종료
        set_effect(triggerIds=[609], visible=True)
        set_event_ui(type=1, arg2='$61000011_ME__MAIN__GOODBYE$', arg3='3000', arg4='0')
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            widget_action(type='OxQuizUGC', func='MoveAllUser')
            return 대기()


