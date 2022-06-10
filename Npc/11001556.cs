using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001556: Laoz
/// </summary>
public class _11001556 : NpcScript {
    internal _11001556(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0617105607006360$ 
                // - Our minds and bodies follow each other in harmony. Consider, the truly wise speak with wisdom, and also act with wisdom.
                return true;
            case 30:
                // $script:0727223007006790$ 
                // - Finally, you have arrived.
                switch (selection) {
                    // $script:0727223007006791$
                    // - You summoned me?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0727223007006792$ 
                // - Indeed. Your training has brought you to an important crossroad. According to our traditions, it is time for you to set out on a journey to test your skills in the outside world.
                // $script:0727223007006793$ 
                // - However, the presence of this terrible darkness must be dealt with first. We can discuss your training later.
                return true;
            default:
                return true;
        }
    }
}
