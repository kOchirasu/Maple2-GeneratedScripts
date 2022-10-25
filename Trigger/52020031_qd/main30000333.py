""" trigger/52020031_qd/main30000333.xml """
import common


# 제단 입장
# 예상치 못한 인물 하렌(11003747) - spawnpoint : 1 
# 한순간의 방심 하렌(11003749) - spawnpoint : 2
# 연출용 하렌(11003756) - spawnpoint : 101
class idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[30000333], questStates=[1]):
            return 두번째연출준비(self.ctx)


class 두번째연출준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 두번째연출준비_01(self.ctx)


class 두번째연출준비_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[102]) # 퀘스트용 하렌
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째연출준비_02(self.ctx)


class 두번째연출준비_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020031, portalId=6001)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째연출(self.ctx)


class 두번째연출(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=0, msg='천공의 심장을 돌려줘.', duration=3000)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3200):
            return 두번째연출_01(self.ctx)


class 두번째연출_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 두번째연출_02(self.ctx)


class 두번째연출_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003756, msg='곱게 가져갈 수 있을 거라고 생각해?', duration=3000)
        self.add_cinematic_talk(npcId=11003756, msg='꿈도 야무지다니까... 호호호', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 두번째연출_03(self.ctx)


class 두번째연출_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4012], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째연출전투준비_01(self.ctx)


class 두번째연출전투준비_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 두번째연출전투준비(self.ctx)


class 두번째연출전투준비(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=2) # UI 숨기기 초기화
        self.set_cinematic_ui(type=0) # 유저 이동 가능하게

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 두번째연출전투준비1(self.ctx)


class 두번째연출전투준비1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[601], animationEffect=False) # 몬스터 하렌
        self.set_event_ui(type=1, arg2='하렌을 처치하세요!', arg3='2000', arg4='0')
        self.add_balloon_talk(spawnId=601, msg='숨통을 끊어주마.', duration=3000, delayTick=3000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[601]):
            return 두번째연출전투종료1(self.ctx)


class 두번째연출전투종료1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0.5)
        self.move_user(mapId=52020031, portalId=6001)
        self.destroy_monster(spawnIds=[601])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째연출전투종료2(self.ctx)


class 두번째연출전투종료2(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
