using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003220: Joddy
/// </summary>
public class _11003220 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0404083307008245$
    // - And now we're fighting literal devils...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008246$
                // - I never thought I'd miss my drill sergeant...
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
