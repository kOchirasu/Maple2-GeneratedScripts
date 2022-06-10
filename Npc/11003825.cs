using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003825: Tristan
/// </summary>
public class _11003825 : NpcScript {
    internal _11003825(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0115140307009749$ 
                // - Let's get to business. 
                return true;
            case 10:
                // $script:0115140307009750$ 
                // - ...Finally, the time has come. 
                return true;
            default:
                return true;
        }
    }
}
