""" trigger/52000124_qd/main.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100105,60100106,60100107,60100108,60100109,60100110], questStates=[2]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60100110], questStates=[3]):
            return delnpc(self.ctx)


# 준비
class ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202], animationEffect=True) # 연출용 카트반 (11003195)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return camera(self.ctx)


class camera(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=4001, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_01(self.ctx)


# 이벤트 씬 시작
class scene_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4002], returnView=False)
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003195, msg='$52000124_QD__MAIN__0$', duration=2000, align='right')
        self.set_scene_skip(state=scene_07, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_02(self.ctx)


class scene_02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003195, msg='$52000124_QD__MAIN__1$', duration=2000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03(self.ctx)


class scene_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.add_cinematic_talk(npcId=11000069, msg='$52000124_QD__MAIN__2$', duration=2000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_04(self.ctx)


class scene_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_3001')
        self.add_cinematic_talk(npcId=11003195, msg='$52000124_QD__MAIN__3$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_05(self.ctx)


class scene_05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Sit_down_A', duration=1E+12)
        self.add_cinematic_talk(npcId=11000069, msg='$52000124_QD__MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_06(self.ctx)


class scene_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.add_cinematic_talk(npcId=11003195, msg='$52000124_QD__MAIN__5$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_07(self.ctx)


class scene_07(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True) # 카트반(11003196)
        self.destroy_monster(spawnIds=[202]) # 연출용 카트반(11003195)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100110], questStates=[2]):
            return warptalk(self.ctx)


class warptalk(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=201, msg='$52000124_QD__MAIN__6$', duration=2000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return warp(self.ctx)


class warp(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000073, portalId=4)


# delnpc
class delnpc(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201,202])


initial_state = idle
