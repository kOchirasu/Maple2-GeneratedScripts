""" trigger/02020100_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        enable_spawn_point_pc(spawnId=3, isEnable=False)
        set_user_value(triggerId=99990002, key='Seed1start', value=0)
        set_user_value(triggerId=99990003, key='Seed2start', value=0)
        set_user_value(triggerId=99990004, key='Seed3start', value=0)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_ladder(triggerIds=[2001], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[2002], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[2003], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[2004], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[2005], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[2006], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[2007], visible=False, animationEffect=False, animationDelay=0)
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114], visible=True, arg3=0, arg4=0)
        set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230], visible=True, arg3=0, arg4=0)
        set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_actor(triggerId=1403, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_actor(triggerId=1404, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_mesh(triggerIds=[1301,1302,1303,1304], visible=False, arg3=0, arg4=0)
        set_interact_object(triggerIds=[10002109], state=0)
        set_interact_object(triggerIds=[10002110], state=0)
        set_interact_object(triggerIds=[10002111], state=0)
        set_interact_object(triggerIds=[10002112], state=0)
        set_interact_object(triggerIds=[10002113], state=0)
        set_interact_object(triggerIds=[10002115], state=0)
        set_interact_object(triggerIds=[10002116], state=0)
        set_interact_object(triggerIds=[10002122], state=0)
        set_breakable(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], enabled=False)
        set_breakable(triggerIds=[5011,5012,5013,5014,5015,5016,5017,5018,5019], enabled=False)
        set_agent(triggerIds=[9001], visible=True)
        set_agent(triggerIds=[9002], visible=True)
        set_agent(triggerIds=[9003], visible=True)
        set_agent(triggerIds=[9004], visible=True)
        set_agent(triggerIds=[9005], visible=True)
        set_agent(triggerIds=[9006], visible=True)
        set_agent(triggerIds=[9007], visible=True)
        set_agent(triggerIds=[9008], visible=True)
        set_agent(triggerIds=[9009], visible=True)
        set_agent(triggerIds=[9010], visible=True)
        set_agent(triggerIds=[9011], visible=True)
        set_agent(triggerIds=[9012], visible=True)
        set_agent(triggerIds=[9013], visible=True)
        set_agent(triggerIds=[9014], visible=True)
        set_agent(triggerIds=[9015], visible=True)
        set_agent(triggerIds=[9016], visible=True)
        set_agent(triggerIds=[9017], visible=True)
        set_agent(triggerIds=[9018], visible=True)
        set_agent(triggerIds=[9019], visible=True)
        set_agent(triggerIds=[9020], visible=True)
        set_agent(triggerIds=[9021], visible=True)
        set_agent(triggerIds=[9022], visible=True)
        set_agent(triggerIds=[9023], visible=True)
        set_agent(triggerIds=[9024], visible=True)
        set_agent(triggerIds=[9025], visible=True)
        set_agent(triggerIds=[9026], visible=True)
        set_agent(triggerIds=[9027], visible=True)
        set_agent(triggerIds=[9028], visible=True)
        set_agent(triggerIds=[9029], visible=True)
        set_agent(triggerIds=[9030], visible=True)
        set_agent(triggerIds=[9031], visible=True)
        set_agent(triggerIds=[9032], visible=True)
        set_agent(triggerIds=[9033], visible=True)
        set_agent(triggerIds=[9034], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_agent(triggerIds=[9005], visible=False)
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114], visible=False, arg3=0, arg4=0)
        create_monster(spawnIds=[201], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            return 씨앗체험()


class 씨앗체험(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9006], visible=False)
        set_agent(triggerIds=[9007], visible=False)
        set_agent(triggerIds=[9008], visible=False)
        set_agent(triggerIds=[9009], visible=False)
        set_mesh(triggerIds=[1007,1008,1009,1010], visible=True, arg3=0, arg4=250, arg5=3)
        create_monster(spawnIds=[202,203,204,205], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[202,203,204,205]):
            return 씨앗체험_씨앗들기()


class 씨앗체험_씨앗들기(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020100_BF__MAIN__0$', arg3='5000')
        set_user_value(triggerId=99990005, key='Seed0start', value=1)
        # <action name="오브젝트반응설정한다" arg1="10002115" arg2="1" />
        # <action name="메쉬를설정한다" arg1="1301" arg2="1" arg3="0" arg4="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Seed0interact', value=1):
            return 씨앗체험_나무심기()
        """
        <condition name="오브젝트가반응했으면" arg1="10002115" arg2="0" >
            <transition state="씨앗체험_나무심기"/>    
        </condition>
        """


class 씨앗체험_나무심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002116], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002116], arg2=0):
            set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_On')
            set_user_value(triggerId=99990005, key='Seed0start', value=2)
            return 씨앗체험_끝()


class 씨앗체험_끝(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9010], visible=False)
        set_agent(triggerIds=[9011], visible=False)
        set_agent(triggerIds=[9012], visible=False)
        set_agent(triggerIds=[9013], visible=False)
        set_mesh(triggerIds=[1011,1012,1013,1014], visible=True, arg3=0, arg4=250, arg5=3)
        create_monster(spawnIds=[207,208,209], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[207,208,209]):
            return 사다리활성화()


class 사다리활성화(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[2001], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[2002], visible=True, animationEffect=True, animationDelay=4)
        set_ladder(triggerIds=[2003], visible=True, animationEffect=True, animationDelay=6)
        set_ladder(triggerIds=[2004], visible=True, animationEffect=True, animationDelay=8)
        set_ladder(triggerIds=[2005], visible=True, animationEffect=True, animationDelay=10)
        set_ladder(triggerIds=[2006], visible=True, animationEffect=True, animationDelay=12)
        set_ladder(triggerIds=[2007], visible=True, animationEffect=True, animationDelay=14)
        create_monster(spawnIds=[210,211,212], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[210,211,212]):
            return 씨앗1_활성화()


class 씨앗1_활성화(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=1, isEnable=True)
        set_user_value(triggerId=99990002, key='Seed1start', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Seed1interact', value=1):
            return 씨앗1_전투()


class 씨앗1_전투(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9014], visible=False)
        set_agent(triggerIds=[9015], visible=False)
        set_agent(triggerIds=[9016], visible=False)
        set_agent(triggerIds=[9017], visible=False)
        set_agent(triggerIds=[9018], visible=False)
        create_monster(spawnIds=[213,214,215,216], arg2=False)
        set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], visible=False, arg3=0, arg4=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[213,214,215,216]):
            return 씨앗1_심기()


class 씨앗1_심기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9019], visible=False)
        set_agent(triggerIds=[9020], visible=False)
        set_agent(triggerIds=[9021], visible=False)
        set_agent(triggerIds=[9022], visible=False)
        set_mesh(triggerIds=[1001,1002,1003,1004], visible=True, arg3=0, arg4=250, arg5=3)
        set_interact_object(triggerIds=[10002112], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002112], arg2=0):
            return 씨앗2_활성화()


class 씨앗2_활성화(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9023], visible=False)
        set_agent(triggerIds=[9024], visible=False)
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=True)
        set_user_value(triggerId=99990002, key='Seed1start', value=2)
        set_user_value(triggerId=99990003, key='Seed2start', value=1)
        set_mesh(triggerIds=[1005,1006], visible=True, arg3=0, arg4=250, arg5=3)
        set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> state.State:
        if user_value(key='Seed2interact', value=1):
            return 씨앗2_전투()


class 씨앗2_전투(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9025], visible=False)
        set_agent(triggerIds=[9026], visible=False)
        set_agent(triggerIds=[9027], visible=False)
        set_agent(triggerIds=[9028], visible=False)
        set_agent(triggerIds=[9029], visible=False)
        set_event_ui(type=1, arg2='$02020100_BF__MAIN__1$', arg3='5000')
        create_monster(spawnIds=[111,112,113,114,115,116], arg2=False)
        set_mesh(triggerIds=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], visible=False, arg3=0, arg4=0)
        set_interact_object(triggerIds=[10002113], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002113], arg2=0):
            return 발판1_지역감지()


class 발판1_지역감지(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9030], visible=False)
        set_agent(triggerIds=[9031], visible=False)
        set_agent(triggerIds=[9032], visible=False)
        set_agent(triggerIds=[9033], visible=False)
        set_agent(triggerIds=[9034], visible=False)
        set_actor(triggerId=1403, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        set_mesh(triggerIds=[1221,1222,1223,1224,1225,1226,1227,1228,1229,1230], visible=False, arg3=0, arg4=0)
        destroy_monster(spawnIds=[111,112,113,114,115,116])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[903]):
            return 발판1_활성화대기()


class 발판1_활성화대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[225,226], arg2=False)
        set_user_value(triggerId=99990003, key='Seed2start', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='Seed3interact', value=1):
            return 발판1_몬스터처리()
        if monster_dead(boxIds=[225,226]):
            return 발판1_몬스터처리()


class 발판1_몬스터처리(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990004, key='Seed3start', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Seed3interact', value=1):
            return 발판1_활성화()


class 발판1_활성화(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002122], state=1)
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        enable_spawn_point_pc(spawnId=3, isEnable=True)
        create_monster(spawnIds=[121,122,123,124], arg2=False)
        set_breakable(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], enabled=True)
        set_breakable(triggerIds=[5011,5012,5013,5014,5015,5016,5017,5018,5019], enabled=True)

    def on_tick(self) -> state.State:
        if user_value(key='EliteClear', value=1):
            return 보스전()


class 보스전(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990005, key='Seed4start', value=2)
        destroy_monster(spawnIds=[111,112,113,114,115,116,117,118,119])
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)


