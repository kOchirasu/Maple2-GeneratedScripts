using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004159: Beatrice
/// </summary>
public class _11004159 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0730132107010543$
    // - I pray everyone is safe...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0730132107010544$
                // - Please don't overexert yourself.
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
