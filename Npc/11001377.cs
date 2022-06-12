using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001377: Locault
/// </summary>
public class _11001377 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217144507005365$
    // - Hm...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217144507005368$
                // - What, you think a woman can't be a fight manager? Just watch. I'm going to turn Boh and every other one of my clients into world champions.
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
