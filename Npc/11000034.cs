using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000034: Mahio
/// </summary>
public class _11000034 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000189$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000191$
                // - Nothing's more important than peace of mind. I find mine snuggled up safe in bed.
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
