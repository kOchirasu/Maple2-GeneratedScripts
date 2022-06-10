using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000744: Sikken
/// </summary>
public class _11000744 : NpcScript {
    internal _11000744(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002888$ 
                // - I may be old, but I'm young at heart. 
                return true;
            case 20:
                // $script:0831180407002890$ 
                // - Don't judge a book by its cover. I may be old, but I'm still a girl on the inside.  
                return true;
            default:
                return true;
        }
    }
}
