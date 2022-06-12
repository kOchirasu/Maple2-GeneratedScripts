using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003370: Kyle
/// </summary>
public class _11003370 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0516225807008487$
    // - Heheheh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0516225807008489$
                // - Savor the moment.
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
