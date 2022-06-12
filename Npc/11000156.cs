using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000156: Sam
/// </summary>
public class _11000156 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000660$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000662$
                // - What do I do? I've got piles of packages, and the Royal Road to $map:02000001$ is all busted up.
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
