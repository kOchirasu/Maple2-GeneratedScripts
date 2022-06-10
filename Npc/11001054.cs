using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001054: Nomar
/// </summary>
public class _11001054 : NpcScript {
    internal _11001054(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003600$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407003603$ 
                // - People say that sometimes dreams, do come true. I hope they're right.
                switch (selection) {
                    // $script:0831180407003604$
                    // - What's your dream?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407003605$ 
                // - My dream isn't much. I just want to be a successful businessman. I may be delivering pizzas now, but I know I can make it big if I work hard enough.
                return true;
            default:
                return true;
        }
    }
}
