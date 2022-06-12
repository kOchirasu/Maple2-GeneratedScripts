using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000108: Roy
/// </summary>
public class _11000108 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000442$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000445$
                // - I heard $map:02000001$ is filled with beautiful ladies, so I came here, all decked out. What a waste of time. And now I'm stuck here!
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
