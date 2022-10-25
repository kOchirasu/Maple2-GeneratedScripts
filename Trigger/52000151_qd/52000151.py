""" trigger/52000151_qd/52000151.xml """
import common


# ########################씬7 파토스의 등장########################
class wait(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[50001642], questStates=[1]):
            return 생명의틈으로01(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[3]):
            return 생틈퀘수령전대기(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[2]):
            return 생틈퀘수령전대기(self.ctx)
        if self.quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[1]):
            return 파토스등장연출01(self.ctx)
        """
        <condition name="유저를감지했으면" arg1="10010">
                <transition state="파토스등장연출01"/>
            </condition>
        """


class wait_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10010]):
            return 파토스등장연출01(self.ctx)


class 생틈퀘수령전대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=False) # 케이틀린
        self.create_monster(spawnIds=[200], animationEffect=False) # 아노스
        self.create_monster(spawnIds=[201], animationEffect=False) # 호르헤
        self.set_npc_emotion_loop(spawnId=200, sequenceName='Event_01_A', duration=999999)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[50001642], questStates=[1]):
            return 생명의틈으로01(self.ctx)


class 파토스등장연출01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_monster(spawnIds=[202], animationEffect=False) # 케이틀린
        self.create_monster(spawnIds=[200], animationEffect=False) # 아노스
        self.create_monster(spawnIds=[201], animationEffect=False) # 호르헤
        self.create_monster(spawnIds=[203], animationEffect=False) # 파토스
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Stun_A', duration=999999)
        self.face_emotion(spawnId=201, emotionName='Concerned')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 파토스등장연출02(self.ctx)


class 파토스등장연출02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='exit')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 파토스등장연출02_B(self.ctx)


class 파토스등장연출02_B(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3000,3001], returnView=False)
        self.set_effect(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107], visible=True, arg3=0, arg4=100)
        self.set_effect(triggerIds=[1200,1201,1202,1203,1204,1205,1206], visible=True, arg3=0, arg4=100)
        self.set_effect(triggerIds=[1300,1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311], visible=True, arg3=0, arg4=100)
        self.set_effect(triggerIds=[1400,1401,1402,1403,1404,1405,1406,1407,1408,1409], visible=True, arg3=0, arg4=100)
        self.set_effect(triggerIds=[1500,1501,1502,1503,1504,1505,1506,1507,1508], visible=True, arg3=0, arg4=100)
        self.set_effect(triggerIds=[1600,1601,1602,1603,1604,1605,1606,1607,1608], visible=True, arg3=0, arg4=100)
        self.set_effect(triggerIds=[1700,1701,1702,1703,1704], visible=True, arg3=0, arg4=100)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출03(self.ctx)


class 파토스등장연출03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003439, illustId='0', msg='$52000151_QD__52000151__0$', duration=4000, align='right') # 호르헤 대사
        self.select_camera_path(pathIds=[7000,7001], returnView=False)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_B') # 호르헤

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출04(self.ctx)


class 파토스등장연출04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003442, illustId='0', msg='$52000151_QD__52000151__1$', duration=4000, align='right') # 케이틀린 대사
        self.select_camera_path(pathIds=[7002,7003], returnView=False) # 아노스 선생님이 두명…?!

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출05(self.ctx)


class 파토스등장연출05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__2$', duration=4000, align='right') # 파토스 대사
        self.select_camera_path(pathIds=[7004,7005], returnView=False)
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Bore_A') # 파토스

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출06(self.ctx)


class 파토스등장연출06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__3$', duration=4000, align='right') # 파토스 대사
        self.select_camera_path(pathIds=[7006,7007], returnView=False)
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_patos_come') # 내 이름은 파토스. 빛의 이노센트 따위와 이름을 섞고 싶지 않군.

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출08(self.ctx)


class 파토스등장연출08(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__4$', duration=4000, align='right') # 파토스 대사
        self.select_camera_path(pathIds=[7008,7009], returnView=False) # 난 어둠의 이노센트다. 그래, 빛의 위선을 뚫고 나온 이 세상의 진정한 힘이지…

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출09(self.ctx)


class 파토스등장연출09(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003442, illustId='0', msg='$52000151_QD__52000151__5$', duration=4000, align='right') # 파토스 대사
        self.select_camera_path(pathIds=[7010,7011], returnView=False) # 어둠의…이노센트?!

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출10(self.ctx)


class 파토스등장연출10(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003439, illustId='0', msg='$52000151_QD__52000151__6$', duration=4000, align='right') # 호르헤 대사
        self.select_camera_path(pathIds=[7000,7001], returnView=False)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A') # 호르헤

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출12(self.ctx)


class 파토스등장연출12(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003439, illustId='0', msg='$52000151_QD__52000151__7$', duration=4000, align='right') # 호르헤 대사
        self.select_camera_path(pathIds=[7012,7013,7014,7015], returnView=False) # 하지만 어둠의 이노센트라니…이노센트는 하나가 아니었나…?

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출13(self.ctx)


class 파토스등장연출13(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__8$', duration=4000, align='right') # 파토스 대사
        self.select_camera_path(pathIds=[7016,7017], returnView=False) # 훗…하나?

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 파토스등장연출14(self.ctx)


class 파토스등장연출14(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__9$', duration=4000, align='right') # 파토스 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 파토스등장연출15(self.ctx)


class 파토스등장연출15(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__10$', duration=4000, align='right') # 파토스 대사
        self.select_camera_path(pathIds=[7018,7019], returnView=False) # 우린 하나가 아니다.

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 파토스등장연출16(self.ctx)


class 파토스등장연출16(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__11$', duration=4000, align='right') # 파토스 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 파토스등장연출17(self.ctx)


class 파토스등장연출17(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__12$', duration=4000, align='right') # 파토스 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 파토스등장연출18(self.ctx)


class 파토스등장연출18(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__13$', duration=4000, align='right') # 파토스 대사
        self.select_camera_path(pathIds=[7020,7021], returnView=False) # 뭐…그것도 잠시 일 테지.생명의 틈만 있다면, 빛의 이노센트도 내 몸이 될 것이다.
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_patos_exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 파토스등장연출19(self.ctx)


class 파토스등장연출19(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__14$', duration=4000, align='right') # 파토스 대사
        self.select_camera_path(pathIds=[7022,7023], returnView=False)
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_patos_turn') # 크큭…빛의 이노센트여.날 거부하지 마라.

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출20(self.ctx)


class 파토스등장연출20(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003441, illustId='0', msg='$52000151_QD__52000151__15$', duration=4000, align='right') # 케이틀린 대사
        self.select_camera_path(pathIds=[7024,7025], returnView=False)
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Attack_01_A') # 파토스

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출21(self.ctx)


class 파토스등장연출21(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 파토스등장연출22(self.ctx)


class 파토스등장연출22(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_anosTurn')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 파토스등장연출23(self.ctx)


class 파토스등장연출23(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_achievement(triggerId=10010, type='trigger', achieve='ProtectFinish') # 50001641 퀘스트 완료 업적
        self.set_npc_emotion_loop(spawnId=200, sequenceName='Event_01_A', duration=999999)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.set_sound(triggerId=9000, enable=True) # 전투 상황 브금
        self.destroy_monster(spawnIds=[203])

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[50001642], questStates=[1]):
            return 생명의틈으로01(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_npc_emotion_loop(spawnId=200, sequenceName='Event_01_A', duration=999999)
        self.reset_camera(interpolationTime=0)
        self.set_sound(triggerId=9000, enable=True) # 전투 상황 브금
        self.destroy_monster(spawnIds=[203])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Skip_1_1(self.ctx)


class Skip_1_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=10010, type='trigger', achieve='ProtectFinish') # 50001641 퀘스트 완료 업적

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10010], questIds=[50001642], questStates=[1]):
            return 생명의틈으로01(self.ctx)


class 생명의틈으로01(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000172, portalId=21002)


initial_state = wait
