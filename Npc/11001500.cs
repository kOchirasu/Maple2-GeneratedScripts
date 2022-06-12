using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001500: Dunba
/// </summary>
public class _11001500 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0118150907005836$
    // - What do I want to eat this time?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0118150907005839$
                // - Could you stop bothering me? I'm eating!
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
