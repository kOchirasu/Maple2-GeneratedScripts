""" trigger/02020100_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.enable_spawn_point_pc(spawnId=2, isEnable=False)
        self.enable_spawn_point_pc(spawnId=3, isEnable=False)
        self.set_user_value(triggerId=99990002, key='Seed1start', value=0)
        self.set_user_value(triggerId=99990003, key='Seed2start', value=0)
        self.set_user_value(triggerId=99990004, key='Seed3start', value=0)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_ladder(triggerIds=[2001], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[2002], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[2003], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[2004], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[2005], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[2006], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[2007], visible=False, animationEffect=False, animationDelay=0)
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014], visible=False, arg3=0, delay=0)
        self.set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114], visible=True, arg3=0, delay=0)
        self.set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230], visible=True, arg3=0, delay=0)
        self.set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        self.set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        self.set_actor(triggerId=1403, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        self.set_actor(triggerId=1404, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        self.set_mesh(triggerIds=[1301,1302,1303,1304], visible=False, arg3=0, delay=0)
        self.set_interact_object(triggerIds=[10002109], state=0)
        self.set_interact_object(triggerIds=[10002110], state=0)
        self.set_interact_object(triggerIds=[10002111], state=0)
        self.set_interact_object(triggerIds=[10002112], state=0)
        self.set_interact_object(triggerIds=[10002113], state=0)
        self.set_interact_object(triggerIds=[10002115], state=0)
        self.set_interact_object(triggerIds=[10002116], state=0)
        self.set_interact_object(triggerIds=[10002122], state=0)
        self.set_breakable(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], enable=False)
        self.set_breakable(triggerIds=[5011,5012,5013,5014,5015,5016,5017,5018,5019], enable=False)
        self.set_agent(triggerIds=[9001], visible=True)
        self.set_agent(triggerIds=[9002], visible=True)
        self.set_agent(triggerIds=[9003], visible=True)
        self.set_agent(triggerIds=[9004], visible=True)
        self.set_agent(triggerIds=[9005], visible=True)
        self.set_agent(triggerIds=[9006], visible=True)
        self.set_agent(triggerIds=[9007], visible=True)
        self.set_agent(triggerIds=[9008], visible=True)
        self.set_agent(triggerIds=[9009], visible=True)
        self.set_agent(triggerIds=[9010], visible=True)
        self.set_agent(triggerIds=[9011], visible=True)
        self.set_agent(triggerIds=[9012], visible=True)
        self.set_agent(triggerIds=[9013], visible=True)
        self.set_agent(triggerIds=[9014], visible=True)
        self.set_agent(triggerIds=[9015], visible=True)
        self.set_agent(triggerIds=[9016], visible=True)
        self.set_agent(triggerIds=[9017], visible=True)
        self.set_agent(triggerIds=[9018], visible=True)
        self.set_agent(triggerIds=[9019], visible=True)
        self.set_agent(triggerIds=[9020], visible=True)
        self.set_agent(triggerIds=[9021], visible=True)
        self.set_agent(triggerIds=[9022], visible=True)
        self.set_agent(triggerIds=[9023], visible=True)
        self.set_agent(triggerIds=[9024], visible=True)
        self.set_agent(triggerIds=[9025], visible=True)
        self.set_agent(triggerIds=[9026], visible=True)
        self.set_agent(triggerIds=[9027], visible=True)
        self.set_agent(triggerIds=[9028], visible=True)
        self.set_agent(triggerIds=[9029], visible=True)
        self.set_agent(triggerIds=[9030], visible=True)
        self.set_agent(triggerIds=[9031], visible=True)
        self.set_agent(triggerIds=[9032], visible=True)
        self.set_agent(triggerIds=[9033], visible=True)
        self.set_agent(triggerIds=[9034], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_agent(triggerIds=[9005], visible=False)
        self.set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114], visible=False, arg3=0, delay=0)
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201]):
            return 씨앗체험(self.ctx)


class 씨앗체험(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9006], visible=False)
        self.set_agent(triggerIds=[9007], visible=False)
        self.set_agent(triggerIds=[9008], visible=False)
        self.set_agent(triggerIds=[9009], visible=False)
        self.set_mesh(triggerIds=[1007,1008,1009,1010], visible=True, arg3=0, delay=250, scale=3)
        self.create_monster(spawnIds=[202,203,204,205], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[202,203,204,205]):
            return 씨앗체험_씨앗들기(self.ctx)


class 씨앗체험_씨앗들기(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020100_BF__MAIN__0$', arg3='5000')
        self.set_user_value(triggerId=99990005, key='Seed0start', value=1)
        # <action name="오브젝트반응설정한다" arg1="10002115" arg2="1" />
        # <action name="메쉬를설정한다" arg1="1301" arg2="1" arg3="0" arg4="0" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed0interact', value=1):
            return 씨앗체험_나무심기(self.ctx)
        """
        <condition name="오브젝트가반응했으면" arg1="10002115" arg2="0" >
            <transition state="씨앗체험_나무심기"/>    
        </condition>
        """


class 씨앗체험_나무심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002116], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002116], stateValue=0):
            self.set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_On')
            self.set_user_value(triggerId=99990005, key='Seed0start', value=2)
            return 씨앗체험_끝(self.ctx)


class 씨앗체험_끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9010], visible=False)
        self.set_agent(triggerIds=[9011], visible=False)
        self.set_agent(triggerIds=[9012], visible=False)
        self.set_agent(triggerIds=[9013], visible=False)
        self.set_mesh(triggerIds=[1011,1012,1013,1014], visible=True, arg3=0, delay=250, scale=3)
        self.create_monster(spawnIds=[207,208,209], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[207,208,209]):
            return 사다리활성화(self.ctx)


class 사다리활성화(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[2001], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[2002], visible=True, animationEffect=True, animationDelay=4)
        self.set_ladder(triggerIds=[2003], visible=True, animationEffect=True, animationDelay=6)
        self.set_ladder(triggerIds=[2004], visible=True, animationEffect=True, animationDelay=8)
        self.set_ladder(triggerIds=[2005], visible=True, animationEffect=True, animationDelay=10)
        self.set_ladder(triggerIds=[2006], visible=True, animationEffect=True, animationDelay=12)
        self.set_ladder(triggerIds=[2007], visible=True, animationEffect=True, animationDelay=14)
        self.create_monster(spawnIds=[210,211,212], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[210,211,212]):
            return 씨앗1_활성화(self.ctx)


class 씨앗1_활성화(trigger_api.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)
        self.set_user_value(triggerId=99990002, key='Seed1start', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed1interact', value=1):
            return 씨앗1_전투(self.ctx)


class 씨앗1_전투(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9014], visible=False)
        self.set_agent(triggerIds=[9015], visible=False)
        self.set_agent(triggerIds=[9016], visible=False)
        self.set_agent(triggerIds=[9017], visible=False)
        self.set_agent(triggerIds=[9018], visible=False)
        self.create_monster(spawnIds=[213,214,215,216], animationEffect=False)
        self.set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], visible=False, arg3=0, delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[213,214,215,216]):
            return 씨앗1_심기(self.ctx)


class 씨앗1_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9019], visible=False)
        self.set_agent(triggerIds=[9020], visible=False)
        self.set_agent(triggerIds=[9021], visible=False)
        self.set_agent(triggerIds=[9022], visible=False)
        self.set_mesh(triggerIds=[1001,1002,1003,1004], visible=True, arg3=0, delay=250, scale=3)
        self.set_interact_object(triggerIds=[10002112], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002112], stateValue=0):
            return 씨앗2_활성화(self.ctx)


class 씨앗2_활성화(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9023], visible=False)
        self.set_agent(triggerIds=[9024], visible=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.enable_spawn_point_pc(spawnId=2, isEnable=True)
        self.set_user_value(triggerId=99990002, key='Seed1start', value=2)
        self.set_user_value(triggerId=99990003, key='Seed2start', value=1)
        self.set_mesh(triggerIds=[1005,1006], visible=True, arg3=0, delay=250, scale=3)
        self.set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed2interact', value=1):
            return 씨앗2_전투(self.ctx)


class 씨앗2_전투(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9025], visible=False)
        self.set_agent(triggerIds=[9026], visible=False)
        self.set_agent(triggerIds=[9027], visible=False)
        self.set_agent(triggerIds=[9028], visible=False)
        self.set_agent(triggerIds=[9029], visible=False)
        self.set_event_ui(type=1, arg2='$02020100_BF__MAIN__1$', arg3='5000')
        self.create_monster(spawnIds=[111,112,113,114,115,116], animationEffect=False)
        self.set_mesh(triggerIds=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], visible=False, arg3=0, delay=0)
        self.set_interact_object(triggerIds=[10002113], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002113], stateValue=0):
            return 발판1_지역감지(self.ctx)


class 발판1_지역감지(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9030], visible=False)
        self.set_agent(triggerIds=[9031], visible=False)
        self.set_agent(triggerIds=[9032], visible=False)
        self.set_agent(triggerIds=[9033], visible=False)
        self.set_agent(triggerIds=[9034], visible=False)
        self.set_actor(triggerId=1403, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        self.set_mesh(triggerIds=[1221,1222,1223,1224,1225,1226,1227,1228,1229,1230], visible=False, arg3=0, delay=0)
        self.destroy_monster(spawnIds=[111,112,113,114,115,116])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[903]):
            return 발판1_활성화대기(self.ctx)


class 발판1_활성화대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[225,226], animationEffect=False)
        self.set_user_value(triggerId=99990003, key='Seed2start', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed3interact', value=1):
            return 발판1_몬스터처리(self.ctx)
        if self.monster_dead(boxIds=[225,226]):
            return 발판1_몬스터처리(self.ctx)


class 발판1_몬스터처리(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990004, key='Seed3start', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed3interact', value=1):
            return 발판1_활성화(self.ctx)


class 발판1_활성화(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002122], state=1)
        self.enable_spawn_point_pc(spawnId=2, isEnable=False)
        self.enable_spawn_point_pc(spawnId=3, isEnable=True)
        self.create_monster(spawnIds=[121,122,123,124], animationEffect=False)
        self.set_breakable(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], enable=True)
        self.set_breakable(triggerIds=[5011,5012,5013,5014,5015,5016,5017,5018,5019], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteClear', value=1):
            return 보스전(self.ctx)


class 보스전(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990005, key='Seed4start', value=2)
        self.destroy_monster(spawnIds=[111,112,113,114,115,116,117,118,119])
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
