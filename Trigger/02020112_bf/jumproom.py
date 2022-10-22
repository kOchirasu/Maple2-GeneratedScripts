""" trigger/02020112_bf/jumproom.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        set_effect(triggerIds=[8005], visible=False)
        set_effect(triggerIds=[8006], visible=False)
        set_effect(triggerIds=[8007], visible=False)
        set_effect(triggerIds=[8008], visible=False)
        set_user_value(triggerId=99990009, key='ButtonSuccess', value=0)
        set_user_value(triggerId=99990010, key='ButtonSuccess', value=0)
        set_user_value(triggerId=99990011, key='ButtonSuccess', value=0)
        set_user_value(triggerId=99990012, key='ButtonSuccess', value=0)
        set_user_value(triggerId=99990001, key='MonsterDead', value=0)
        set_actor(triggerId=9905, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9906, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9907, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9908, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')

    def on_tick(self) -> state.State:
        if count_users(boxId=931, boxId=4, operator='GreaterEqual'):
            return 감지()
        if user_detected(boxIds=[931], jobCode=0):
            return 감지()


class 감지(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8005], visible=True)
        set_effect(triggerIds=[8006], visible=True)
        set_effect(triggerIds=[8007], visible=True)
        set_effect(triggerIds=[8008], visible=True)

    def on_tick(self) -> state.State:
        if all_of():
            return 성공()


class 성공(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990021, key='Reconnect', value=2) # <재접속 유저를 위해 버프 지속적으로 쏴주기 캔슬>
        set_event_ui(type=1, arg2='$02020112_BF__JUMPROOM__0$', arg3='5000')
        set_gravity(gravity=0)
        set_effect(triggerIds=[8005], visible=False)
        set_effect(triggerIds=[8006], visible=False)
        set_effect(triggerIds=[8007], visible=False)
        set_effect(triggerIds=[8008], visible=False)
        add_buff(boxIds=[931], skillId=70002112, level=1, arg5=False)
        set_user_value(triggerId=99990009, key='ButtonSuccess', value=1)
        set_user_value(triggerId=99990010, key='ButtonSuccess', value=1)
        set_user_value(triggerId=99990011, key='ButtonSuccess', value=1)
        set_user_value(triggerId=99990012, key='ButtonSuccess', value=1)
        set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509], visible=False, arg3=0, arg4=20, arg5=3)
        set_mesh(triggerIds=[1510,1511,1512,1513,1514,1515,1516,1517,1518], visible=False, arg3=0, arg4=20, arg5=3)
        set_mesh(triggerIds=[1519,1520,1521,1522,1523,1524,1525,1526,1527], visible=False, arg3=0, arg4=20, arg5=3)
        set_mesh(triggerIds=[1528,1529,1530,1531,1532,1533,1534,1535,1536], visible=False, arg3=0, arg4=20, arg5=3)
        set_actor(triggerId=9905, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')
        set_actor(triggerId=9906, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')
        set_actor(triggerId=9907, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')
        set_actor(triggerId=9908, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')
        create_monster(spawnIds=[152,153,154,155], arg2=False)
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=1, isEnable=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[152,153,154,155]):
            set_user_value(triggerId=99990001, key='MonsterDead', value=1)
            return None


