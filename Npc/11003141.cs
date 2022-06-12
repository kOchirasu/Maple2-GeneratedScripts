using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003141: Rina
/// </summary>
public class _11003141 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0222124707007953$
    // - What's the matter, dear?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0224093607007962$
                // - Cooking in the kitchen is fine, but I'll always prefer cooking outdoors for how liberating it feels.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
