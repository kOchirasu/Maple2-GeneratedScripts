using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001341: Donnie
/// </summary>
public class _11001341 : NpcScript {
    internal _11001341(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005284$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:1217012607005287$ 
                // - Where are all these bugs coming from? They'll take over the skate park at this rate. Then Ludari City... and then, the world! 
                return true;
            default:
                return true;
        }
    }
}
