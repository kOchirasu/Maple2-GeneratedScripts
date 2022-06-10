using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000014: Kalanko
/// </summary>
public class _11000014 : NpcScript {
    internal _11000014(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000067$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000069$ 
                // - W-who are you? You better not be here to steal anything. This is my spot!
                switch (selection) {
                    // $script:0831180407000070$
                    // - That's right.
                    case 0:
                        Id = 21;
                        return false;
                    // $script:0831180407000071$
                    // - No.
                    case 1:
                        Id = 22;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407000072$ 
                // - Hey, no! Get out! If we take too much stuff, they'll notice for sure!
                return true;
            case 22:
                // $script:0831180407000073$ 
                // - Oh, okay. Good. You'd better get out of here then, before someone sees you. And don't tell anyone you saw me in here!
                return true;
            default:
                return true;
        }
    }
}
