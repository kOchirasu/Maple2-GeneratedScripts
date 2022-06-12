using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004195: Ereve
/// </summary>
public class _11004195 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010638$
    // - $MyPCName$, what brings you to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010639$
                // - You must always believe in yourself. Though the road is long and difficult, it is our duty to bring peace to this world.
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
