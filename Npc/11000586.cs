using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000586: Injured Guard
/// </summary>
public class _11000586 : NpcScript {
    internal _11000586(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 50;60;70;80
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002370$ 
                // - Ugh... 
                return true;
            case 50:
                // $script:0831180407002375$ 
                // - H-help... 
                return true;
            case 60:
                // $script:0831180407002376$ 
                // - Ugh... 
                return true;
            case 70:
                // $script:0831180407002377$ 
                // - Ugh... No... 
                return true;
            case 80:
                // $script:0831180407002378$ 
                // - I can't... die like this... 
                return true;
            default:
                return true;
        }
    }
}
