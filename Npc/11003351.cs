using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003351: Ralph's Lackey
/// </summary>
public class _11003351 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0517164307008499$
    // - Taking down the boss... You're something else, you know that?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0517164307008502$
                // - The big guy's been training hard for days now. You really lit a fire under his butt, I'll tell you that.
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
