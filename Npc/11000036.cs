using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000036: Arita
/// </summary>
public class _11000036 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000196$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000199$
                // - Love the flowers and trees as you love yourself. Without them, you wouldn't exist.
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
