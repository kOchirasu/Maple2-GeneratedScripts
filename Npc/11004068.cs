using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004068: Springs Totem
/// </summary>
public class _11004068 : NpcScript {
    internal _11004068(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010140$ 
                // - <font color="#909090">(The bubbling water behind this statue is just the right temperature. There's a plaque on the totem.)</font>
                return true;
            case 10:
                // $script:0619202207010141$ 
                // - <font color="#909090">(The bubbling water behind this statue is just the right temperature. There's a plaque on the totem.)</font>
                // $script:0619202207010142$ 
                // - <i>Dealing with aches? Pains? Fatigue? Skin blemishes? Then take a soak at these world-renown hot springs! A five minute soak in these naturally heated waters is all you need to feel like a new person!</i>
                // $script:0625111007010361$ 
                // - <i>The people of Perion know that nothing is better after a long day of hunting than a dip on the springs. And best of all, it's free to use!</i>
                return true;
            default:
                return true;
        }
    }
}
