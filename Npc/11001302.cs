using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001302: Ereve
/// </summary>
public class _11001302 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1215203907005020$
    // - $MyPCName$, what brings you to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1215203907005021$
                // - $MyPCName$, please don't disappoint me. I know it's difficult, but keep up your efforts to save our world.
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
