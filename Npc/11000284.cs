using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000284: Arwen
/// </summary>
public class _11000284 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001109$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001112$
                // - Getting along with humans is difficult. They're just so different!
                return 30;
            case (30, 1):
                // $script:0831180407001113$
                // - I know there are many good humans out there... but it's not easy to find them.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
