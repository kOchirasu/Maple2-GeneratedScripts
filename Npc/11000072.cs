using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000072: Zenko
/// </summary>
public class _11000072 : NpcScript {
    internal _11000072(INpcScriptContext context) : base(context) {
        Id = 1;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000385$ 
                // - How can I help you? 
                return true;
            case 1:
                // $script:0831180610000389$ functionID=1 
                // - Welcome, $MyPCName$. Thinking about spicing up your look? I can give you any skin tone you like. Care to take a peek? 
                switch (selection) {
                    // $script:0831180610000390$
                    // - Yeah, let's do it!
                    case 0:
                        Id = 0;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
