using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000599: Lenty
/// </summary>
public class _11000599 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002398$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002401$
                // - There are treasure chests hidden all over the world, and they're highly sought after by adventurers.
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
