using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000235: Tracy
/// </summary>
public class _11000235 : NpcScript {
    internal _11000235(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001000$ 
                // - Sigh... 
                return true;
            case 40:
                // $script:0831180407001004$ 
                // - Mm? You're not the person I saw. 
                switch (selection) {
                    // $script:0831180407001005$
                    // - What are you doing?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001006$ 
                // - I don't know. I don't know why I'm doing this, so please stop talking to me. 
                return true;
            default:
                return true;
        }
    }
}
