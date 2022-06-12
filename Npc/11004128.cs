using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004128: Ishura
/// </summary>
public class _11004128 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720143007010499$
    // - I'm sorry I made you worry...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720143007010500$
                // - I'm not sure how I can face everyone...
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
