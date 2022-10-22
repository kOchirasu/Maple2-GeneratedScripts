""" trigger/83000003_colosseum/start.xml """
from common import *
import state


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001], jobCode=0):
            return 연출준비()


class 연출준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        destroy_monster(spawnIds=[202])
        destroy_monster(spawnIds=[203])
        create_monster(spawnIds=[203], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출_01()


class 연출_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출_01_01()


class 연출_01_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출_02()


class 연출_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003,4004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출_03()


class 연출_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출_05()


class 연출_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4005,4006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출_07()


class 연출_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007,4008], returnView=False)
        show_caption(type='VerticalCaption', title='$83000002_COLOSSEUM__START__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_cinematic_ui(type=0)
            reset_camera(interpolationTime=0)
            return 연출끝_01()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_cinematic_ui(type=0)
            reset_camera(interpolationTime=0)
            return 대화딜레이()


class 대화딜레이(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 연출끝_01()


class 연출끝_01(state.State):
    def on_enter(self):
        talk_npc(spawnId=203)
        # <action name="DebugString" string="라운드 클리어 테스트 합니다. 현재 5라운드 클리어로 설정됩니다." />
        # <action name="DungeonClearRound" round="5" />
        # <action name="DungeonClear" />

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902]):
            move_user_to_pos(pos=[300,-225,1500], rot=[0,0,270])
            return 대화딜레이()
        if user_value(key='DungeonPlayType', value=1):
            return NewGame()
        if user_value(key='DungeonPlayType', value=2):
            return ContinueGame()


class NewGame(state.State):
    def on_enter(self):
        debug_string(string='새로 시작하기를 설정했습니다.')
        set_user_value(triggerId=900001, key='MainStart', value=1)


class ContinueGame(state.State):
    def on_enter(self):
        debug_string(string='이어하기를 설정했습니다.')
        dungeon_disable_ranking()
        set_user_value(triggerId=900001, key='MainStart', value=2)


