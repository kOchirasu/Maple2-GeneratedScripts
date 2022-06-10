using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000327: Natalie
/// </summary>
public class _11000327 : NpcScript {
    internal _11000327(INpcScriptContext context) : base(context) {
        Id = 70;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001330$ 
                // - How may I help you?
                return true;
            case 60:
                // $script:0820145207008892$ 
                // - Everything in this world has a purpose and a story to tell.
                return true;
            case 70:
                // $script:0502125007014664$ 
                // - How can I help you?
                return true;
            default:
                return true;
        }
    }
}
