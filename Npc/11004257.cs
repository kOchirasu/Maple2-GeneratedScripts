using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004257: Steam Plume
/// </summary>
public class _11004257 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0829171107010974$
    // - <font color="#909090">(Hot steam rises from deep underground.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0829171107010975$
                // - <font color="#909090">(Hot steam rises from deep underground.)</font>
                return 10;
            case (10, 1):
                // $script:0831140807011026$
                // - <font color="#909090">(Steam rises up from what appears to be a bottomless chasm. It's quite hot, and you think you smell sulfur.)</font>
                return 10;
            case (10, 2):
                // $script:0831140807011027$
                // - <font color="#909090">(Rumor has it that $npcNamePlural:21000053$ make their den below. The steam that rises from deep underground is said to be toxic to humans.)</font>
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
