using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000218: Billy
/// </summary>
public class _11000218 : NpcScript {
    internal _11000218(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000951$ 
                // - What is it? 
                return true;
            case 40:
                // $script:0831180407000955$ 
                // - People should be good to each other. You reap what you sow, as they say... 
                return true;
            default:
                return true;
        }
    }
}
