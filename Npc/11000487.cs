using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000487: Miyu
/// </summary>
public class _11000487 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002134$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002137$
                // - Ah... Doesn't $npcName:11000406[gender:0]$ look handsome? As for you? Not so much.
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
