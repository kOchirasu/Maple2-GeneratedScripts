using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003959: Berserker
/// </summary>
public class _11003959 : NpcScript {
    internal _11003959(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010009$ 
                // - Who're you? 
                return true;
            case 20:
                // $script:0614143707010010$ 
                // - You look pretty tough! Up for a sparring match? 
                return true;
            default:
                return true;
        }
    }
}
