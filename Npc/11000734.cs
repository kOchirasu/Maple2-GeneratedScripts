using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000734: Delv
/// </summary>
public class _11000734 : NpcScript {
    internal _11000734(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000853$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000854$ 
                // - How do you like my hairstyle?
                return true;
            default:
                return true;
        }
    }
}
