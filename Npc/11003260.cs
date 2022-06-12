using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003260: Lian
/// </summary>
public class _11003260 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008196$
    // - Ah, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008197$
                // - Everyone's safe, thanks to you. I hope you won't mind if we call on your help again in the future.
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
