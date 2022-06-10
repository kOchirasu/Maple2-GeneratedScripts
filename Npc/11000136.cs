using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000136: Tina
/// </summary>
public class _11000136 : NpcScript {
    internal _11000136(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000562$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:0831180407000563$ 
                // - This wolf's name is Buka. He's my friend.
                return true;
            default:
                return true;
        }
    }
}
