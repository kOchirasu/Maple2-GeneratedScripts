using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004269: East Auto Bridge
/// </summary>
public class _11004269 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011226$
    // - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011227$
                // - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011228$
                // - <font color="#909090">(This wonderful bridge was designed by the genius architect brother Opath and Oparts. The older brother, Opath, was in charge of the eastern exchange.)</font>
                return 10;
            case (10, 2):
                // $script:0911203207011229$
                // - <font color="#909090">(He added intriguing detail and a touch of mischief to the design, including hidden magic portals and shortcuts.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
