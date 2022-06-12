using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001687: Zabeth
/// </summary>
public class _11001687 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0629000607006488$
    // - What're you staring at? You want a piece of me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0629000607006491$
                // - Whatever you want from me, it can wait.
                switch (selection) {
                    // $script:0706173707006648$
                    // - Were you worried about $npcName:11001679[gender:0]$?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0706173707006649$
                // - Wh-who's worried? Stop talking nonsense, or I'll beat the stuffing outta you!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
