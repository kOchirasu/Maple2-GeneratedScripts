using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001196: Grue
/// </summary>
public class _11001196 : NpcScript {
    internal _11001196(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1016202007004202$ 
                // - Let's have a look at the requisition form... <i>Are you kidding me?</i> I'm not dealing with this right now. 
                return true;
            case 30:
                // $script:1016202007004205$ 
                // - Mm.. What? 
Is there something you need? 
                switch (selection) {
                    // $script:1016202007004206$
                    // - Show me what you have to sell.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1016202007004207$ 
                // - All right, have a looksie in my bag... 
                // $script:1016202007004208$ 
                // - ...Wait, what am I doing? I'm not some blasted shopkeep! I support the employees of the broadcasting station. Coffee, snacks, transportation, unsolicited advice. I get them whatever they need. I'm a key member of the team, so don't you forget it! 
                return true;
            default:
                return true;
        }
    }
}
