using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000394: Emma
/// </summary>
public class _11000394 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001600$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001602$
                // - They say that old miser, $npcName:11000252[gender:0]$, is the worst... but they haven't met $npcName:11000491[gender:1]$!
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
