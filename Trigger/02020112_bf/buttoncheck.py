""" trigger/02020112_bf/buttoncheck.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_actor(triggerId=9901, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9902, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9903, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9904, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621], visible=False, arg3=0, arg4=20, arg5=3)
        set_mesh(triggerIds=[1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640], visible=False, arg3=0, arg4=20, arg5=3)
        set_mesh(triggerIds=[1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660], visible=False, arg3=0, arg4=20, arg5=3)
        set_user_value(triggerId=99990016, key='respawn', value=0)
        set_user_value(triggerId=99990003, key='Timer', value=0)
        set_user_value(triggerId=99990021, key='Reconnect', value=0)
        add_buff(boxIds=[916], skillId=70002104, level=1, arg5=False)
        set_effect(triggerIds=[8001], visible=True)
        set_effect(triggerIds=[8002,8003,8004], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='GravityRoom', value=1):
            return 작동()


class 작동(state.State):
    def on_enter(self):
        add_buff(boxIds=[916], skillId=70002104, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[911], jobCode=0):
            return 감지_1층()


class 감지_1층(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8001], visible=False)
        set_effect(triggerIds=[8002], visible=True)
        set_effect(triggerIds=[8003], visible=True)
        set_effect(triggerIds=[8004], visible=True)
        set_user_value(triggerId=99990003, key='Timer', value=1)
        set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621], visible=True, arg3=0, arg4=20, arg5=3)
        set_mesh(triggerIds=[1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640], visible=True, arg3=0, arg4=20, arg5=3)
        set_mesh(triggerIds=[1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660], visible=True, arg3=0, arg4=20, arg5=3)
        set_actor(triggerId=9901, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')
        set_actor(triggerId=9902, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9903, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9904, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        add_buff(boxIds=[916], skillId=70002103, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if user_value(key='TimerReset', value=1):
            return 대기()
        if user_detected(boxIds=[912], jobCode=0):
            return 감지_2층()


class 감지_2층(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8002], visible=False)
        set_user_value(triggerId=99990016, key='respawn', value=1)
        add_buff(boxIds=[916], skillId=70002103, level=1, arg5=False)
        set_actor(triggerId=9902, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')

    def on_tick(self) -> state.State:
        if user_value(key='TimerReset', value=1):
            return 대기()
        if user_detected(boxIds=[913], jobCode=0):
            return 감지_3층()


class 감지_3층(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8003], visible=False)
        add_buff(boxIds=[916], skillId=70002103, level=1, arg5=False)
        set_actor(triggerId=9903, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')

    def on_tick(self) -> state.State:
        if user_value(key='TimerReset', value=1):
            return 대기()
        if user_detected(boxIds=[914], jobCode=0):
            return 감지_4층()


class 감지_4층(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8004], visible=False)
        set_actor(triggerId=9904, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')
        add_buff(boxIds=[916], skillId=70002105, level=1, arg5=False)
        set_gravity(gravity=-32)
        set_event_ui(type=1, arg2='$02020112_BF__BUTTONCHECK__0$', arg3='5000')
        set_user_value(triggerId=99990016, key='respawn', value=2) # <1층 스폰 중지>
        set_user_value(triggerId=99990003, key='Timer', value=2)
        set_user_value(triggerId=99990001, key='GravityRoom', value=2)
        set_user_value(triggerId=99990021, key='Reconnect', value=1) # <재접속 유저를 위해 버프 지속적으로 쏴주기>
        set_actor(triggerId=9901, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9902, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9903, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9904, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621], visible=False, arg3=0, arg4=20, arg5=3)
        set_mesh(triggerIds=[1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640], visible=False, arg3=0, arg4=20, arg5=3)
        set_mesh(triggerIds=[1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660], visible=False, arg3=0, arg4=20, arg5=3)


