using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000237: Micky
/// </summary>
public class _11000237 : NpcScript {
    internal _11000237(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001013$ 
                // - Argh, this is awful! 
                return true;
            case 30:
                // $script:0831180407001016$ 
                // - Hm? Why did you call me?
                switch (selection) {
                    // $script:0831180407001017$
                    // - What are you doing?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407001018$ 
                // - I don't know. Don't ask!
                return true;
            default:
                return true;
        }
    }
}
