using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000253: Mino
/// </summary>
public class _11000253 : NpcScript {
    internal _11000253(INpcScriptContext context) : base(context) {
        Id = 1;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000391$ 
                // - How may I help you?
                return true;
            case 1:
                // $script:0831180610000395$ functionID=1 
                // - Prepare your hair for the <i>unimaginable</i>. The wild beast in my soul will <i>possess</i> these scissors and summon your desired hairstyle from your memories.
                switch (selection) {
                    // $script:0831180610000396$
                    // - Do it! I'm ready!
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
