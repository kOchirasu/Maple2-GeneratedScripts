using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003158: Carly
/// </summary>
public class _11003158 : NpcScript {
    internal _11003158(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008054$ 
                // - Can I help you?
                return true;
            case 40:
                // $script:0306155707008058$ 
                // - This is my favorite place. It's beautiful and smells even better. And, you might not know this, but I can also eat delicious food here!
                return true;
            default:
                return true;
        }
    }
}
