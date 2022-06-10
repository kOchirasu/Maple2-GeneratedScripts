using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000254: Jane
/// </summary>
public class _11000254 : NpcScript {
    internal _11000254(INpcScriptContext context) : base(context) {
        Id = 60;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001056$ 
                // - How may I help you?
                return true;
            case 60:
                // $script:0831180407001060$ 
                // - Hey, there! If you've got a style in mind, we can make it happen. If you don't, maybe a magazine will inspire you. Want one?
                switch (selection) {
                    // $script:0831180407001061$
                    // - Yep.
                    case 0:
                        Id = 0; // TODO: 61,62 | 63
                        return false;
                    // $script:0831180407001062$
                    // - I'd like some advice.
                    case 1:
                        Id = 64;
                        return false;
                }
                return true;
            case 61:
                // $script:0831180407001063$ functionID=1 
                // - Sure thing. This has all the latest styles. Have a seat and check them out.
                return true;
            case 62:
                // $script:0831180407001064$ 
                // - Err... I'm afraid you already have the only magazine we have. Sorry about that.
                return true;
            case 63:
                // $script:0831180407001065$ 
                // - Oh, friend... I'm afraid your bag is too heavy. Why don't you lighten it first?
                return true;
            case 64:
                // $script:0831180407001066$ 
                // - Sure! I love nothing more than helping match people with the hair of their dreams. Let's chat and find something that's totally you!
                return true;
            default:
                return true;
        }
    }
}
