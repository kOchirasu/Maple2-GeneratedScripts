using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000280: Ted
/// </summary>
public class _11000280 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001090$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001093$
                // - A castle once stood on this very spot, the ancestral home of the Andreas. They were a noble family with close ties to the royals dating back generations. Then one day... the castle simply vanished.
                return 30;
            case (30, 1):
                // $script:0831180407001094$
                // - That guy does nothing but read books all day. He's supposed to be investigating the scene.
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
