""" trigger/52100300_qd/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='Spawn', value=0)
        self.set_user_value(triggerId=99990003, key='RandomBomb', value=0)
        self.set_user_value(triggerId=99990004, key='Laser', value=0)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10002185], state=0) # 엘리베이터 발판
        self.enable_spawn_point_pc(spawnId=100, isEnable=True) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawnId=101, isEnable=False)
        self.enable_spawn_point_pc(spawnId=102, isEnable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[901]):
            return 연출시작(self.ctx)


# 연출시작
class 연출시작(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52100300, portalId=5001)
        self.create_monster(spawnIds=[351])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작_2(self.ctx)


class 연출시작_2(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4004,4005], returnView=False)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2900):
            return 연출시작_2_02(self.ctx)


class 연출시작_2_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006,4007], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출시작_2_03(self.ctx)


class 연출시작_2_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작_3(self.ctx)


class 연출시작_3(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4001,4002], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52100300_QD__MAIN__12$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출시작_4(self.ctx)


class 연출시작_4(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52100300_QD__MAIN__13$', duration=3500)
        self.add_cinematic_talk(npcId=11004682, illustId='11004022', align='right', msg='$52100300_QD__MAIN__14$', duration=3500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 연출시작_5(self.ctx)


class 연출시작_5(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=351, patrolName='MS2PatrolData_3001')
        self.add_cinematic_talk(npcId=11004682, illustId='11004022', align='right', msg='$52100300_QD__MAIN__15$', duration=3500)
        self.add_cinematic_talk(npcId=0, msg='$52100300_QD__MAIN__16$', duration=3500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 연출시작_6(self.ctx)


class 연출시작_6(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[351], arg2=False)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작_7(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[351])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작_7(self.ctx)


class 연출시작_7(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[902]):
            self.set_event_ui(type=1, arg2='$52100300_QD__MAIN__0$', arg3='5000')
            self.create_monster(spawnIds=[101,102,103], animationEffect=False)
            return 추가대사_01(self.ctx)


class 추가대사_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_user_value(triggerId=99990004, key='Laser', value=1)
            self.side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$52100300_QD__MAIN__1$', duration=5000)
            return 추가대사_02(self.ctx)


class 추가대사_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101,102,103]):
            self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__2$', duration=5000)
            return 추가대사_03(self.ctx)


class 추가대사_03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_normal', script='$52100300_QD__MAIN__3$', duration=5000)
            return 엘리베이터_체크(self.ctx)


class 엘리베이터_체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__4$', duration=5000)
            return 엘리베이터_스위치(self.ctx)


class 엘리베이터_스위치(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002185], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002185], stateValue=0):
            return 엘리베이터_활성화(self.ctx)


class 엘리베이터_활성화(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[5001], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[903]):
            return 아르케온_탑승_가이드(self.ctx)


class 아르케온_탑승_가이드(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52100300_QD__MAIN__5$', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[711]):
            return 레이저_패턴_시작(self.ctx)


class 레이저_패턴_시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[904]):
            return 갈림길_전투(self.ctx)


class 갈림길_전투(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201,202,203,204], animationEffect=False)
        self.set_actor(triggerId=9001, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        self.set_mesh(triggerIds=[1001], visible=True)
        self.enable_spawn_point_pc(spawnId=100, isEnable=False) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawnId=101, isEnable=True)
        self.enable_spawn_point_pc(spawnId=102, isEnable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[905]):
            return 짜투리_전투(self.ctx)


class 짜투리_전투(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,302,303,304], animationEffect=False)
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=True)
        self.set_mesh(triggerIds=[30000,30010,30020,30030], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[911]):
            return 웨이브_시작(self.ctx)


class 웨이브_시작(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_unfair', script='$52100300_QD__MAIN__6$', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 추가대사_04(self.ctx)


class 추가대사_04(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='Spawn', value=1)
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=False)
        self.set_mesh(triggerIds=[30000,30010,30020,30030], visible=False)
        self.side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$52100300_QD__MAIN__7$', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SpawnRoomEnd', value=1):
            self.set_actor(triggerId=9001, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_start')
            return 길열림(self.ctx)


class 길열림(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1001], visible=False)
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=True)
        self.set_mesh(triggerIds=[30000,30010,30020,30030], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[921]):
            return 지뢰방_시작(self.ctx)


class 지뢰방_시작(common.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=100, isEnable=False) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawnId=101, isEnable=False)
        self.enable_spawn_point_pc(spawnId=102, isEnable=True)
        self.set_actor(triggerId=9002, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        self.set_actor(triggerId=9003, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        self.set_actor(triggerId=9004, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        self.set_mesh(triggerIds=[5001], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003], visible=True)
        self.set_user_value(triggerId=99990003, key='RandomBomb', value=1)
        self.side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$52100300_QD__MAIN__8$', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 추가대사_05(self.ctx)


class 추가대사_05(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__9$', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 추가대사_06(self.ctx)


class 추가대사_06(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_normal', script='$52100300_QD__MAIN__10$', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RandomBombEnd', value=1):
            self.set_user_value(triggerId=99990004, key='Laser', value=0)
            return 보스전(self.ctx)


class 보스전(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__11$', duration=5000)
        self.set_actor(triggerId=9002, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_start')
        self.set_mesh(triggerIds=[3001], visible=False)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
