using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004254: Inscribed Totem
/// </summary>
public class _11004254 : NpcScript {
    internal _11004254(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0829171107010968$ 
                // - <font color="#909090">(The water in the "Demonspring", for which the surrounding area is named, is neither red nor black as one might expect, but rather a sickly translucent green.)</font>
                return true;
            case 10:
                // $script:0829171107010969$ 
                // - <font color="#909090">(The water in the "Demonspring", for which the surrounding area is named, is neither red nor black as one might expect, but rather a sickly translucent green.)</font>
                // $script:0831140807011011$ 
                // - <font color="#909090">(It's said that the spring was tainted long ago by the blood of the goddess of darkness. It is <i>also</i> said that this spring contains the blood of an ancient turtle. No one knows the truth of the matter.)</font>
                // $script:0831140807011012$ 
                // - <font color="#909090">(Nevertheless, it's probably best not to let the liquid touch you.)</font>
                return true;
            default:
                return true;
        }
    }
}
