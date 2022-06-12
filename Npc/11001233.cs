using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001233: Rejan
/// </summary>
public class _11001233 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1125194807004478$
    // - Ugh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1125194807004481$
                // - Ugh... I was injured by a trap, and $npc:11001244[gender:0]$ ran on ahead on his own.
                switch (selection) {
                    // $script:1205222707004732$
                    // - What happened?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1205222707004733$
                // - We tracked $npcName:11001231[gender:0]$ and his Jibricia followers here, but they had already filled the passage with traps. I'm worried $npcName:11001244[gender:0]$ might be in danger.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
