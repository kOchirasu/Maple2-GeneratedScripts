using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001329: Dubore
/// </summary>
public class _11001329 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005235$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005238$
                // - Yesterday, 2895 guests passed on their way to $map:02010002$. Today, you are the 3527th guest.
                return 30;
            case (30, 1):
                // $script:1227194507005707$
                // - Ah... Why can't I simply forget my useless memories? Being able to remember everything is a curse!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
