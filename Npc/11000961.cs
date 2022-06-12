using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000961: Tinnie
/// </summary>
public class _11000961 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003339$
    // - Why can't I shake this bad feeling...?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003341$
                // - One day, I want to follow in $npcName:11000015[gender:1]$'s footsteps and become the leader of the Green Hoods. I want to earn the same respect that she did.
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
