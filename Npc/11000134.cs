using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000134: Wolf Heart
/// </summary>
public class _11000134 : NpcScript {
    internal _11000134(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000557$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:0831180407000558$ 
                // - Once a year, the Murpagoth warriors go on a pilgrimage through the Vayar Mountains. By the time they return, they've grown much stronger than they were before. 
                return true;
            default:
                return true;
        }
    }
}
