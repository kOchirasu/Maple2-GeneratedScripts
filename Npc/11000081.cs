using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000081: Yoyo
/// </summary>
public class _11000081 : NpcScript {
    internal _11000081(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000372$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:0831180407000374$ 
                // - I like making shoes for my friends. Be my friend, and I'll give you a pair of shoes.
                return true;
            default:
                return true;
        }
    }
}
