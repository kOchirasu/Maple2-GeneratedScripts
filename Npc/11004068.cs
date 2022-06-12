using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004068: Springs Totem
/// </summary>
public class _11004068 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010140$
    // - <font color="#909090">(The bubbling water behind this statue is just the right temperature. There's a plaque on the totem.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010141$
                // - <font color="#909090">(The bubbling water behind this statue is just the right temperature. There's a plaque on the totem.)</font>
                return 10;
            case (10, 1):
                // $script:0619202207010142$
                // - <i>Dealing with aches? Pains? Fatigue? Skin blemishes? Then take a soak at these world-renown hot springs! A five minute soak in these naturally heated waters is all you need to feel like a new person!</i>
                return 10;
            case (10, 2):
                // $script:0625111007010361$
                // - <i>The people of Perion know that nothing is better after a long day of hunting than a dip on the springs. And best of all, it's free to use!</i>
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
