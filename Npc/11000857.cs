using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000857: Monshel
/// </summary>
public class _11000857 : NpcScript {
    internal _11000857(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003115$ 
                // - I'm not doing this because I want to.
                return true;
            case 30:
                // $script:0831180407003118$ 
                // - Please. Please, don't stare.
                // $script:0831180407003119$ 
                // - ...
                // $script:0831180407003120$ 
                // - S-stop staring!
                return true;
            default:
                return true;
        }
    }
}
