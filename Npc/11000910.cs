using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000910: Renji
/// </summary>
public class _11000910 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003272$
    // - There's nothing to life. Just let nature take its course.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003274$
                // - Stop bothering me. I don't have time for chitchat!
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
