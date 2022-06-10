using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001947: Violin Student
/// </summary>
public class _11001947 : NpcScript {
    internal _11001947(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007493$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:1208184307007539$ 
                // - Are you here for the audition? You better grab your instrument and start practicing while you still can. 
                return true;
            default:
                return true;
        }
    }
}
