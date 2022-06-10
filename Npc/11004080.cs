using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004080: Blacksmith's Workbench
/// </summary>
public class _11004080 : NpcScript {
    internal _11004080(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0620203007010268$ 
                // - <font color="#909090">(This workbench is particularly cluttered.)</font> 
                return true;
            case 10:
                // $script:0620203007010269$ 
                // - <font color="#909090">(This workbench is particularly cluttered.)</font> 
                // $script:0620203007010270$ 
                // - <font color="#909090">(Many weapon parts are scattered across the top of the bench. Everything on it is coated with a fine layer of onyx dust. It appears Ophelia's skill is the result of countless hours of practice.)</font> 
                // $script:0620203007010271$ 
                // - <font color="#909090">(On the corner of the workbench, there's a fancy business card that seems out of place. <i>"Unload Your Unused Trash! Ophelia's Hardware Store! We Buy All Scrap Metal. Call Us! 902-555-3959")</i></font> 
                // $script:0625140507010368$ 
                // - <font color='#909090'>(Is the enchanting business not working out? What a strange turn of events...)</font> 
                return true;
            default:
                return true;
        }
    }
}
