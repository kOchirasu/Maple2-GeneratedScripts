using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001458: Fin
/// </summary>
public class _11001458 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1222171407005462$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1222171407005465$
                // - We aren't some fly-by-night operation. We're the Blackstars!
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
