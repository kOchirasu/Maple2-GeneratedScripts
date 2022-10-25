""" trigger/02000521_bf/barricade.xml """
import common


class ready(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[710]):
            return chaos_raid(self.ctx)


# 카오스 레벨이면 벽 생성
class chaos_raid(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return create_barricade(self.ctx)


class create_barricade(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799], visible=True, arg3=0, delay=200, scale=35)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[402]):
            return end(self.ctx)


class end(common.Trigger):
    pass


initial_state = ready
