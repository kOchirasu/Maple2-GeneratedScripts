using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000217: Candice
/// </summary>
public class _11000217 : NpcScript {
    internal _11000217(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000947$ 
                // - What is it? 
                return true;
            case 20:
                // $script:0831180407000949$ 
                // - I grew up in $map:02000084$, that's where my family lives. I heard about a job that paid well, so I moved all the way here. 
                // $script:0831180407000950$ 
                // - All I had to do was look after some rich guy's son. Man was that a mistake. This kid I'm looking after treats me worse than his cat. 
                return true;
            default:
                return true;
        }
    }
}
