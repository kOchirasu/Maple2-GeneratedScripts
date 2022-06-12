using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001340: Jenk
/// </summary>
public class _11001340 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217012607005279$
    // - Delicious food here! Get your delicious food!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1217012607005283$
                // - All my food is made with 100% love, guaranteed. You'll like 'em so much, you won't even notice if someone drops dead right next to you! They'll change your whole outlook on life!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
