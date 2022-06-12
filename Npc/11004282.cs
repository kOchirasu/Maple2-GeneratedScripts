using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004282: Loose Tile
/// </summary>
public class _11004282 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011296$
    // - <font color="#909090">(A distant roar echoes through the air.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011297$
                // - <font color="#909090">(A distant roar echoes through the air.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011298$
                // - <font color="#909090">(The tile is loose, but the roar reverberates through your body. Your every instinct tells you to run.)</font>
                return 10;
            case (10, 2):
                // $script:0913151207011309$
                // - <font color="#909090">(For a brief moment, you swear you see something moving through the crack in the floor. Surely you imagined it...)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
