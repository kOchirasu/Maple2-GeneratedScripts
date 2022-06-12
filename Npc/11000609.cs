using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000609: Coye
/// </summary>
public class _11000609 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002504$
    // - Ah... What do I do? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002505$
                // - What do I do if $npcName:11000526[gender:0]$'s creditors come after me? How could he hang me out to dry like this?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
