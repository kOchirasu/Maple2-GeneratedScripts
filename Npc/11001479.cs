using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001479: Startz
/// </summary>
public class _11001479 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0106111607005765$
    // - Do you have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0106111607005766$
                // - I'm glad we've retrieved the Lumenstone, but the war with the Kargons is far from over.
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
