""" trigger/02020025_bf/main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9001], visible=True)
        self.set_agent(triggerIds=[9002], visible=True)
        self.set_agent(triggerIds=[9003], visible=True)
        self.set_agent(triggerIds=[9004], visible=True)
        self.set_agent(triggerIds=[9005], visible=True)
        self.set_agent(triggerIds=[9006], visible=True)
        self.set_agent(triggerIds=[9007], visible=True)
        self.set_agent(triggerIds=[9008], visible=True)
        self.destroy_monster(spawnIds=[-1])
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_user_value(triggerId=99990004, key='Timer', value=0) # <일반 5분 타이머>
        self.set_user_value(triggerId=99990006, key='SpecialTimer', value=0) # <3분내 클리어 특별 타이머>
        self.set_user_value(triggerId=99990002, key='battlesetting', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.move_user(mapId=2020025, portalId=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라_캡션(self.ctx)


class 카메라_캡션(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[5001,5002], returnView=True)
        self.show_caption(type='VerticalCaption', title='$02020025_BF__main__3$', desc='$02020025_BF__main__4$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 유저연출(self.ctx)


class 유저연출(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202])
        self.set_conversation(type=1, spawnId=0, script='$02020025_BF__main__5$', arg4=5, arg5=0)
        self.select_camera(triggerId=503, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_콘대르설명1(self.ctx)


class 카메라_콘대르설명1(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Talk_B', duration=18430)
        self.add_cinematic_talk(npcId=24110001, msg='$02020025_BF__main__0$', duration=4000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 유저연출_2(self.ctx)


class 유저연출_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$02020025_BF__main__6$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 유저연출_3(self.ctx)


class 유저연출_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=504, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라_콘대르설명2(self.ctx)


class 카메라_콘대르설명2(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=24110001, illustId='Conder_normal', msg='$02020025_BF__main__1$', duration=4000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_콘대르설명3(self.ctx)


class 카메라_콘대르설명3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=24110001, illustId='Conder_normal', msg='$02020025_BF__main__2$', duration=4000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_콘대르설명4(self.ctx)


class 카메라_콘대르설명4(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=24110001, illustId='Conder_normal', msg='$02020025_BF__main__7$', duration=4000, align='left')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.1)
        self.destroy_monster(spawnIds=[202])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=False, animationDelay=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 전투_진행(self.ctx)


class 전투_진행(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_agent(triggerIds=[9005], visible=False)
        self.set_agent(triggerIds=[9006], visible=False)
        self.set_agent(triggerIds=[9007], visible=False)
        self.set_agent(triggerIds=[9008], visible=False)
        self.set_user_value(triggerId=99990002, key='battlesetting', value=1)
        # <action name="SetUserValue" triggerID="99990004" key="Timer" value="1"/>
        # <action name="SetUserValue" triggerID="99990002" key="SpecialTimer" value="1"/>
        # <action name="SetUserValue" triggerID="99990006" key="SpecialTimer" value="1"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End', value=1):
            return 랭크체크대사(self.ctx)


class 랭크체크대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_first_user_mission_score(score=1500, operator='GreaterEqual'):
            self.side_npc_talk(npcId=24110001, illust='Conder_normal', duration=5000, script='$02020025_BF__main__8$', voice='ko/Npc/00002146')
            return 던전종료_A랭크이상(self.ctx)
        if self.dungeon_first_user_mission_score(score=1500, operator='Less'):
            self.side_npc_talk(npcId=24110001, illust='Conder_smile', duration=5000, script='$02020025_BF__main__9$', voice='ko/Npc/00002145')
            return 던전종료_A랭크미만(self.ctx)


class 던전종료_A랭크이상(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])
        self.dungeon_clear()


class 던전종료_A랭크미만(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])
        self.dungeon_fail()


initial_state = 입장
