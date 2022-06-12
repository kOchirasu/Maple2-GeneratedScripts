using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004138: Doctor Harold
/// </summary>
public class _11004138 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0730132107010541$
    // - Sigh, another patient?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0730132107010542$
                // - And just who's going to treat <i>my</i> injuries?
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
