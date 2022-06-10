using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000595: Scott
/// </summary>
public class _11000595 : NpcScript {
    internal _11000595(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002385$ 
                // - Hm... That's...  
                return true;
            case 50:
                // $script:0831180407002389$ 
                // - Mm? Are you a traveler? 
                switch (selection) {
                    // $script:0831180407002390$
                    // - What are you doing here?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407002391$ 
                // - Oh, me? I'm studying these creatures we call the fairfolk. All kinds of fairfolk inhabit forests like this. 
                return true;
            default:
                return true;
        }
    }
}
