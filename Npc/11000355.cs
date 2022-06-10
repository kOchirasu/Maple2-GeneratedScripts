using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000355: Walko
/// </summary>
public class _11000355 : NpcScript {
    internal _11000355(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001478$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407001480$ 
                // - Woof! One day, a meteor fell from the sky. Be careful, it might have friends.
                return true;
            default:
                return true;
        }
    }
}
