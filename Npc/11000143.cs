using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000143: Boen
/// </summary>
public class _11000143 : NpcScript {
    internal _11000143(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000581$ 
                // - Hello. 
                return true;
            case 30:
                // $script:0831180407000584$ 
                // - Sigh... See that big hotel on the cliff? It dropped from the sky one day, literally out of the blue. Since then, monsters have been swarming the area. It's getting impossible to do anything. 
                return true;
            case 40:
                // $script:0831180407000585$ 
                // - Huh? You think my name is funny. I disagree.  
                // $script:0831180407000586$ 
                // - Boen is easy to remember and rolls off the tongue beautifully. Go to the top of that cliff and shout my name. It'll echo for a long time. 
                return true;
            default:
                return true;
        }
    }
}
