""" trigger/83000003_colosseum/start.xml """
import common


class 유저감지(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2001], jobCode=0):
            return 연출준비(self.ctx)


class 연출준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.destroy_monster(spawnIds=[202])
        self.destroy_monster(spawnIds=[203])
        self.create_monster(spawnIds=[203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출_01(self.ctx)


class 연출_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출_01_01(self.ctx)


class 연출_01_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4002], returnView=False)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 연출_02(self.ctx)


class 연출_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003,4004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출_03(self.ctx)


class 연출_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출_05(self.ctx)


class 연출_05(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4005,4006], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출_07(self.ctx)


class 연출_07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4007,4008], returnView=False)
        self.show_caption(type='VerticalCaption', title='$83000002_COLOSSEUM__START__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_cinematic_ui(type=0)
            self.reset_camera(interpolationTime=0)
            return 연출끝_01(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4009], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_cinematic_ui(type=0)
            self.reset_camera(interpolationTime=0)
            return 대화딜레이(self.ctx)


class 대화딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return 연출끝_01(self.ctx)


class 연출끝_01(common.Trigger):
    def on_enter(self):
        self.talk_npc(spawnId=203)
        # <action name="DebugString" string="라운드 클리어 테스트 합니다. 현재 5라운드 클리어로 설정됩니다." />
        # <action name="DungeonClearRound" round="5" />
        # <action name="DungeonClear" />

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[902]):
            self.move_user_to_pos(pos=[300,-225,1500], rot=[0,0,270])
            return 대화딜레이(self.ctx)
        if self.user_value(key='DungeonPlayType', value=1):
            return NewGame(self.ctx)
        if self.user_value(key='DungeonPlayType', value=2):
            return ContinueGame(self.ctx)


class NewGame(common.Trigger):
    def on_enter(self):
        self.debug_string(string='새로 시작하기를 설정했습니다.')
        self.set_user_value(triggerId=900001, key='MainStart', value=1)


class ContinueGame(common.Trigger):
    def on_enter(self):
        self.debug_string(string='이어하기를 설정했습니다.')
        self.dungeon_disable_ranking()
        self.set_user_value(triggerId=900001, key='MainStart', value=2)


initial_state = 유저감지
