using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001022: Raymon
/// </summary>
public class _11001022 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003472$
    // - Wh-what? You again?!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003475$
                // - Y-yes, I'm $npcName:11000526[gender:0]$.
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
