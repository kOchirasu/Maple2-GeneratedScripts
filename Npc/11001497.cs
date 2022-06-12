using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001497: Tara
/// </summary>
public class _11001497 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0118150907005824$
    // - I'm happy to be friends with such great people.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0118150907005827$
                // - I'm hoping I can relax. At least for today.
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
