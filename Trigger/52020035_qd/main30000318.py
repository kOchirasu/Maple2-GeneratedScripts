""" trigger/52020035_qd/main30000318.xml """
import trigger_api


# 퀘스트 수락 후 연출 시작
class idle3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[703], questIds=[30000318], questStates=[2]):
            return 연출시작3(self.ctx)


# 라딘과 대화 시작
class 연출시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=8, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출시작3_1(self.ctx)


class 연출시작3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(isVisible=False)
        self.destroy_monster(spawnIds=[117])
        self.destroy_monster(spawnIds=[118])
        self.destroy_monster(spawnIds=[119])
        self.destroy_monster(spawnIds=[120])
        self.destroy_monster(spawnIds=[121])
        self.create_monster(spawnIds=[110], animationEffect=False, animationDelay=0) # 연출라딘
        self.create_monster(spawnIds=[117], animationEffect=False, animationDelay=0) # 연출웨이홍
        self.create_monster(spawnIds=[118], animationEffect=False, animationDelay=0) # 연출브리드민
        self.create_monster(spawnIds=[119], animationEffect=False, animationDelay=0) # 연출바사라첸
        self.create_monster(spawnIds=[120], animationEffect=False, animationDelay=0) # 연출하렌
        self.create_monster(spawnIds=[121], animationEffect=False, animationDelay=0) # 연출카일
        self.select_camera_path(pathIds=[4026], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 뒷이야기(self.ctx)


class 뒷이야기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=8, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003754, msg='크크큭... 착한 연기 잘 하는군. 라딘.', duration=3000)
        self.set_scene_skip(state=끝, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 뒷이야기01(self.ctx)


class 뒷이야기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4028], returnView=False)
        self.add_cinematic_talk(npcId=11003753, msg='...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 뒷이야기01(self.ctx)


class 뒷이야기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4030], returnView=False)
        self.set_npc_emotion_sequence(spawnId=119, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003756, msg='훗. 생각보다 잘 넘어간 것 같군요.', duration=3000)
        self.add_cinematic_talk(npcId=11003759, msg='쳇, 복잡하게 만들지 말고 그냥 죽어버리면 되잖아?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 뒷이야기02(self.ctx)


class 뒷이야기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4026], returnView=False)
        self.add_cinematic_talk(npcId=11003754, msg='하렌. 그럼 우리도 다음 작전을 이야기 해 볼까.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 뒷이야기02_1(self.ctx)


class 뒷이야기02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4031], returnView=False)
        self.move_npc(spawnId=119, patrolName='MS2PatrolData_3008')
        self.add_cinematic_talk(npcId=11003756, msg='...후훗.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=9, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=9, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=2020012, portalId=1)
        self.destroy_monster(spawnIds=[111])
        self.destroy_monster(spawnIds=[112])
        self.destroy_monster(spawnIds=[113])
        self.destroy_monster(spawnIds=[114])
        self.destroy_monster(spawnIds=[115])


initial_state = idle3
