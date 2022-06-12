using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004268: West Auto Bridge
/// </summary>
public class _11004268 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011222$
    // - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011223$
                // - <font color="#909090">(This bridge connects the city to the desert of Karkar. It plays a major role in the development of the island.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011224$
                // - <font color="#909090">(This wonderful bridge was co-designed by the genius architect brother Opath and Oparts. The younger brother, Oparts, was in charge of the western exchange. His flair for the fabulous is evident in the bridge's flashy lights.)</font>
                return 10;
            case (10, 2):
                // $script:0911203207011225$
                // - <font color="#909090">(There are over 100 lights in use on the West Auto Bridge, and they symbolize the glamor and promise of the big city.)</font>
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
