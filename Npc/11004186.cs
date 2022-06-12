using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004186: Darphony
/// </summary>
public class _11004186 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010634$
    // - Ah... N-nice to meet you... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010635$
                // - I came here to get t-t-tougher, so I can chase off the w-wolves plaguing our farm.
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
