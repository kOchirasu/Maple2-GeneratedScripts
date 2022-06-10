using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000323: Tony
/// </summary>
public class _11000323 : NpcScript {
    internal _11000323(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50;60;70
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001300$ 
                // - How may I help you?
                return true;
            case 40:
                // $script:0831180407001303$ 
                // - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot warrior? 
                return true;
            case 50:
                // $script:0831180407001304$ 
                // - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot mage? 
                return true;
            case 60:
                // $script:0831180407001305$ 
                // - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot archer? 
                return true;
            case 70:
                // $script:0831180407001306$ 
                // - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot thief? 
                return true;
            default:
                return true;
        }
    }
}
