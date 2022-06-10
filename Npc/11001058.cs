using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001058: Corniel
/// </summary>
public class _11001058 : NpcScript {
    internal _11001058(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003613$ 
                // - Will we ever see light again?  
                return true;
            case 30:
                // $script:0831180407003616$ 
                // - Everything in this world has light within it. I can see your light. It's warm. 
                return true;
            default:
                return true;
        }
    }
}
