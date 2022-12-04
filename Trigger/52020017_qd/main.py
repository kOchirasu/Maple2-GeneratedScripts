""" trigger/52020017_qd/main.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200115], questStates=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.create_monster(spawnIds=[204], animationEffect=True)
        self.create_monster(spawnIds=[205], animationEffect=True)
        self.create_monster(spawnIds=[206], animationEffect=True)
        self.create_monster(spawnIds=[207], animationEffect=True)
        self.create_monster(spawnIds=[208], animationEffect=True)
        self.create_monster(spawnIds=[209], animationEffect=True)
        self.create_monster(spawnIds=[210], animationEffect=True)
        self.create_monster(spawnIds=[211], animationEffect=True)
        self.create_monster(spawnIds=[212], animationEffect=True)
        self.create_monster(spawnIds=[213], animationEffect=True)
        self.create_monster(spawnIds=[214], animationEffect=True)
        self.create_monster(spawnIds=[215], animationEffect=True)
        self.create_monster(spawnIds=[216], animationEffect=True)
        self.create_monster(spawnIds=[217], animationEffect=True)
        self.create_monster(spawnIds=[218], animationEffect=True)
        self.create_monster(spawnIds=[219], animationEffect=True)
        self.create_monster(spawnIds=[220], animationEffect=True)
        self.create_monster(spawnIds=[301], animationEffect=True)
        self.create_monster(spawnIds=[302], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[60200115], questStates=[1]):
            return Object_Off(self.ctx)


class Object_Off(trigger_api.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[0,0,0])
        self.create_monster(spawnIds=[101], animationEffect=True) # 엘레나
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_interact_object(triggerIds=[10001282], state=0)
        self.add_balloon_talk(spawnId=0, msg='!', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Event_Start(self.ctx)


class Event_Start(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003624, msg='아아…. 드디어 극의 주인공을 찾은 것 같네.', duration=2800, align='left')
        self.set_scene_skip(action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_A_01(self.ctx)


class Event_A_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='!?', duration=1800, illustId='0', align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_A_02(self.ctx)


class Event_A_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.add_cinematic_talk(npcId=11003624, msg='그래. 바로 너. 네가 주인공이야.', duration=2800, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_A_03(self.ctx)


class Event_A_03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3001')
        self.add_cinematic_talk(npcId=11003624, msg='참, 주인공 역할을 말해주지 않았구나.', duration=2800, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_A_04(self.ctx)


class Event_A_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003624, msg='이 극의 주인공 역할은 말이야.', duration=1800, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_A_05(self.ctx)


class Event_A_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True)
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.add_cinematic_talk(npcId=11003624, msg='여기서 죽는 거야.', duration=2800, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_A_06(self.ctx)


class Event_A_06(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003624, msg='자, 그럼 극을 시작해볼까?', duration=2800, illustId='RobotMaidBrownHair_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_A_End(self.ctx)


class Event_A_Skip_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True) # 엘레나

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_A_Skip_02(self.ctx)


class Event_A_Skip_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3001')
        self.set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_A_End(self.ctx)


class Event_A_End(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_ambient_light(primary=[1,1,1])
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_balloon_talk(spawnId=0, msg='!', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle_A_Ready(self.ctx)


class Battle_A_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle_A(self.ctx)


class Battle_A(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=201, addSpawnId=601)
        self.change_monster(removeSpawnId=202, addSpawnId=602)
        self.change_monster(removeSpawnId=203, addSpawnId=603)
        self.change_monster(removeSpawnId=204, addSpawnId=604)
        self.change_monster(removeSpawnId=205, addSpawnId=605)
        self.change_monster(removeSpawnId=206, addSpawnId=606)
        self.change_monster(removeSpawnId=207, addSpawnId=607)
        self.change_monster(removeSpawnId=208, addSpawnId=608)
        self.change_monster(removeSpawnId=209, addSpawnId=609)
        self.change_monster(removeSpawnId=210, addSpawnId=610)
        self.change_monster(removeSpawnId=211, addSpawnId=611)
        self.change_monster(removeSpawnId=212, addSpawnId=612)
        self.change_monster(removeSpawnId=213, addSpawnId=613)
        self.change_monster(removeSpawnId=214, addSpawnId=614)
        self.change_monster(removeSpawnId=215, addSpawnId=615)
        self.change_monster(removeSpawnId=216, addSpawnId=616)
        self.change_monster(removeSpawnId=217, addSpawnId=617)
        self.change_monster(removeSpawnId=218, addSpawnId=618)
        self.change_monster(removeSpawnId=219, addSpawnId=619)
        self.change_monster(removeSpawnId=220, addSpawnId=620)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620]):
            return Battle_B_Ready(self.ctx)


class Battle_B_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle_B(self.ctx)


class Battle_B(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=301, addSpawnId=701)
        self.change_monster(removeSpawnId=302, addSpawnId=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[701,702]):
            return Battle_End(self.ctx)


class Battle_End(trigger_api.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[1,1,1])
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.destroy_monster(spawnIds=[101])
        self.set_interact_object(triggerIds=[10001282], state=1)


initial_state = Idle
