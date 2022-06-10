using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000834: Cathy Mart Employee
/// </summary>
public class _11000834 : NpcScript {
    internal _11000834(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003051$ 
                // - Welcome to Cathy Mart. 
                return true;
            case 40:
                // $script:0831180407003055$ 
                // - When is the next shift going to show up? I really have to go to the bathroom! ...Oh, shoot! Please excuse me, um, how may I help you? 
                return true;
            case 50:
                // $script:0831180407003056$ 
                // - You can pay for your items at the cashier over there. 
                return true;
            case 60:
                // $script:0831180407003057$ 
                // - Cathy Mart sells only the highest-quality products. If you find any items that don't seem to meet our standards, please don't hesitate to let me know. 
                return true;
            default:
                return true;
        }
    }
}
