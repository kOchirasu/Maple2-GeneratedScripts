using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001121: Dr. Collins
/// </summary>
public class _11001121 : NpcScript {
    internal _11001121(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0910171307003826$ 
                // - What brings you?
                return true;
            case 30:
                // $script:0915113107003927$ 
                // - Those on the cutting edge of technological research often complain about lack of funds, resources, and other material things. The only thing I lack is time... Say, how old do you think I am?
                switch (selection) {
                    // $script:0915113107003928$
                    // - You look young-ish to me.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0915113107003929$
                    // - You look like an old geezer. 50-plus, at least.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0915113107003930$ 
                // - Hmph! Flattery will get you nowhere with me. Or perhaps you need to see an eye doctor.
                return true;
            case 32:
                // $script:0915113107003931$ 
                // - Close enough! There's so much I want to study, but I'm past my prime. <i>If only there were more time...!</i> Wait... That gives me an idea...
                return true;
            default:
                return true;
        }
    }
}
