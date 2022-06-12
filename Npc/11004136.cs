using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004136: Eupheria
/// </summary>
public class _11004136 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0730132107010537$
    // - Your aura is one of virtue.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0730132107010538$
                // - All that lifeforce... will you give it to me?
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
