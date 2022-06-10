using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000389: Tivo
/// </summary>
public class _11000389 : NpcScript {
    internal _11000389(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001581$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407001584$ 
                // - Since the big split, $map:2000115$ has been attracting all kinds of lookie-loos. And a true businessman never wastes a good opportunity like this! 
                return true;
            default:
                return true;
        }
    }
}
