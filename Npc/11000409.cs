using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000409: Julian
/// </summary>
public class _11000409 : NpcScript {
    internal _11000409(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001728$ 
                // - Welcome, $MyPCName$! 
                return true;
            case 10:
                // $script:0831180407001729$ 
                // - The forest trail is too dangerous. We have to make it safe again, as soon as possible. 
                return true;
            case 20:
                // $script:0831180407001730$ 
                // - $npcName:99000041$ are making this trail too dangerous to travel. 
                return true;
            default:
                return true;
        }
    }
}
