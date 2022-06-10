using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000352: Steve
/// </summary>
public class _11000352 : NpcScript {
    internal _11000352(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001463$ 
                // - Can I help you? 
                return true;
            case 40:
                // $script:0831180407001466$ 
                // - You can't step on flowers like that! Don't lie to me, I saw you! 
                return true;
            default:
                return true;
        }
    }
}
