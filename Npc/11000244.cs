using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000244: Mrs. Toulette
/// </summary>
public class _11000244 : NpcScript {
    internal _11000244(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001037$ 
                // - Can I help you? 
                return true;
            case 40:
                // $script:0831180407001041$ 
                // - Why are you talking to me? What do you want? 
                return true;
            case 50:
                // $script:0831180407001042$ 
                // - People say that the richer you get, the pickier you get. Makes sense, since you can have whatever you want with enough money. 
                return true;
            default:
                return true;
        }
    }
}
