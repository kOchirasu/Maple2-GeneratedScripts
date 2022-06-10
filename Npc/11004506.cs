using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004506: Mannstad Sentry
/// </summary>
public class _11004506 : NpcScript {
    internal _11004506(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012436$ 
                // - I know your face. Road in on that primitive flying boat, didn't you? 
                return true;
            case 10:
                // $script:1228182607012437$ 
                // - I know your face. Road in on that primitive flying boat, didn't you? 
                switch (selection) {
                    // $script:1228182607012438$
                    // - That's right.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1228182607012439$ 
                // - Hmph. You did good work in Richmonde, I'll give you that. 
                return true;
            default:
                return true;
        }
    }
}
