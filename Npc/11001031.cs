using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001031: Chano
/// </summary>
public class _11001031 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003525$
    // - Ugh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003528$
                // - $npcName:11000335[gender:0]$... Sigh... I don't know what to tell you about him... 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
