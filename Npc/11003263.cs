using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003263: Jorge
/// </summary>
public class _11003263 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008206$
    // - $MyPCName$... You did everything you could.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008207$
                // - The path to Ellinel is still blocked, but we'll find a way back.
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
