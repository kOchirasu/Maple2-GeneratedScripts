using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004212: Muky
/// </summary>
public class _11004212 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806052107010679$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806052107010680$
                // - It's my goal in life to one day be as shroomy as the $npcName:11004213[gender:0]$. Or failing that, at least to mush it up with the best of them.
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
