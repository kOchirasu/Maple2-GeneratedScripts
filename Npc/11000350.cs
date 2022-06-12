using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000350: Jeremy
/// </summary>
public class _11000350 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001460$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001462$
                // - I've been traveling all my life, and the greatest lesson I've learned is to never waste anything. $npcName:21000029$, for example, has hundreds of practical uses. It's amazing stuff!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
