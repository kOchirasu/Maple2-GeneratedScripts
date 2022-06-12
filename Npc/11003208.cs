using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003208: Zeta
/// </summary>
public class _11003208 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0404083307008237$
    // - Thank you for saving my brother!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008238$
                // - I thought my bro was a goner... until you came along, that is.
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
